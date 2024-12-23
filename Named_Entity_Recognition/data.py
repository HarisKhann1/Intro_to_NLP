from nltk.tree import Tree

# Input data (already in chunked form)
data = [
    Tree('S', [('\ufeffImage', 'NN'), ('copyright', 'NN'), Tree('ORGANIZATION', [('EPA', 'NNP'), ('Image', 'NNP')]), ('caption', 'NN'), ('Uber', 'NNP'), ('has', 'VBZ'), ('been', 'VBN'), ('criticised', 'VBN'), ('many', 'JJ'), ('times', 'NNS'), ('over', 'IN'), ('the', 'DT'), ('way', 'NN'), ('it', 'PRP'), ('runs', 'VBZ'), ('its', 'PRP$'), ('business', 'NN'), ('Ride-sharing', 'JJ'), ('firm', 'NN'), ('Uber', 'NNP'), ('is', 'VBZ'), ('facing', 'VBG'), ('a', 'DT'), ('criminal', 'JJ'), ('investigation', 'NN'), ('by', 'IN'), ('the', 'DT'), Tree('GPE', [('US', 'JJ')]), ('government', 'NN'), ('.', '.')]),
    Tree('S', [('The', 'DT'), ('scrutiny', 'NN'), ('has', 'VBZ'), ('started', 'VBN'), ('because', 'IN'), ('the', 'DT'), ('firm', 'NN'), ('is', 'VBZ'), ('accused', 'VBN'), ('of', 'IN'), ('using', 'VBG'), ('``', '``'), ('secret', 'JJ'), ("''", "''"), ('software', 'NN'), ('that', 'WDT'), ('let', 'VBD'), ('it', 'PRP'), ('operate', 'VB'), ('in', 'IN'), ('regions', 'NNS'), ('where', 'WRB'), ('it', 'PRP'), ('was', 'VBD'), ('banned', 'VBN'), ('or', 'CC'), ('restricted', 'VBN'), ('.', '.')]),
    Tree('S', [('The', 'DT'), ('software', 'NN'), (',', ','), ('called', 'VBN'), ('``', '``'), ('greyball', 'NN'), ("''", "''"), (',', ','), ('helped', 'VBD'), ('it', 'PRP'), ('identify', 'VB'), ('officials', 'NNS'), ('seeking', 'VBG'), ('to', 'TO'), ('stop', 'VB'), ('the', 'DT'), ('service', 'NN'), ('running', 'VBG'), ('.', '.')]),
    Tree('S', [('A', 'DT'), ('spokesman', 'NN'), ('for', 'IN'), Tree('PERSON', [('Uber', 'NNP')]), ('declined', 'VBD'), ('to', 'TO'), ('comment', 'VB'), ('on', 'IN'), ('the', 'DT'), ('investigation', 'NN'), (',', ','), ('reported', 'VBD'), ('the', 'DT'), Tree('ORGANIZATION', [('Reuters', 'NNPS')]), ('news', 'NN'), ('agency', 'NN'), ('.', '.')]),
    # more chunks here...
]

