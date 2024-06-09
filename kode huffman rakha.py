import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Fungsi untuk membangun pohon Huffman
def build_huffman_tree(freq_dict):
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        internal_node = HuffmanNode(None, lo.freq + hi.freq)
        internal_node.left = lo
        internal_node.right = hi
        heapq.heappush(heap, internal_node)
    
    return heapq.heappop(heap)

def print_huffman_tree(node, prefix=""):
    if node:
        if node.char:
            print(f"Character: {node.char}, Frequency: {node.freq}, Code: {prefix}")
        print_huffman_tree(node.left, prefix + "0")
        print_huffman_tree(node.right, prefix + "1")

input_text = "Rakha Alcander"

# menghitung frekuensi karakter
char_freq = defaultdict(int)
for char in input_text:
    char_freq[char] += 1

huffman_tree = build_huffman_tree(char_freq)

print("Pohon Huffman:")
print_huffman_tree(huffman_tree)

# Fungsi untuk membangun pohon Huffman
def build_huffman_tree(freq_dict):
    heap = [[weight, [char, ""]] for char, weight in freq_dict.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

input_text = "Rakha Alcander"

# menghitung frekuensi karakter
char_freq = defaultdict(int)
for char in input_text:
    char_freq[char] += 1

# membangun pohon huffman
huffman_tree = build_huffman_tree(char_freq)

# membuat kamus karakter ke kode huffman
huffman_dict = {char: code for char, code in huffman_tree}

# dikonversikan ke kode huffman
encoded_text = ''.join(huffman_dict[char] for char in input_text)

print("Kode Huffman untuk kata:", input_text)
print("Kode Huffman:", encoded_text)
