# To replace these words, you can use regular expressions, or regex.
# Regex allows you to find patterns of characters in text.

import re
from random import choice
import requests


# Using re.sub you can change any character in the string.
# For instance, You can  stop the substitution after a set number of replacements.
# So to only replace the first match, you can do this:changing the e characters to i looks like this:




#import the file
url = "gutenberg.txt"
r = open(url,encoding= "utf8").read()
text = r


#create lists and replace normal words with zombiewords
def change_prose(text):
    plural_nouns = ["ladies", "gentlemen", "women", "men", "children", "boys", "girls"]

    singular_nouns = ["son", "daughter", "child", "wife", "woman", "mrs", "miss", "husband", "man", "mr", "sir", "lady"]

    speaking = ["said", "replied", "spoke", "shouted", "cried", "whispered"]

    zombie_sounds = ["groaned", "moaned", "growled", "screamed", "gurgled"]

    plural_nouns = plural_nouns + [word.title() for word in plural_nouns]

    singular_nouns = singular_nouns + [word.title() for word in singular_nouns]

    for word in plural_nouns:
        text = re.sub(r'\b{0}\b'.format(word), "zombies", text)

    for word in singular_nouns:
        text= re.sub(r'\b{0}\b'.format(word), "zombie", text)

    for word in speaking:
        text = re.sub(r'\b{0}\b'.format(word), choice(zombie_sounds), text)
    return(text)


#replace diffrent letters
def zombify_speech(text):
    text = re.sub(r'[eiosEIOS]', "r", text)
    text = re.sub(r'[^zhrgbmnaZHRGBMNA“”?\n.!?-]', '', text)
    text = re.sub(r'r\b', 'rh', text)
    text = re.sub(r'(\b[aA]\b)', 'hra', text)
    return(text)

speech = re.findall(r'“.*?”', text, flags=re.DOTALL)

for words in speech:
    text = text.replace(words,zombify_speech(words))

text = change_prose(text)

#create a new file calles "Zombie"
with open("Zombie.txt", "w", encoding="utf-8") as f:
    f.write(text)


