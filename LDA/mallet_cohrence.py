import os
import wenzhang_Lemmatizer1
from gensim import corpora
from gensim.corpora import Dictionary
from gensim.models.wrappers import LdaMallet
from gensim.models.coherencemodel import CoherenceModel
from tqdm import tqdm
import matplotlib.pyplot as plt

def txt_to_numpy(filename):
    doc_topics=[]
    file = open(filename)
    lines = file.readlines()
    for line in lines:
        p_float= []
        p=line.split()
        p_str=p[2:]
        for i in range(len(p_str)):
            p_float.append(float(p_str[i]))
        doc_topics.append(p_float)
    print(filename)
    print(doc_topics)
    return doc_topics

def topic_model_coherence_generator(texts, start_topic_count, end_topic_count, step):
    models = []
    coherence_scores = []
    for topic_nums in tqdm(range(start_topic_count, end_topic_count+1, step)):
        dictionary_path = 'dictionary_mallet122_' + str(topic_nums) + '.dictionary'
        dictionary = corpora.Dictionary.load(dictionary_path)
        corpus = [dictionary.doc2bow(text) for text in texts]
        mallet_path = 'C:\\Users\\asus\\Desktop\\hypertension相关评价\\python生成结果\\LDA\\122文章\\mallet模型\\dictionary_mallet122_' + str(
            topic_nums) + '.model'
        mallet_lda_model = LdaMallet.load(mallet_path)
        cv_coherence_model_mallet_lda = CoherenceModel (model=mallet_lda_model, corpus=corpus , texts=texts,  dictionary=dictionary, coherence='c_v')
        coherence_score = cv_coherence_model_mallet_lda.get_coherence()
        coherence_scores.append(coherence_score)
    return coherence_scores

def draw_cv(coherence_scores,start_topic_count,end_topic_count,step):
    plt.style.use('fivethirtyeight')
    x_ax = range(start_topic_count, end_topic_count+1, step)
    y_ax = coherence_scores
    plt.figure(figsize=(12, 6))
    plt.plot(x_ax, y_ax, c='r')
    plt.axhline(y=0.535, c='k', linestyle='--', linewidth=2)
    plt.rcParams['figure.facecolor'] = 'white'
    xl = plt.xlabel('Number of Topics')
    yl = plt.ylabel('Coherence Score')
    plt.show()

if __name__=='__main__':
    #MALLET_PATH = os.path.join("D:\Mallet","mallet-2.0.8","bin","mallet.bat")
    texts=wenzhang_Lemmatizer1.texts2
    start_topic_count = 10
    end_topic_count = 20
    step = 1
    dictionary = corpora.Dictionary(texts)
    corpus_ = [dictionary.doc2bow(text) for text in texts]
    coherence_scores = topic_model_coherence_generator(texts=texts, start_topic_count=start_topic_count, end_topic_count=end_topic_count, step=step)
    print(coherence_scores)
    draw_cv(coherence_scores, start_topic_count, end_topic_count, step)
'''
    lda_mallet = LdaMallet( mallet_path=MALLET_PATH, corpus=corpus_, num_topics=3, id2word=dictionary)
    topic_words20 = lda_mallet.show_topics(num_topics=3, num_words=20)
    print(topic_words20)
    topic_words=lda_mallet.get_topics()
    print(topic_words)
    doc_topics=txt_to_numpy(lda_mallet.fdoctopics())
    cv_coherence_model_mallet_lda = CoherenceModel(model=lda_mallet,corpus=corpus_ ,texts=texts, dictionary=dictionary, coherence='c_v')
    coherence_score = cv_coherence_model_mallet_lda.get_coherence()
    print(coherence_score)
'''
