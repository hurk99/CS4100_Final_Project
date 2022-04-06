import sys

from image_robot import ImageRobot
from summarizer_robot import SummarizerRobot


def main():
    main_topic = None
    article = None
    image_directory = None

    summarizer_robot = SummarizerRobot(article)
    summarized_text = summarizer_robot.summarize(1.2)

    image_robot = ImageRobot(summarized_text, image_directory)
    image_robot.get_images(main_topic)


if __name__ == "__main__":
    main()
