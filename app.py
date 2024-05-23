import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
text="""NIE was started in 1946 with diploma programs in Civil Engineering in a room under a thatched roof in Lakshmipuram under leadership of kushagra.[1] The first batch consisted of 86 students. Later, the classes were held in a shed in the nearby Sharada Vilas High School campus, in Mysore. S. Ramaswamy, D. V. Narasimha Rao and T. Ramarao ("Tunnel" Ramarao), the founders, established NIE by 1950 with its own class rooms and workshops on a 6-acre (24,000 m2) campus. NIE started AMIE courses in Civil Engineering for intermediate-passed students in 1948. The students were permitted to change over to the regular degree course leading to B.E. degree in Civil Engineering of the University of Mysore. Thus, NIE became the second engineering college in the state of Karnataka and the first in Mysore. The first batch of students in Civil Engineering graduated in 1953.

A Golden Jubilee Complex was completed in 1996 on a 6-acre (24,000 m2) plot opposite the main building in part of the golden jubilee celebrations. In 2004, the college received World Bank aid under the TEQIP project.[2] The funds obtained were used to strengthen the Centres of Excellence in the college and to set up new ones.

In 2007, NIE attained autonomy under Visvesvaraya Technological University.[3] In 2011, NIE received further World Bank aid under the TEQIP-II. These funds were used to augment the postgraduate programs.

In March 2019,[4] the government of Karnataka approved a private university status for NIE society through notification of The NIE University Act 2019,[5] and it is set to start NIE University. D.A. Prasanna was designated the founder chancellor.[4] """
stopwords=list(STOP_WORDS)
#print(stopword)

nlp=spacy.load('en_core_web_sm')
#storing all the text in doc
doc=nlp(text)
#print(doc)
tokens=[token.text for token in doc]
#print(tokens)
wordfreq={}
for word in doc:
    if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
        if word.text not in wordfreq.keys():
            wordfreq[word.text] =1
        else:
            wordfreq[word.text]+=1
#print(wordfreq)
maxfreq=max(wordfreq.values())
#print(maxfreq)

for word in wordfreq.keys():
    wordfreq[word]=wordfreq[word]/maxfreq
#print(wordfreq)
sent_tokens=[sent for sent in doc.sents]
#print(sent_tokens)

sent_scores ={}
for sent in sent_tokens:
    for word in sent:
        if word.text in wordfreq.keys():
            if sent not in sent_scores.keys():
                sent_scores[sent]=wordfreq[word.text]
            else:
                sent_scores[sent]+=wordfreq[word.text]
#print(sent_scores)
select_len=int(len(sent_tokens)*0.2)
#print(select_len)
summary =nlargest(select_len,sent_scores,key=sent_scores.get)

#print(summary)
finale_summary=[word.text for word in summary]
summary=' '.join(finale_summary)
print(summary)