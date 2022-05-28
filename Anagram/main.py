# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True
word1 = input("Enter the first word \n")
word2 = input("Enter the second word \n")


# Converting the input to a list
def wordToList(word):
    array = []
    for i in word:
        if(i != " "):
            array.append(i.lower())

    sortedArray = sorted(array)

    return sortedArray


# Length checker for the list
def listLength(array):
    return len(array)


def wordCompare(arr1, arr2):
    anagramResult = arr1 == arr2

    if anagramResult:
        return True
    else:
        return False


def find_anagrams(word1, word2):
    word1Array = wordToList(word1)
    word2Array = wordToList(word2)

    # Confirming that the user inserted values
    if (listLength(word1Array) > 0) & (listLength(word2Array) > 0):
        result = f"Anagram Result: {wordCompare(word1Array, word2Array)}"
        print(result)

        return result

    else:
        print("All fields are mandatory")
        return False


find_anagrams(word1, word2)