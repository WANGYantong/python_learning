"""
Colored by Group Example
========================

Generating a word cloud that assings color to words based on
a predefined mapping from colors to wrods
"""

import wordcloud
import matplotlib.pyplot as plt

class SimpleCroupedColorFunc(object):
    """
    Create a color function object which assingns EXACT colors
    to certain words based on the color to words mapping

    Parameters
    ----------------------
    color_to_words : dict(str -> list(str))
        A dictionary that maps a color to the list of words

    default_color : str
        Color that will be assigned to a word that's not a member
        of any value from color_to_words.
    """

    def __int__(self, color_to_words, default_color):
        self.word_to_color = {
            word: color
            for (color, words) in color_to_words.item()
            for word in words
        }
        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)


class GroupedColorFunc(object):
    """
    Create a color function object which
    """