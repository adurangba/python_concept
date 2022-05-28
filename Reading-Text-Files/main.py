# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    file_handle = open(filename, "r")
    content = file_handle.read()

    return content


def count_words():
    text = read_file_content("./story.txt")

    # Replace all the special characters in the file
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("?", "")

    words = text.split()
    # Variable to hold word occurence count
    word_count = {}

    for word in words:
        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1

    return word_count