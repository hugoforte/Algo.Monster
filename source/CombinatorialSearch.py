from ast import Str
from typing import List

#permutations
def permutations(letters: str) -> List[str]:
    def permutations(path: [], used: [], res: []):
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
    def dfs(path: [], letter_number_list: [], letter_number_mask: [[]], res: []):
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
    s = "aab"
    words = ["a", "c"]
    res = word_break(s, words)
    print(str(res) + ' :you can make the word:' + s + ' out of: ' + ','.join(words))

def word_break(s: str, words: List[str]) -> bool:
    return False
 

if __name__ == '__main__':
    #call_letter_combinations() => 
    call_word_break()