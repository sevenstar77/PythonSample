from nltk.tokenize import WordPunctTokenizer
from nltk import word_tokenize, LancasterStemmer
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from collections import Counter
import requests
import nltk

#nltk.download()
wn = nltk.corpus.wordnet
#synset = wn.synsets("viper")
synset = wn.synsets("snake")
#print(synset)
#print(synset[0])


#viper

#Black Mama
#hypernyms() 상위어  /// hyponyms() 하위어
#print(wn.synset("snake.n.01").hypernyms())
#print(wn.synset("snake.n.01").hyponyms())



#유사도 측정(0~1) 0 : 서로 관계 없다. 1 완전한 유의어
snake = wn.synset("snake.n.01")
viper = wn.synset("viper.n.01")
result1 = snake.path_similarity(viper)
#print(result1)


#lion = wn.synsets('lion')
#tiger = wn.synsets('tiger')

# print(lion)
# print(tiger)


result2 = wn.synset("lion.n.01").path_similarity(wn.synset("tiger.n.01"))
#print(result2)

lion = wn.synset("lion.n.01")
tiger = wn.synset("tiger.n.01")

result3 = [simxy.definition() for simxy in max((x.path_similarity(y), x, y)  for x in wn.synsets("tiger") for y in wn.synsets("lion"))[1:]]
#print(result3)


#normalization
"""
word_tokenize(text) : 단어 토큰나이져 // sent_tokenize(text) : 문장 토큰나이져 // regxp_tokenize(text, re) 정규 표현식 기반의 토큰나이져, re 파라미터는 단어를 표현하는 정규 표현식
"""
word_product = WordPunctTokenizer()
text = "shbtefbjl company !+_fcvh baseball"
text1 = "say hello wolrd"
result4 = word_product.tokenize(text)
#print(result4)

# import traceback
# try:
#     word_tokenize(text1)
# except:
#     print(traceback.format_exc())


content = requests.get('http://www.naver.com').content
#print(content)

#형태소 분석기 생성
ls = nltk.LancasterStemmer()
#soup 객체생성
soup = BeautifulSoup(content, "html.parser")

#token 화 nltk.word_tokenize error 발생
words = WordPunctTokenizer().tokenize(soup.text)
#words = nltk.word_tokenize(soup.text)

words = [w.lower() for w in words]

#불용어 제거
result5 = [ls.stem(w)for w in words if w not in stopwords.words("english") and w.isalnum()]
#print(result5)

counterworlds = Counter(words)
#print(counterworlds)


print(counterworlds.most_common(10))


