import re
from collections import Counter

with open("alice.txt", encoding="utf-8") as file:
    text = file.read()

start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK ALICE'S ADVENTURES IN WONDERLAND ***"
end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK ALICE'S ADVENTURES IN WONDERLAND ***"
a = len(start_marker)
print(text.find(start_marker),
text.find(end_marker), a)

#slice text from startmarker +length to end marker
text = text[881:145486]


#convert to lowercase
text = text.lower()

#convert to single words
words = re.findall(r'\b\w+\b', text)
#count the frequency of each word
word_count = Counter(words)
#show ten most frequent words and their rank, and rank multiplied by the count
for rank, (word, count) in enumerate(word_count.most_common(100), start=1):
    print(f"{rank}. {word}: {count} and rank*count: {rank * count}")

#import sqlite3 and store the word count in a database
import sqlite3

conn = sqlite3.connect("words.db")
#cursor is the object that allows us to execute SQL commands
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS words (word TEXT PRIMARY KEY, count INTEGER)")
#empties the table before inserting new data
cur.execute("DELETE FROM words")
#executes insert for many rows with ? as placeholder
cur.executemany("INSERT INTO words (word, count) VALUES (?, ?)", word_count.items())
#saves the changes to the database
conn.commit()
#fetches the ten most frequent words from the database
cur.execute("SELECT word, count FROM words ORDER BY count DESC LIMIT 10")
print(cur.fetchall())
#how many words appear unique in the text
cur.execute("SELECT COUNT(word) FROM words WHERE count = 1")
print(cur.fetchall())
#ten most frequent words with more than five characters
cur.execute("SELECT word, count FROM words WHERE LENGTH(word) > 5 ORDER BY count DESC LIMIT 10")
print(cur.fetchall())