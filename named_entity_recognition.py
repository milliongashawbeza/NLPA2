import nltk
sentence = """At eight o'clock on Thursday morning
 Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
tagged[0:6]
entities = nltk.chunk.ne_chunk(tagged)
print(entities)
