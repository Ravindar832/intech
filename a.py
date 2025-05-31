# String Compression and Decompression

import re

def rle_compress(s: str) -> str:
    """Basic Run-Length Encoding"""
    if not s:
        return ""
    
    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(f"{s[i - 1]}{count}")
            count = 1

    compressed.append(f"{s[-1]}{count}")
    return ''.join(compressed)

def second_compress(rle: str) -> str:
    """Remove '1' from the encoded string to reduce size"""
    result = []
    i = 0
    while i < len(rle):
        char = rle[i]
        j = i + 1
        count = ""
        while j < len(rle) and rle[j].isdigit():
            count += rle[j]
            j += 1
        if count == "1" or count == "":
            result.append(char)
        else:
            result.append(f"{char}{count}")
        i = j
    return ''.join(result)

def decompress(s: str) -> str:
    """Decompress optimized RLE string"""
    pattern = re.compile(r"([a-zA-Z])(\d*)")
    result = []
    for match in pattern.findall(s):
        char, count = match
        count = int(count) if count else 1
        result.append(char * count)
    return ''.join(result)

def test_compression():
    """Test all compression and decompression cases"""
    test_strings = [
        "aabcccccaaa",     
        "aabbccaaa",      
             
        "abcd",            
                       
    ]

    for s in test_strings:
        print(f"Original: {s}")
        c1 = rle_compress(s)
        print(f"Compressed 1: {c1}")
        c2 = second_compress(c1)
        print(f"Compressed 2: {c2}")
        d = decompress(c2)
        print(f"Decompressed: {d}")
        assert d == s, "Decompression failed!"
        print("✔️ Test passed\n")


if __name__ == "__main__":
    test_compression()
