import heapq
from collections import Counter


def huffman_encoding(text):
    heap = [[wt, [ch, ""]] for ch, wt in Counter(text).items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo, hi = heapq.heappop(heap), heapq.heappop(heap)
        for pair in lo[1:] + hi[1:]:
            pair[1] = "0" + pair[1] if pair in lo[1:] else "1" + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return "".join(dict(heap[0][1:]).get(ch, "") for ch in text), dict(heap[0][1:])


# Example usage
text = "hello huffman"
encoded_text, codes = huffman_encoding(text)
print("Encoded Text:", encoded_text)
print("Huffman Codes:", codes)
