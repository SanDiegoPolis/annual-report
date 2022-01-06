import jieba
import wordcloud
import sys

# 读取停用词列表
def get_stopword_list(file):
    with open(file, 'r', encoding='utf-8') as f:
        stopword_list = [word.strip('\n') for word in f.readlines()]
    return stopword_list

# 分词 然后清除停用词语
def clean_stopword(str, stopword_list):
    result = ''
    word_list = jieba.lcut(str)   # 分词后返回一个列表  jieba.cut()   返回的是一个迭代器
    for w in word_list:
        if w not in stopword_list:
            result += w
    return ' '.join(jieba.lcut(result))
    
if __name__ == '__main__':
    stopword_file = './stopwords/cn_stopwords.txt'
    process_file = './list/list_msg.txt'
    stopword_list = get_stopword_list(stopword_file)    # 获得停用词列表
    stopword_list += get_stopword_list('./stopwords/cn_stopwords_addition.txt')
    stopword_list += get_stopword_list('./stopwords/cmd_stopwords.txt')
    with open(process_file, 'r', encoding='utf-8') as f:
        text = f.read()
        w = wordcloud.WordCloud(font_path = 'msyh.ttc', width = 1920, height = 1080, background_color = 'white')
        cleaned_stopword = clean_stopword(text, stopword_list)
        #print(cleaned_stopword)
        w.generate(cleaned_stopword)
        image = w.to_file('./wordcloud-annual.png')