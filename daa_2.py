import heapq

# Creating Huffman tree node
class node:
    def __init__(self,freq,symbol,left=None,right=None):
        self.freq=freq # frequency of symbol
        self.symbol=symbol # symbol name (character)
        self.left=left # node left of current node
        self.right=right # node right of current node
        self.huff= '' # # tree direction (0/1)

    def __lt__(self,nxt): # Check if curr frequency less than next nodes freq
        return self.freq<nxt.freq

def printnodes(node,val=''):
    newval=val+str(node.huff)
    # if node is not an edge node then traverse inside it
    if node.left: 
        printnodes(node.left,newval)
    if node.right: 
        printnodes(node.right,newval)

    # if node is edge node then display its huffman code
    if not node.left and not node.right:
        print("{} -> {}".format(node.symbol,newval))

if __name__=="__main__":
    chars = ['a', 'b', 'c', 'd', 'e', 'f']
    freq = [ 5, 9, 12, 13, 16, 45]
    nodes=[]    

    for i in range(len(chars)): # converting characters and frequencies into huffman tree nodes
        heapq.heappush(nodes, node(freq[i],chars[i]))

    while len(nodes)>1:
        left=heapq.heappop(nodes)
        right=heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1
        # Combining the 2 smallest nodes to create new node as their parent
        newnode = node(left.freq + right.freq , left.symbol + right.symbol , left , right)
        # node(freq,symbol,left,right)
        heapq.heappush(nodes, newnode)

    printnodes(nodes[0]) # Passing root of Huffman Tree

# Explaination:

# 1. Importing the necessary library:
#    - The code starts by importing the `heapq` library, which is used for creating a priority 
#      queue to efficiently select the lowest frequency nodes during the Huffman tree construction.

# 2. Creating the `node` class:
#    - A `node` class is defined to represent nodes in the Huffman tree. Each node has attributes 
#      for frequency (`freq`), symbol (character), left child node (`left`), right child node (`right`), 
#      and a `huff` attribute to store the direction (0 or 1) in the tree.

# 3. The `__lt__` method:
#    - The `__lt__` method is defined within the `node` class to allow comparison of nodes based on their 
#      frequencies. This is necessary for heapq to order nodes by their frequencies.

# 4. `printnodes` function:
#    - The `printnodes` function is used to traverse the Huffman tree and print the Huffman codes for 
#      each character in the tree. It recursively traverses the tree, appending '0' or '1' to the `huff` 
#      attribute of nodes as it descends.

# 5. Main part of the code:
#    - In the `if __name__ == "__main__":` block, a list of characters (`chars`) and their corresponding
#      frequencies (`freq`) are defined. These represent the input data for Huffman encoding.

# 6. Creating initial nodes:
#    - Initially, each character and its frequency are converted into `node` objects and pushed onto a 
#      priority queue (`nodes`) using `heapq.heappush`.

# 7. Constructing the Huffman tree:
#    - The code enters a `while` loop that continues until there is only one node left in the priority 
#      queue. In each iteration of the loop, it pops the two nodes with the lowest frequencies (`left` and `right`) 
#      from the queue.
#    - It assigns `0` to `left.huff` and `1` to `right.huff` to mark their positions in the Huffman tree.
#    - It then combines these two nodes into a new node with the sum of their frequencies and their symbols as a 
#      concatenation. This new node is pushed back onto the priority queue.
#    - The loop continues until there's only one node left in the queue, which becomes the root of the Huffman tree.

# 8. Printing Huffman codes:
#    - Finally, the `printnodes` function is called with the root node of the Huffman tree to traverse 
#      and print the Huffman codes for each character.

# The code constructs the Huffman tree and prints the Huffman codes for the given character frequencies, 
#  which is the desired behavior for Huffman encoding using a greedy approach.

# Theory:
# Huffman coding is a variable-length prefix coding algorithm used for lossless data 
# compression. It was developed by David A. Huffman while he was a Ph.D. student at MIT in
# 1952. The primary goal of Huffman coding is to represent data in a way that minimizes the 
# overall length of the encoded message. It is widely used in various compression formats like
# ZIP, GZIP, and JPEG.

# Working:

# 1. Frequency Analysis: In the first step, the algorithm analyzes the input data 
# (usually a stream of characters or symbols) to determine the frequency of each 
# symbol. Symbols can be individual characters in a text document or any other 
# discrete units in the data.

# 2. Building the Huffman Tree: The algorithm constructs a binary tree called the 
# Huffman tree. In this tree, each leaf node represents a symbol, and each non-leaf 
# node has a frequency value that is the sum of its child nodes' frequencies. The goal 
# is to create a binary tree where frequently occurring symbols are closer to the root, 
# and less frequent symbols are farther from the root.

# 3. Assigning Binary Codes: The next step involves assigning binary codes to each symbol 
# based on their position in the Huffman tree. A symbol closer to the root will have a 
# shorter binary code, and a symbol farther from the root will have a longer binary code. 
# This property ensures that the codes are uniquely decodable.

# 4. Encoding: The input data is then encoded using the binary codes assigned to each symbol. 
# This encoding results in a compressed representation of the original data.

# 5. Decoding: To retrieve the original data, the encoded binary stream is decoded by traversing 
# the Huffman tree from the root to the leaf nodes, where the original symbols are reconstructed.

# Now, regarding the time and space complexity of the provided Huffman coding implementation:

# - Time Complexity:
#   - Constructing the initial nodes and building the Huffman tree takes O(n * log n) time, where 
#   'n' is the number of unique symbols (characters) in the input data.
#   - The construction of the Huffman tree involves repeated operations with a priority queue (heap) 
#   that has O(log n) complexity for each insertion or deletion, and these operations are performed 'n-1' times.

# - Space Complexity:
#   - The space complexity of this code is primarily determined by the priority queue used to store 
#   the nodes. It takes O(n) space for storing the initial nodes (one for each symbol).
#   - The space used by the priority queue and the constructed Huffman tree is also O(n) because, at 
#   most, you have 'n' nodes in the queue at any given time.
#   - The space complexity for the `printnodes` function's recursive call stack is determined by the 
#   height of the Huffman tree, which is O(log n) in the worst case.

# Overall, the provided code has a time complexity of O(n * log n) for building the Huffman tree and 
# a space complexity of O(n) for storing nodes and the constructed tree. The time complexity is 
# generally quite efficient for most practical purposes, and the space complexity is linear in the 
# number of unique symbols in the input data.