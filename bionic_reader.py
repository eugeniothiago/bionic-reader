import os
from math import floor


def bionic_reader(text:str):
    
    def bold_word(word, idx):
        bold = '\033[1m'
        end = '\033[0m'
        return f"{bold}{word[:idx]}{end}{word[idx:]}"
    bolded_text = []
    for word in text.split():
        word_split_idx = floor(len(word)/2)
        if len(word) ==3:
            word_split_idx=2
        word = bold_word(word,word_split_idx)
        bolded_text.append(word)
    text = " ".join(bolded_text)
    return text