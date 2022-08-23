import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
def pre_remove(a):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    stopwords=set(stopwords.words("english"))
    word_token=word_tokenize(a)
    filtered=[w for w in word_token if w not in stopwords]
    r=''
    for i in filtered:
        r=r+i+' '
    return(r)
    
def base_word(a):
    from nltk.stem import PorterStemmer
    from nltk.tokenize import sent_tokenize,word_tokenize
    ps = PorterStemmer()
    words=word_tokenize(a)
    filtered=[ps.stem(w) for w in words]
    r=''
    for i in filtered:
        r=r+i+' '
    return(r)
    
# base_word("Ravi is doing Homework")
# 'ravi is do homework '
def lemmatize(a):
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize
    words=word_tokenize(a)
    lemmatizer =WordNetLemmatizer()
    filtered=[lemmatizer.lemmatize(w) for w in words]
    return(filtered)
    
# lemmatize("feet cacti geese Ravi do")
# ['foot', 'cactus', 'goose', 'Ravi', 'do']
def NER(a):
    import nltk
    tokenized_words=nltk.word_tokenize(a)
    tagged=nltk.pos_tag(tokenized_words)
    chunked=nltk.ne_chunk(tagged)
    named=[]
    for w in chunked:
        if hasattr(w,"label"):
            named.append(" ".join(c[0] for c in w.leaves()))
    return(named)
 
def main(a):
    s=[]
    r=''
    for i in a:
        if i !=".":
            r=r+i
        else:
            s.append(r)
            r=""
    result=[]
    for i in s:
        result.append(lemmatize(base_word(pre_remove(i))))
    return(result)
        
# main("Ravi is a good boy.chandu is a bad boy.")
# [['ravi', 'good', 'boy'], ['chandu', 'bad', 'boy']]
def final(a,b):
    from nltk.corpus import wordnet
    from itertools import chain
    original=main(a)
    answer=main(b)
    t=[]
    for i in answer:
        r=[]
        for j in original:
            s=0
            for w in i:
                synonyms = wordnet.synsets(w)
                lemmas =[w for w in set(chain.from_iterable([word.lemma_names() for word in synonyms]))]
                if helper(w,j):
                    s=s+1
            r.append(s/len(j))
        t.append(max(r))
    m=0
    for i in NER(b):
        if i in NER(a):
            m=m+1
    f1=m/len(NER(a))*100
    f2=(sum(t)/len(t))*100
        
    return(f1*(0.90)+f2*(0.10))
                    
                    
            
# final("Ravi is doing a job in Google.","Ravi is working in Google.")
90.0
from nltk.corpus import wordnet
from itertools import chain
synonyms = wordnet.synsets("doing")
lemmas = [w for w in set(chain.from_iterable([word.lemma_names() for word in synonyms]))]
# lemmas

if [1,2,3,4] in [1,2]:
    print(8)
def helper(l1,l2):
    for i in l1:
        if i in l2:
            return(True)
    return(False)
helper([],[1,2,3])
False
a="NEW DELHI: Telecom and IT minister Ashwini Vaishnaw on Thursday visited the 5G test-bed at IIT Madras and successfully tested a 5G call on an indigenously-developed network. The test-bed had been inaugurated by Prime Minister Narendra Modi on Tuesday. “This is the first step towards making the solution feasible commercially. Over the next few months, Made-in-India solution has the potential of going from local to global. It also meets India’s needs indigenously and securely,” the minister said.At a time when concerns around cyber security are at their peak, India has been developing its local 5G network solution that it promises will be more efficient in cost as well as productivity.Vaishnaw has said that the government will be deploying the solution, once its ready for commercialisation, on the network of state-owned BSNL, and thereafter it will also be pitched to other private operators. “We are confident that a more efficient solution which is also cost-effective will appeal to companies not only in India, but even those who are abroad. We feel that the India-made 5G stack will have a huge export potential.” For BSNL, the 4G and 5G stack is being developed by a consortium that has C-Dot working on the core, while the Tata group comes in with TCS and Tejas. The government will deploy this solution for BSNL’s upgradation to 4G and thereafter to 5G." 
b="India has shown interest in Hyperloop tech since 2017, by then Railway Minister Suresh Prabhu. In fact, the ministry also held talks with US-based Hyperloop One, but nothing quite materialised.  IIT Madras’s  Avishkar Hyperloop which was formed in 2017 had been working on scalability and frugal engineering concepts for the development of a Hyperloop based transportation system for India. The group was one of the top ten finalists at the SpaceX Hyperloop Pod competition of 2019 and was the only Asian team to do so. They also were awarded the ‘Most Scalable Design Award’ at the European Hyperloop Week in 2021. "
final(a,b)

