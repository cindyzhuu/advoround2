# This program generates a haiku for a given text (article, poem, story), by parsing for keywords and generating a poem based on those keywords
# Use examples: Generating a haiku for the Advo's featured article, to give a "sneak peak"/creative summary

import re
from collections import Counter
import openai

# picks the top 3 most frequently-occuring words to pass as keywords for the haiku generator
def get_keywords(text, num_words=3):
    stop_words = {
        "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at",
        "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could",
        "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for",
        "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
        "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm",
        "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't",
        "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours",
        "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so",
        "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's",
        "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until",
        "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when",
        "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would",
        "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"
    }

    #remove all non-words from the text
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()

    #splits text into array of words
    words = cleaned_text.split()

    #keeps meaningful words (those not in the stop words)
    filtered_words = [word for word in words if word not in stop_words]

    #counts the number of occurrences of each word
    word_count = Counter(filtered_words)

    #picks the 3 most frequent words(or however many specified in num_words)
    top_keywords = [word for word, count in word_count.most_common(num_words)]
    
    return top_keywords

# calls openai API to generate haiku based on the keywords
def generate_haiku(prompt):
    openai.api_key = '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'  

    response = openai.Completion.create(
      engine="text-davinci-002",  # You can choose other engines too
      prompt=f"Write a haiku about {prompt}:",
      max_tokens=20
    )
    return response.choices[0].text.strip()

def main():
    article = input("Enter a prompt for the haiku: ")
    prompt = get_keywords(article)
    haiku = generate_haiku(prompt)
    print(haiku)

if __name__ == "__main__":
    main()# advoround2
