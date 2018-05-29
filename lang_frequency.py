import os
import collections
import sys


def load_text(file_path):
    with open(file_path) as my_file:
        return my_file.read()


def get_most_frequency_words(text):
    word_list = text.split(" ")
    my_word_list = []
    for word in word_list:
        if word.isalpha():
            my_word_list.append(word)
    wordcount = collections.Counter(my_word_list)
    number_words = 10
    return wordcount.most_common(number_words)


def output_most_frequency_words(most_frequency_words):
    for word, number in most_frequency_words:
        print(' ', word, ' - repeates', '  ', number, 'times')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('You do not input any file_path')
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        exit('There is not any file like it')

    text = load_text(file_path)
    most_frequency_words = get_most_frequency_words(text)
    output_most_frequency_words(most_frequency_words)
    