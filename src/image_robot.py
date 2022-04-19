import os

from bing_image_downloader import downloader
from keybert import KeyBERT

class ImageRobot:
    def __init__(self, summary, topic, img_dir="images"):
        self.summary = summary
        self.topic = topic
        self.img_dir = img_dir

    def keywords(self, txt, num_keywords=1):
        kw_model = KeyBERT()
        keywords = kw_model.extract_keywords(txt)
        return [tup[0] for tup in keywords[:num_keywords]]
    
    def __download_img(self, query, limit=1):

        downloader.download(query, limit=limit, output_dir=self.img_dir,
                            timeout=30, verbose=False)

    def get_images(self):
        file_paths = []
        for sent in self.summary:
            keyword = self.keywords(sent)[0]
            query = keyword + " and " + self.topic
            try:
                self.__download_img(query)
            except:
                print(f"Error downloading image for query {query}")

        for (dir_path, dir_names, file_names) in os.walk(self.img_dir):
            file_paths += [os.path.join(dir_path, file) for file in file_names]

        return file_paths

