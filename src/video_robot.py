import cv2
from gtts import gTTS

# def tts(text, lang="en"):

#     gtts = gTTS(text=text, lang=lang, slow = True)
#     gtts.save("test.mp3")

class VideoRobot:
    def __init__(self, sentences, file_paths, height=1080, width=1920):
        self.sentences = sentences
        self.file_paths = file_paths
        self.height = height
        self.width = width
    
    def downscale(self):
        """downscales images that are bigger than 1080x1920"""
        for path in self.file_paths:
            img = cv2.imread(path)
            height, width = img.shape[:2]
            if height > self.height or width > self.width:
                downsize_factor = min(self.height/height,self.width/width)
                new_height = int(height * downsize_factor)
                new_width = int(width * downsize_factor)
                img = cv2.resize(img, (new_width,new_height), interpolation=cv2.INTER_AREA)
                cv2.imwrite(path, img)
        
    def expand_images_to_frame(self):
        """adds border to images so they fit the frame"""
        for path in self.file_paths:
            img = cv2.imread(path)
            height, width = img.shape[:2]
            vertical = int((self.height - height)/2)
            horizontal = int((self.width - width)/2)
            img = cv2.copyMakeBorder(img, vertical, vertical, horizontal, horizontal,
                 cv2.BORDER_CONSTANT, 0)
            img = cv2.resize(img, (self.width, self.height))
            cv2.imwrite(path, img)

    def force_resize(self):
        """
        force image to expand to frame resolution
        will not keep aspect ratio
        probably don't wanna use this function
        """
        for path in self.file_paths:
            img = cv2.imread(path)
            img = cv2.resize(img, (self.width,self.height), interpolation=cv2.INTER_AREA)
            cv2.imwrite(path, img)

    def img_to_video(self, output_path):
        """create video sequence from images"""
        fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
        video = cv2.VideoWriter(output_path, fourcc, 15, (self.width, self.height))
        for path in self.file_paths:
            img = cv2.imread(path)
            # check for correct resolution and write to video
            if img.shape[:2] == (self.height, self.width):
                video.write(img)
                
        cv2.destroyAllWindows()
        video.release()