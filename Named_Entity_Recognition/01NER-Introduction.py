import nltk
"""
This script performs Named Entity Recognition (NER) on a given sentence using the Natural Language Toolkit (nltk).
It tokenizes the sentence, tags each token with its part of speech (POS), and then identifies named entities.
Steps:
1. Tokenize the input sentence into words.
2. Tag each token with its corresponding part of speech.
3. Print the tokenized sentence and the POS-tagged sentence.
4. Print the first three POS-tagged tokens with explanations.
5. Perform named entity recognition on the POS-tagged sentence and print the result.
Dependencies:
- nltk: Natural Language Toolkit library for working with human language data.
Example:
Input: 'In New York, I like to ride the Metro to visit MOMA and some restaurants rated well by Ruth Reichl.'
Output:
- Tokenized sentence: ['In', 'New', 'York', ',', 'I', 'like', 'to', 'ride', 'the', 'Metro', 'to', 'visit', 'MOMA', 'and', 'some', 'restaurants', 'rated', 'well', 'by', 'Ruth', 'Reichl', '.']
- POS-tagged sentence: [('In', 'IN'), ('New', 'NNP'), ('York', 'NNP'), (',', ','), ('I', 'PRP'), ('like', 'VBP'), ('to', 'TO'), ('ride', 'VB'), ('the', 'DT'), ('Metro', 'NNP'), ('to', 'TO'), ('visit', 'VB'), ('MOMA', 'NNP'), ('and', 'CC'), ('some', 'DT'), ('restaurants', 'NNS'), ('rated', 'VBN'), ('well', 'RB'), ('by', 'IN'), ('Ruth', 'NNP'), ('Reichl', 'NNP'), ('.', '.')]
- Named entities: (S (GPE In/IN New/NNP York/NNP) ,/, I/PRP like/VBP to/TO ride/VB the/DT Metro/NNP to/TO visit/VB MOMA/NNP and/CC some/DT restaurants/NNS rated/VBN well/RB by/IN (PERSON Ruth/NNP Reichl/NNP) ./.)
"""

sentence = '''In New York, I like to ride the Metro to
visit MOMA and some restaurants rated
well by Ruth Reichl.'''

tokenized_sent = nltk.word_tokenize(sentence)
print("\n",tokenized_sent)

tagged_sent = nltk.pos_tag(tokenized_sent)
print("\n",tagged_sent)
print("\n",tagged_sent)
'''
- [('In', 'IN'), ('New', 'NNP'), ('York', 'NNP')] output.
- 'IN': "In" is a preposition, indicating a relationship (e.g., location, time).
- 'NNP': "New" is a proper noun (singular), part of a specific name (e.g., "New York").
- 'NNP': "York" is also a proper noun (singular), completing the proper noun "New York."
- The output represents the syntactic structure of the phrase "In New York".
'''
print("\n",nltk.ne_chunk(tagged_sent))