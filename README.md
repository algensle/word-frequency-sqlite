# word-frequency-sqlite

Counts word frequencies in a text, stores them in a SQLite database and queries them with SQL. Tested on "Alice's Adventures in Wonderland" (Project Gutenberg).

## Observations
The header and footer of the Project Gutenberg text file distort the results about the word frequency and were therefore sliced from the analysed text.

As expected the most common words are function words followed by "said" and "alice" as the most frequent content words in the top ten of the example text.

The calculation of rank x frequency is roughly constant from rank 10 on, as predicted by Zipf's law, but not for the top ranks. For example rank 1: 1651, rank 10: 3980, rank 100: 4900

## Limitations
Contractions like "don't" get split with the regex implementation into fragments and not full words. The table of contents is still part of the analysed text.

## Usage 
```
python word_count.py

```
