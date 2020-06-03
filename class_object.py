class SearchEngineBase(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open("D:\\task_list\\面向对象抽象理解\\"+file_path, 'r') as fin:
            text = fin.read()
            #print('text', text)
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')

    def search(self, query):
        raise Exception('search not implemented.')

def main(search_engine):
    print('Input keywords:')
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)
"""
class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results

search_engine = SimpleEngine()
main(search_engine)
"""
"""
# Bag of Words 的搜索模型（词袋模型）
import re 

class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}
    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)
    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results
    
    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True
    @staticmethod
    def parse_text_to_words(text):
        #使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w]', ' ', text)
        #转为小写
        text = text.lower()
        #去除空白单词
        word_list = text.split(' ')
        #生成所有单词的列表
        word_list = filter(None, word_list)
        #返回单词的set
        return set(word_list)
search_engine = BOWEngine()
main(search_engine)
#由于词袋模型不考虑词汇间出现的顺序，无法实现单词按顺序出现，或者搜索的单词在文中离得近一些
#对象编程会把算法复杂性隔离开来，而保留接口和其他的代码不变。
"""
#Inverted Index 倒序索引
import re 
class BOWInvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        self.Inverted_index = {}
        
