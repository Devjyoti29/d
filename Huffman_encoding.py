from collections import Counter
import heapq
class Tree:
    def __init__(self,ch,freq,left=None,right=None):
        self.ch=ch
        self.freq=freq
        self.left=left
        self.right=right
    def __lt__(self,other):
        return self.freq<other.freq

def build_tree(text):
    counter=Counter(text)
    pq=[Tree(ch,counter[ch]) for ch in counter.keys()]
    heapq.heapify(pq)
    while(len(pq)>1):
        left=heapq.heappop(pq)
        right=heapq.heappop(pq)
        parent=Tree(None,left.freq + right.freq,left,right)
        heapq.heappush(pq,parent)
    return pq[0]

def build_map(root):
    def dfs(root,code,encording_map):
        if root.ch:
            encording_map[root.ch]=''.join(code)
        else:
            code.append('0')
            dfs(root.left,code,encording_map)
            code.pop()
            code.append('1')
            dfs(root.right,code,encording_map)
            code.pop()
    encoding_map={}
    dfs(root,[],encoding_map)
    return encoding_map
def encode(text):
    root=build_tree(text)
    encoding_map=build_map(root)
    return ''.join([encoding_map[ch] for ch in text])
def decode(encoded,root):
    decoded=[]
    node=root
    for bit in encoded:
        if bit=='0':
            node=node.left
        else:
            node=node.right
        if node.ch:
            decoded.append(node.ch)
            node=root
    return ''.join(decoded)

print(encode("aaaaaba"))

root=build_tree("aaaaaba")
print(decode("1111101",root))