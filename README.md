# German Lexical Analysis Tool

## Project Overview
This project provides a specialized Python framework for the lexical analysis of German literary texts. The primary objective is to assist language learners in overcoming reading barriers by identifying and studying the most frequent vocabulary within a specific text before beginning the reading process.

## Methodology
The tool processes raw text files through a pipeline designed for the linguistic complexities of the German language:

1. **Text Normalization**: The script ingests German text and prepares it for processing.
2. **Lemmatization**: Utilizing the spaCy 'de_core_news_sm' model, the script identifies the lemma (canonical form) of each word. This is essential for German, as it consolidates inflected verbs, declined nouns, and adjectives into a single dictionary entry.
3. **Lexical Filtering**: To ensure the output is educationally relevant, the script filters out punctuation, numerical values, and high-frequency stop words (such as articles and prepositions).
4. **Frequency Distribution**: The remaining tokens are aggregated to calculate their frequency of occurrence, sorted in descending order.

## Educational Application
By analyzing the vocabulary of a book prior to reading, a student can:
- Identify and memorize the core vocabulary used by a specific author.
- Reduce cognitive load during the actual reading process.
- Create targeted frequency-based dictionaries tailored to individual literary works.

## MY POV
This project is first of all a little help for me and my desire to learn German.
