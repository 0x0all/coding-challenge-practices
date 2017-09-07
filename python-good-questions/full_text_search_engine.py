"""
Your program must have two publicly visible methods. The first can be called “add”. “Add” simply adds a given document to your index.  The “add” method takes two parameters, 1) the unique identifier for the document, and 2) a single string representing the entire body of the document.  If you wanted to add a single page of the textbook to your index, you would pass the page number as the first parameter and the contents of the page as the second parameter.

The second method can be called “search”.  “Search” simply allows the caller to search the index that has been built up by repeatedly calling the “add” method.  Search takes a single parameter, a string query.  The query is a space delimited set of the terms that you are searching for.  For simplicity’s sake, you should interpret the query as a boolean AND query.  Meaning that all of the terms in your query need to appear somewhere in each of the documents that are part of the result set.  As the return type for “search”, you need to return only a collection of the document ids that match your query.  You don’t need to return the actual document body.
"""
import colections.defaultdict

class Index(object):
    def __init__(self):
        self.dict = defaultdict(list)
        self.list_of_words = defaultdict(set)
       
    def add(self, id, str):
        """my name is daniel"""
        """1"""
       
        words = list(str.split().tolower())
        for word in words:
            if word not in self.dict:
                self.dict[word] = [id]
            else:
                self.dict[word].append(id)
        
         temp_list = [x for x in words]
         self.list_of_words[id] = set(temp_list)
                        
               
    def search(self, str):
        res = []
       
        words = list(str.split().tolower())
       
        for word in words:
            if word not in self.dict:
                return []
            else:
                pages = self.dict[word]
                if set(words) && self.list_of_words[p for p in pages]:
                    res += self.dict[word]
               
        return set(res)
          
if __name__ == '__main__':                    
    add(1, 'hello world')
    #dict {'hello': [1], 'world': [1]}
    #list_of_words {'1': ('hello', world)}
    add(2, 'hello cat')
    #dict {'hello': [1,2,3], 'world': [1], 'cat': [2,3], 'and': [3], 'dog': [3]}
    #list_of_words {'1': ('hello', 'world'), '2': ('hello', 'cat')}
    add(3, 'hello cat and dog')
    search('hello cat')