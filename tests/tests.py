import pytest

from summarizer_robot import SummarizerRobot


def pytest_configure_summarizer_robot():
    sample_article = "An apple is an edible fruit produced by an apple tree (Malus domestica). Apple trees are " \
                     "cultivated worldwide and are the most widely grown species in the genus Malus. The tree " \
                     "originated in Central Asia, where its wild ancestor, Malus sieversii, is still found today. " \
                     "Apples have been grown for thousands of years in Asia and Europe and were brought to North " \
                     "America by European colonists. Apples have religious and mythological significance in many " \
                     "cultures, including Norse, Greek, and European Christian tradition. "
    summarizer_robot = SummarizerRobot(sample_article)


# Summarizer Robot =====================================================================================================

class TestSummarizerRobot:
    def __init__(self):
        self.summarizer_robot = None

    def setup(self):
        sample_article = "An apple is an edible fruit produced by an apple tree (Malus domestica). Apple trees are " \
                         "cultivated worldwide and are the most widely grown species in the genus Malus. The tree " \
                         "originated in Central Asia, where its wild ancestor, Malus sieversii, is still found today. " \
                         "Apples have been grown for thousands of years in Asia and Europe and were brought to North " \
                         "America by European colonists. Apples have religious and mythological significance in many " \
                         "cultures, including Norse, Greek, and European Christian tradition. "
        self.summarizer_robot = SummarizerRobot(sample_article)

    # Regions of test for value of sentence
    @pytest.mark.order0
    def test_summarizer_robot_create_frequency_table(self):
        assert False

    @pytest.mark.order1
    def test_summarizer_robot_set_sentence_value_table(self):
        assert False

    @pytest.mark.order2
    def test_summarizer_robot_find_average_sentence_value(self):
        assert False

    # Regions of test that is sentence similarity
    @pytest.mark.order3
    def test_summarizer_robot_sentence_similarity(self):
        assert False

    @pytest.mark.order4
    def test_summarizer_robot_create_similarity_matrix(self):
        assert False

    @pytest.mark.order5
    def test_summarizer_robot_create_sentence_similarity_table(self):
        assert False

    @pytest.mark.order6
    def test_summarizer_robot_summarize(self):
        assert False


# Image Robot ==========================================================================================================


pytest_configure_summarizer_robot()
