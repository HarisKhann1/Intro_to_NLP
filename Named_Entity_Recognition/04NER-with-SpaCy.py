import spacy;
"""
This script demonstrates how to perform Named Entity Recognition (NER) using the SpaCy library.
Modules:
    spacy: A library for advanced Natural Language Processing in Python.
Functions:
    nlp: Loads the SpaCy model 'en_core_web_sm' for processing English text.
Usage:
    Run this script to load the SpaCy model and prepare it for Named Entity Recognition tasks.
"""

article = """
    Apple Inc. is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, and online services. It is considered one of the Big Tech technology companies, alongside Amazon, Google, Microsoft, and Facebook.
    Apple's hardware products include the iPhone smartphone, the iPad tablet computer, the Mac personal computer, the iPod portable media player, the Apple Watch smartwatch, the Apple TV digital media player, the AirPods wireless earbuds, the AirPods Max headphones, and the HomePod smart speaker line. Apple's software includes the macOS, iOS, iPadOS, watchOS, and tvOS operating systems, the iTunes media player, the Safari web browser, the Shazam music identifier, and the iLife and iWork creativity and productivity suites, as well as professional applications like Final Cut Pro, Logic Pro, and Xcode. Its online services include the iTunes Store, the iOS App Store, Mac App Store, Apple Music, Apple TV+, Apple Arcade, Apple Fitness+, iMessage, and iCloud.
    """

nlp = spacy.load('en_core_web_sm', disable=['parser', 'tagger', 'matcher'])

doc = nlp(article)

print("Entities in the article:")
for ent in doc.ents:
    print(ent.text, ent.label_)

# doc = nlp("Apple is looking at buying U.K. startup for $1 billion");

# print("Entities in the text:")
# print(doc.ents)
# print(doc.ents[0], doc.ents[0].label_)

# print()
# for token in doc:
#     print(token.text, token.pos_)

