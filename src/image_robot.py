import re
import wikipedia as wiki
from nltk import tokenize
import os
from google_images_download import google_images_download
from PIL import Image
from nltk.tokenize import word_tokenize, sent_tokenize
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions


def convert_to_jpg(files):
    for f in files:
        img = Image.open(f)
        rgb_img = img.convert("RGB")
        rgb_img.save(f + ".jpg")


def rename_files(self, files):
    # TODO: Ensure that files will automatically be formatted correctly
    new_files_list = []
    for i in range(len(files)):
        try:
            new_name = "{0}/img{1}".format(self.download_directory, i)
            os.rename(files[i], new_name)
            new_files_list.append(new_name)
        except:
            continue

    return new_files_list


class ImageRobot:
    def __init__(self, script, image_directory):
        self.script = script
        self.image_directory = image_directory
        self.sentences = sent_tokenize(script)
        self.keywords_list = []
        self.keywords_dictionary = {}
        self.google_images = google_images_download.googleimagesdownload()
        # TODO: Get the API Key
        self.natural_language_understanding = NaturalLanguageUnderstandingV1(
            version="2018-11-16",
            iam_apikey="API_KEY_HERE",
            url="URL_HERE")

    def get_keywords(self):
        for sentence in self.sentences:
            response = self.natural_language_understanding.analyze(
                text=sentence,
                features=Features(keywords=KeywordsOptions(emotion=True,
                                                           sentiment=True))).get_result()

            temp_list = []
            for keyword in response["keywords"]:
                temp_list.append(keyword["text"])

            self.keywords_dictionary[sentence] = temp_list
            self.keywords_list.append(temp_list)

    def get_image(self, keyword, main_topic):
        search = keyword + " and " + main_topic
        arguments = {"keywords": search,
                     "limit": 1,
                     "print_urls": True,
                     "no_directory": True,
                     "size": "large",
                     "output_directory": self.image_directory}
        return self.google_images.download(arguments)[0][keyword]

    def get_images(self, main_topic):
        images_list = []
        for keyword in self.keywords_list:
            img = self.get_image(keyword, main_topic)
            images_list.append(img)

        images_list = rename_files(images_list)
        convert_to_jpg(images_list)
