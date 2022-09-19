import os
from math import floor


def bionic_reader(text: str, bold_output_type: str) -> str:
    def bold_word(word, idx, bold_output_type) -> str:
        ansi_bold = "\033[1m"
        ansi_end = "\033[0m"
        markdown_bold = "**"
        html_bold = "<b>"
        html_bold_end = "</b>"
        if bold_output_type == "ansi":
            return f"{ansi_bold}{word[:idx]}{ansi_end}{word[idx:]}"
        elif bold_output_type == "markdown":
            return f"{markdown_bold}{word[:idx]}{markdown_bold}{word[idx:]}"
        elif bold_output_type == 'html':
            return f"{html_bold}{word[:idx]}{html_bold_end}{word[idx:]}"

    bolded_text = []
    for word in text.split():
        word_split_idx = floor(len(word) / 2)
        if len(word) == 3:
            word_split_idx = 2
        word = bold_word(word, word_split_idx, bold_output_type)
        bolded_text.append(word)
    text = " ".join(bolded_text)
    return text
