# -*- coding: utf-8 -*-
#https://www.machinelearningplus.com/python/python-regex-tutorial-examples/

#1. Extract the user id, domain name and suffix from the following email addresses.

import re
emails = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""
'''
desired_output = [('zuck26', 'facebook', 'com'),
 ('page33', 'google', 'com'),
 ('jeff42', 'amazon', 'com')]
'''

# Solution
pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
print(re.findall(pattern, emails, flags=re.IGNORECASE))

#2. Retrieve all the words starting with ‘b’ or ‘B’ from the following text.

text = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better.""" 

# Solution: 
import re
print(re.findall(r'\bB\w+', text, flags=re.IGNORECASE))
#> ['Betty', 'bought', 'bit', 'butter', 'But', 'butter', 'bitter', 'bought', 'better', 'butter', 'bitter', 'butter', 'better'] 

# '\b' mandates the left of 'B' is a word boundary, effectively requiring the word to start with 'B'. 
# Setting 'flags' arg to 're.IGNORECASE' makes the pattern case insensitive.


#3. Split the following irregular sentence into words

sentence = """A, very   very; irregular_sentence"""
desired_output = "A very very irregular sentence"
# Solution
import re
" ".join(re.split('[;,\s_]+', sentence))


#4. Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
'''
desired_output = 'Good advice What I would do differently if I was learning to code today'
'''

# Solution
import re
def clean_tweet(tweet):
    tweet = re.sub('http\S+\s*', '', tweet)  # remove URLs
    tweet = re.sub('RT|cc', '', tweet)  # remove RT and cc
    tweet = re.sub('#\S+', '', tweet)  # remove hashtags
    tweet = re.sub('@\S+', '', tweet)  # remove mentions
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)  # remove punctuations
    tweet = re.sub('\s+', ' ', tweet)  # remove extra whitespace
    return tweet

print(clean_tweet(tweet))

#https://raw.githubusercontent.com/selva86/datasets/master/sample.html

#5. Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html

import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
print(r.text)  # html text is contained here


re.findall('<.*?>(.*)< /.*?>', r.text)

'''
desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph! ', 'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']

# Solution:
# Note: remove the space after < and /.*> for the pattern to work
re.findall('<.*?>(.*)< /.*?>', r.text) 
'''
