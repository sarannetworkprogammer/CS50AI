import nltk
import sys
import os
import string
import math

from nltk.corpus import stopwords

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """

    dict1 ={}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):

                path1 = os.path.join(os.getcwd(), directory)
                path = os.path.join(path1,file)
                
                
                with open(path, encoding="utf-8") as in_file:
                    data = in_file.read()
                

                    dict1[file] = data

    return dict1


    

def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """

    words = []
    stop_words = set(nltk.corpus.stopwords.words('english'))
    words1 = nltk.tokenize.word_tokenize(document.lower())

    for word in words1:
        if word not in stop_words and word not in string.punctuation:
            words.append(word)

    return words
    



def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """

    dict2 = {}

    doc_len = len(documents)

    uniquewords = set()

    for k, v in documents.items():
        for word in v:
            uniquewords.add(word)

    
    for each in uniquewords:
        count = 0
        for doc in documents.values():
            if each in doc:
                count = count + 1

        dict2[each] = math.log(doc_len/count)

    
    return dict2

   



def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    file_scores = dict()

    for file, words in files.items():
        total_tf_idf = 0
        for word in query:
            total_tf_idf += words.count(word) * idfs[word]
        file_scores[file] = total_tf_idf

    ranked_files = sorted(file_scores.items(), key=lambda x: x[1], reverse=True)
    ranked_files = [x[0] for x in ranked_files]

    return ranked_files[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    sentence_scores = list()

    for sentence in sentences:
        sentence_values = [sentence, 0, 0]

        for word in query:
            if word in sentences[sentence]:
                # Compute “matching word measure”
                sentence_values[1] += idfs[word]
                # Compute "query term density"
                sentence_values[2] += sentences[sentence].count(word) / len(sentences[sentence])

        sentence_scores.append(sentence_values)
        
    return [sentence for sentence, mwm, qtd in sorted(sentence_scores, key=lambda item: (item[1], item[2]), reverse=True)][:n]


if __name__ == "__main__":
    main()
