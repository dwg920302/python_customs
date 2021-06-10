from numpy import dot
from numpy.linalg import norm


def cos_sim(v1, v2):
    return dot(v1, v2)/(norm(v1)*norm(v2))


doc1 = "My name is A"
doc2 = "My Rank is A"
doc3 = "My name is B"
doc4 = "My name is A Rank is B"
doc5 = "My name is not A"

doc = [doc1, doc2, doc3, doc4, doc5]

doc_keywords = set()

doc_keywords.update(doc1.split(' '))
doc_keywords.update(doc2.split(' '))
doc_keywords.update(doc3.split(' '))
doc_keywords.update(doc4.split(' '))
doc_keywords.update(doc5.split(' '))

# keyword 하나가 추가될 때 새로운 keyword를 DB에 등록하고, 그 값을 AUTO_INCREMENT로 지정?

dic_keywords = {}  # DB 대용임

i = 0
for data in list(doc_keywords):
    dic_keywords[i] = data
    i += 1

print(dic_keywords)

# print(cos_sim(doc1, doc2))


