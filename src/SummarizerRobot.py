import networkx as nx
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.cluster.util import cosine_distance


class SummarizerRobot:
    def __init__(self, raw_text):
        self.raw_text = raw_text

        # Stop word is a commonly used word that a search engine can be programmed to ignore
        # stopwords.words("english") is a given set of stopwords.
        self.stop_words = set(stopwords.words("english"))

        # Converts the raw_text into an array of words
        self.words = word_tokenize(raw_text)
        self.words = [word.lower() for word in self.words]

        # Converts the raw_text into an array of sentences
        self.sentences = sent_tokenize(raw_text)
        self.sentences = [sentence.lower() for sentence in self.sentences]

        # Create a 2D graph of each sentence compared to other sentences, each having a value showcasing their
        # similarity value
        self.similarity_matrix = np.zeros((len(self.sentences), len(self.sentences)))

        # How often did the word show up? The more often -> more valuable
        self.word_frequency_table = dict()

        # What is the worth of the sentence based on the worth of the word it has
        self.sentence_value_table = dict()

        # How unique is a given sentence? Higher the number, the less unique it is.
        self.sentence_similarity_table = dict()

    def read_article(self, file_name):
        self.sentences = list()
        file = open(file_name, "r")
        file_data = file.readline()
        article = file_data[0].split(". ")

        for sentence in article:
            # Clean out sentences
            sentence = sentence.lower()
            self.sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
        sentence.pop()

    def sentence_similarity(self, sentence1, sentence2):
        sentence_1_words = [word for word in sentence1]
        sentence_2_words = [word for word in sentence2]

        combined_sentence_words = list(set(sentence_1_words + sentence_2_words))
        sentence_1_vector = [0] * len(combined_sentence_words)
        sentence_2_vector = [0] * len(combined_sentence_words)
        for word in sentence1:
            if word not in self.stop_words:
                sentence_1_vector[combined_sentence_words.index(word)] += 1
        for word in sentence2:
            if word not in self.stop_words:
                sentence_2_vector[combined_sentence_words.index(word)] += 1
        """
        Example of what is going on here:
        Sentence_1_words = [a, b, b, c]
        Sentence_2_words = [b, b, c, d]
        combined_sentence_words = [a, b, c, d]
        
                             a  b  c  d
        sentence_1_vector = [1, 2, 1, 0]
        sentence_2_vector = [0, 2, 1, 1]
        """
        # Use cosine_distance to numerize the similarity between the two vectors.
        return 1 - cosine_distance(sentence_1_vector, sentence_2_vector)

    def create_similarity_matrix(self):
        for index_1 in range(len(self.sentences)):
            for index_2 in range(len(self.sentences)):
                # If the sentences are different
                if index_1 != index_2:
                    self.similarity_matrix[index_1][index_2] = self.sentence_similarity(self.sentences[index_1],
                                                                                        self.sentences[index_2])

    def create_sentence_similarity_table(self):
        self.create_similarity_matrix()
        sentence_similarity_graph = nx.from_numpy_array(self.similarity_matrix)
        scores = nx.pagerank(sentence_similarity_graph)
        for index, sentence in enumerate(self.sentences):
            self.sentence_similarity_table[sentence] = scores[index]

    def create_frequency_table(self):
        """
        Count the amount of times a word has been popping up in the entire article.
        The more times it pops up, the more "valuable" it is.
        However, we want to ignore very common words / stop words such as "a", "the", etc.
        :return: None
        """
        for word in self.words:
            if word not in self.stop_words:
                value = self.word_frequency_table.get(word, 0)
                self.word_frequency_table[word] = value + 1

    def set_sentence_value_table(self):
        """
        We will apply a value of a sentence based on the value of the words the sentence has.
        :return:
        """
        for sentence in self.sentences:
            # Go through every word in a sentence
            words_in_sentence = word_tokenize(sentence)
            for word in words_in_sentence:
                frequency = self.word_frequency_table.get(word)
                # If a given word is in the frequency table
                if frequency is not None:
                    # Update the value of the sentence
                    old_value = self.sentence_value_table.get(sentence, 0)
                    self.sentence_value_table[sentence] = old_value + frequency

    def find_average_sentence_value(self):
        return sum(self.sentence_value_table.values()) / len(self.sentence_value_table)

    def summarize(self, value: float) -> str:
        # TODO: Utilize the similarity heuristic that I have implemented
        # TODO: Create tests to ensure that the given code does work.
        self.create_frequency_table()
        self.set_sentence_value_table()
        average = self.find_average_sentence_value()
        summary = ""
        for sentence in self.sentences:
            sentence_value = self.sentence_value_table.get(sentence, 0)
            if sentence_value > average * value:
                summary += " " + sentence
        return summary
