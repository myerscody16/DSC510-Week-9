#Name: Cody Myers
#Assignment: DSC 510 Week 9
#Purpose: To parse a text file and count the number of times each word is used throughout the file then export the
#output to it's own text file

from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer


def process_file(word_dict, fileName):
    with open("{}.txt".format(fileName),'a') as f:
        f.write(word_dict)
    #file is automatically closed by using "with"


def pretty_print(word_dict):
    finalString = "Word          Count\n-------------------\n"
    for k,v in word_dict.items():
        #call function to format the string
        newString = format_string(k.decode("ascii"), v)
            #"{} : {}\n".format(k.decode("ascii"),v)
        finalString = finalString + newString
    return finalString


def format_string(aKey, aValue):
    #14 characters to the start of the word "Count" in the final output
    keyLength = len(aKey)
    difference = 14 - keyLength
    formattedString = aKey
    for i in range(0, difference + 1):
        formattedString = formattedString + " "
    finishedString = formattedString + str(aValue) + "\n"
    return finishedString


def text_preprocess(raw_text):
    #converts letters to lower case letters
    raw_text = raw_text.lower()

    #creates instance of the regular expression tokenizer from the ntlk library
    tokenizer = RegexpTokenizer(r"\w+")

    #creates a list where every element is only a word and eliminates any puctuation, new lines, or spaces.
    tokens = tokenizer.tokenize(raw_text)

    #creates an array of values for each word
    vectorizer = CountVectorizer()

    #converts array to values for the dictionary that we are about to create
    word_counts = vectorizer.fit_transform([" ".join(tokens)])

    #create the dictionary
    word_dict = {k.encode("ascii"):v for k,v in zip(vectorizer.get_feature_names(),word_counts.toarray()[0])}

    return word_dict


#main
with open("Gettysburg.txt", "r") as f:
    data = f.read()
    #file is automatically closed by using "with"

x = text_preprocess(data)

count = 0
for k in x.items():
    count += 1

clean_looking_dict = pretty_print(x)

print("What would you like to call the output file?")

fileName = input()

with open("{}.txt".format(fileName), 'w') as d:
    d.write("The length of the dictionary is : {}\n".format(count))

process_file(clean_looking_dict, fileName)








