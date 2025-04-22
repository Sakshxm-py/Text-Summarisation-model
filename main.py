# Text Summarization Project in Python using Extractive Method

# Importing necessary libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary NLTK data files (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Asking for user input - multi-line text input
print("Please enter the text you want to summarize. Type 'DONE' to finish entering text.")
text = ""

while True:
    line = input()  # Taking input line by line
    if line.lower() == 'done':  # If the user types 'DONE', stop entering text
        break
    text += line + "\n"  # Add the inputted line to the text

# Step 1: Preprocessing the text
# Tokenizing the text into words
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

# Step 2: Creating a frequency table to store word frequencies
freqTable = dict()
for word in words:
    word = word.lower()  # Convert to lowercase for uniformity
    if word in stopWords:  # Ignore stopwords
        continue
    if word.isalpha():  # Ignore non-alphabetical characters (punctuation, numbers)
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

# Step 3: Scoring each sentence based on the frequency of words
sentences = sent_tokenize(text)
sentenceValue = dict()
for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():  # If the word exists in the sentence
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

# Step 4: Calculating the average sentence value
sumValues = sum(sentenceValue.values())  # Sum all sentence values
average = sumValues / len(sentenceValue)  # Calculate average sentence score

# Step 5: Storing sentences into the summary based on their value
summary = ''
for sentence in sentences:
    if sentence in sentenceValue and sentenceValue[sentence] > (1.2 * average):  # Select sentences that are more important
        summary += " " + sentence

# Output the generated summary
print("\nGenerated Summary:")
print(summary)
