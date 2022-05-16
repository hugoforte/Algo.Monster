from typing import List

#permutations
def permutations(letters: str) -> List[str]:
    def permutations(path, used, res):
        if len(path) == len(letters):
            #res.append(path)
            res.append(''.join(path))
            return

        for i, letter in enumerate(letters):
            #skip is char is used
            if not used[i]:
                used[i] = True
                path.append(letters[i])
                permutations(path, used, res)
                path.pop()
                used[i] = False
                s
    res = []
    permutations([], [False] * len(letters), res)
    return res

#letter_combinations_of_phone_number
def call_letter_combinations():
    res = letter_combinations_of_phone_number("23")
    for line in res:
        print(line)
def letter_combinations_of_phone_number(digits: str) -> List[str]:
    #https://excalidraw.com/#json=AUU3-l0FvZ5QSt7Myo9tx,_NBuX9cqSLLBA6gmJcMLfw
    #https://algo.monster/problems/letter_combinations_of_phone_number
    #This one is wrong - it creates all permutations, when we actually just need them in sequence, a much easier problem
    KEYBOARD = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    def dfs(path, letter_number_lis, letter_number_mask, res):
        if len(path) == len(letter_number_list):
            res.append(''.join(path))

        #for all the letter_numbers
        for i, letter_numbers in enumerate(letter_number_list):
            for j, letter in enumerate(letter_numbers):
                if letter_number_mask[i][j]:
                    continue

                path.append(letter)
                #mask specific letter from being used again
                letter_number_mask[i][j] = True
                #also mask entire container from being used
                letter_number_mask[i] = [True] * len(letter_number_mask[i])
                dfs(path, letter_number_list, letter_number_mask, res)
                path.pop()
                letter_number_mask[i][j] = False
                letter_number_mask[i] = [False] * len(letter_number_mask[i])

    res = []
    letter_list = []
    mask = [None] * len(digits)
    for i, number in enumerate(digits):
        letter_list.append(KEYBOARD[number])
        mask[i] = [False] * len(KEYBOARD[number])
    
    dfs([], letter_list, mask, res)
    return res

#word_break
def call_word_break():
    s = "algomonster"
    words = ["algo", "monster"]
    res = word_break(s, words)
    print(str(res) + ' :you can make the word:' + s + ' out of: ' + ','.join(words))
def word_break(s: str, words: List[str]) -> bool:
#https://excalidraw.com/#json=TD6kzfvj6K_7L_HfO28AL,JuXVrMCUKSJPX3sRbioqnw
#https://algo.monster/problems/word_break

    _cache = {}
    def break_dfs(index: int) -> bool:
        if(index in _cache):
           return _cache[index]

        if index == len(s):
            return True

        retVal = False
        for word in words:
            #loop through word to see if we have a match so far
            for i, character in enumerate(word):
                #TODO, use startswith here instead of looping through the characters
                if s[index + i] != word[i]:
                    break;
                #we have not found a missmatch, continue
                if break_dfs(index + i + 1):
                    retVal = True

        _cache[index] = retVal
        return retVal

    return break_dfs(0)

#decode_ways
def call_decode_ways():
#https://excalidraw.com/#json=GE-TjSUNfts2Gkgl8LSj6,7ER1PU77yWmzr4EgJy9Iog
#https://algo.monster/problems/decode_ways
    res = decode_ways('123')
    print(res)
def decode_ways(digits: str) -> int:
    encodings = [str(i) for i in range(1, 27)]
    cache = {}
    def decode_dfs(index: int):
        decodings_found = 0
        if len(digits) == index:
            cache[index] = 1
            return 1;

        if index in cache:
            decodings_found += cache[index]

        for encoding in encodings:
            if digits[index:].startswith(encoding):
                decodings_found += decode_dfs(index + len(encoding))

        cache[index] = 0
        return decodings_found

    return decode_dfs(0)

#partition
def call_partition():
#https://excalidraw.com/#json=73pG-TEh85YV-MB1u_kV0,ipsJu2-zbTf1yhkvSBsQNw
#https://algo.monster/problems/palindrome_partitioning
    res = partition("19191")
    #print(len(res))
    for line in res:
        print(line)
        

def partition(s: str) -> List[List[str]]:
    partitions = []

    def is_palindrome(s:str)->bool:
        return s == s[::-1]

    def partition_string(partitions_so_far: List[str], s: str):
        #if we have reached the bottom, add the partition to the solutions
        if len(s) == 0:
            partitions.append(partitions_so_far.copy())
            return
        #loop through s to find palindromes
        for i, char in enumerate(s):
            potential_palindrome = s[0:i+1]
            if is_palindrome(potential_palindrome):
                partitions_so_far.append(potential_palindrome)
                partition_string(partitions_so_far, s[i+1:])
                partitions_so_far.pop()

    partition_string([], s)
    return partitions

if __name__ == '__main__':
    #call_letter_combinations() => 
    #call_word_break()
    #call_decode_ways()
    call_partition()