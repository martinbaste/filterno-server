# -*- coding: utf-8 -*-
# @Author: Adrian Zucco
# @Date:   2018-04-08 10:31:10
# @Last Modified by:   Adrian Zucco
# @Last Modified time: 2018-04-08 10:32:42

import nltk

REQUIRED_CORPORA = [
    'brown',  # Required for FastNPExtractor
    'punkt',  # Required for WordTokenizer
    'maxent_treebank_pos_tagger',  # Required for NLTKTagger
    'movie_reviews',  # Required for NaiveBayesAnalyzer
    'wordnet',  # Required for lemmatization and Wordnet
    'stopwords'
]

def main():
    for each in REQUIRED_CORPORA:
        print(('Downloading "{0}"'.format(each)))
        nltk.download(each, download_dir='./nltk_dependencies/')
    print("Finished.")

if __name__ == '__main__':
    main()