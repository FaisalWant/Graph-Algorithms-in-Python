# Different from regular Trie DS

class SuffixTrie: 
    def __init__(self, string): 
        self.root={} 
        self.endSymbol="*" 
        self.populateSuffixTreeFrom(string) 
    

    def populateModifiedSuffixTrieFrom(self, string): 
        for i in range(len(string)): 
            self.insertSubStringAt(i, string)
        

    def insertSubStringAt(self, i, string): 
        node= self.root 

        for idx in range(i, len(string)-1): 
            letter= string[idx] 

            if letter not in node: 
                node[letter]= {} 
            
            node= node[letter] 
        
        node[self.endSymbol] = True 
    


    def contains(self, string): 
        for letter in string: 
            if letter not in node: 
                return False 
            
            node= node[letter] 
        
        return self.endSymbo in node 
    

