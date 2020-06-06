from gensim import corpora
import matplotlib.pyplot as plt
import Perplexity
import gensim_test1


def graph_draw(topic, perplexity):  # 做主题数与困惑度的折线图
    x = topic
    y = perplexity
    plt.plot(x, y, color="red", linewidth=2)
    plt.xlabel("Number of Topic")
    plt.ylabel("Perplexity")
    plt.show()


if __name__ == '__main__':
    a = range(1, 20, 1)  # 主题个数
    p = []
    for num_topics in a:
        lda=gensim_test1.lda
        dictionary=gensim_test1.dictionary
        corpus = corpora.MmCorpus('corpus.mm')
        print(corpus)
        testset = []
        print(corpus.num_docs)
        for c in range(corpus.num_docs):  # 如何抽取训练集？
            testset.append(corpus[c])
        prep = Perplexity.perplexity(lda, testset, dictionary, len(dictionary.keys()), num_topics)
        p.append(prep)

    graph_draw(a, p)

