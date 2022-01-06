import os

# 读取停用词列表
def get_stopword_list(file):
    with open(file, 'r', encoding='utf-8') as f:
        stopword_list = [word.strip('\n') for word in f.readlines()]
    return stopword_list

# 写入停用词列表
def set_stopword_list(file, wordlist):
    with open(file, 'w', encoding='utf-8') as f:
        for word in wordlist:
            f.write(word + '\n')

if __name__ == '__main__':
    stopword_file = os.path.dirname(__file__) + '/cn_stopwords_addition.txt'
    stopword_list = get_stopword_list(stopword_file)
    stopword_list.sort()
    set_stopword_list(stopword_file, stopword_list)