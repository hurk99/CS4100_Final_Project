from image_robot import ImageRobot
from summarizer_robot import SummarizerRobot
from video_robot import VideoRobot
import os

txt = """
Northeastern University (NU or NEU) is a private research university with its main campus in Boston. 
Established in 1898, the university offers undergraduate and graduate programs on its main campus in 
Boston as well as satellite campuses in Charlotte, North Carolina; Seattle, Washington; San Jose, California; 
Oakland, California; Portland, Maine; and Toronto and Vancouver in Canada. In 2019, Northeastern purchased 
the New College of the Humanities in London, England. The university's enrollment is approximately 19,000 
undergraduate students and 8,600 graduate students. It is classified among "R1: Doctoral Universities
Very high research activity". Northeastern faculty and alumni include Nobel Prize laureates, Rhodes, Truman, 
and Marshall scholars. Undergraduate admission to the university is categorized as "most selective."

Northeastern features a cooperative education program, more commonly known as "co-op," that integrates 
classroom study with professional experience and includes over 3,100 partners across all seven continents. 
The program has been a key part of Northeastern's curriculum of experiential learning for more than a hundred 
years and is one of the largest co-op/internship programs in the world. While not required for all academic
disciplines, participation is nearly universal among undergraduate students. Northeastern also has a
comprehensive study abroad program that spans more than 170 universities and colleges.

Northeastern is a large, highly residential university. Most undergraduate students choose to live on campus but 
third-years and above have the option to live off campus. Seventy-eight percent of Northeastern students receive 
some form of financial aid. In the 2020–21 school year, the university has committed $355 million in grant and 
scholarship assistance. In 2019, Northeastern's six-year graduation rate was 89 percent.

The university's sports teams, the Northeastern Huskies, compete in NCAA Division I as members of the 
Colonial Athletic Association (CAA) in 18 varsity sports. The men's and women's hockey teams compete 
in Hockey East, while the men's and women's rowing teams compete in the Eastern Association of Rowing 
Colleges (EARC) and Eastern Association of Women's Rowing Colleges (EAWRC), respectively. Men's Track 
and Field has won the CAA back to back years in 2015 and 2016. In 2013, men's basketball won its first 
CAA regular season championship, men's soccer won the CAA title for the first time, and women's ice 
hockey won a record 16th Beanpot championship.[15] The Northeastern men's hockey team won the 2018, 2019, 
and 2020 Beanpot, defeating Boston University, Boston College, and Harvard.
"""


def main():
    # set main stuff
    main_topic = "northeastern university"
    article = txt
    img_dir = "../images"

    # summarize
    sum_bot = SummarizerRobot(article)
    summary = sum_bot.summarize(1.2)

    # look for images
    img_bot = ImageRobot(summary, main_topic, img_dir=img_dir)
    file_paths = img_bot.get_images()

    # turn images into a video
    vid_bot = VideoRobot(summary, file_paths)
    vid_bot.downscale()
    vid_bot.expand_images_to_frame()
    mp3_paths = vid_bot.tts()
    durations = vid_bot.get_mp3_durations(mp3_paths)
    vid_bot.img_to_video('../video.mp4', durations)
    vid_bot.add_sound()

if __name__ == "__main__":
    main()
