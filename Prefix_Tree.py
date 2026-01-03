# Logic for Prefix tree
# Skeleton for each node in tree the word metadata will be store in the nodes python dictionary {} key values 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isCompleteWord = False
        
        
# Insert new word loop through string letters and create new nodes for word paths or reuse if already exist
      
def insert(root,key):
    node = root
    for ch in key:
        if ch not in node.children:
            node.children[ch] = TrieNode()
        node = node.children[ch]
        
    node.isCompleteWord = True
    

# Check for full word saving each key as string value in memory

def search(root,word):
    node = root
    accumulated_word =""
    for ch in word:
        if ch not in node.children:
            return False
        node = node.children[ch]
        accumulated_word += ch
        if node.isCompleteWord:
            return accumulated_word

# Loop to look through every character possibility for given prefix by checking every index to find associated words
# Extend results through loop to get list of words  
    
def get_words(node,prefix=""):
        results = []
        
        
        if node.isCompleteWord:
            
            results.append(prefix)
        for ch, child in node.children.items():
            results.extend(get_words(child,prefix +ch ))
        
        return results
        
# Get prefix from user input after checking if text input is complete word
# Return get_words results
    
def prefix(root,prefix):
    node = root
    
    for ch in prefix:
        if ch not in node.children:
            return False
        node = node.children[ch]
    words = get_words(node,prefix)
    return words


        
