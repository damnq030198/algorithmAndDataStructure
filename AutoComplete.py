# class Trie:
#     def __init__(self,value = None,freq = 0):
#         self.value = value
#         self.freq = freq
#         self.children = dict()
    
#     class AutoCompleteSystem:
#         def __init__(self, sentences, times):
#             self.root, self.query = Trie(),""

#             for i,sent in enumerate(sentences):
#                 node = self.root
#                 for char in sent:
#                     if char not in node.children:
#                         node.children[char] =Trie(char)
#                     node = node.children[char]
#                 node.freq = times[i]
#         def DFS(self,node,string):
#             if node.freq > 0:
#                 self.res.append((-node.freq,string))
#             if len(node.children) == 0:
#                 return
#             for char in node.children:
#                 self.DFS(node.children[char],string+char)

#         def input(self,c):
#             node = self.root
#             #finish the input, save this query as a historical sentence 
#             if c == '#':
#                 for char in self.query:
#                     if char not in node.children:
#                         node.children[char] = Trie(char)
#                     node = node.children[char]
#                 node.freq +=1
#                 self.query = ""
#                 return
#             self.query,self.res, string = self.query+c,[],''
#             for char in self.query:
#                 if char not in node.children:
#                     return[]
#                 node = node.children[char]
#                 string +=char 
            
#             #DFS to get string results
#             self.DFS(node,string)
#             #sort tuple: freq decreasing, string increasing
#             self.res.sort()
#             return [x[1] for x in self.res[:3]]

#trie
class Node:
    def __init__(self):
        self.m_children_node = {}
        self.m_total_word_so_far = ""
        self.m_current_letter = ""
        self.m_word = ''
        self.m_curr_index = 0
    
    def add_word(self,word,word_so_far = '',curr_index =-1):
        self.m_word = word
        self.m_curr_index = curr_index
        if self.m_curr_index >=0:
            self.m_current_letter = self.m_word[self.m_curr_index]
            self.m_total_word_so_far = word_so_far + self.m_word[self.m_curr_index]
        if self.m_curr_index +1 < len(self.m_word):
            if self.m_word[self.m_curr_index+1] not in self.m_children_node:
                self.m_children_node[self.m_word[self.m_curr_index+1]] = Node()
                self.m_children_node[self.m_word[self.m_curr_index+1]].add_word(self.m_word,self.m_total_word_so_far,self.m_curr_index+1)
            else:
                self.m_children_node[self.m_word[self.m_curr_index+1]].add_word(self.m_word,self.m_total_word_so_far,self.m_curr_index+1)

    def auto_complete_word(self,str):
        if len(str)>0 and str[0] in self.m_children_node:
            self.m_children_node[str[0]].auto_complete_word(str[1:])
        if len(str) == 0:
            print("auto complete :")
            self.print_tree()
    
    def print_tree(self):
        if self:
            if len(self.m_children_node) == 0:
                print("word :", self.m_total_word_so_far)
            else:
                for i in self.m_children_node:
                    self.m_children_node[i].print_tree()

#client code
words = ["den","dear","do","disco","dam","mother","brother"]

root = Node()
for w in words:
    root.add_word(w)

root.print_tree()
print("de :")
root.auto_complete_word('de')
for i in range(5):
    mystr = input("enter the letter:")
    root.auto_complete_word(mystr)
