import os
from math import floor
import argparse
from typing import Any

parser = argparse.ArgumentParser()
parser.add_argument("--text", type=str, required=False)
parser.add_argument("--file", type=str, required=False)
parser.add_argument("--output-type", type=str, required=True)
args = parser.parse_args()


def bionic_reader(text: str, bold_output_type: str, file) -> str:
    def bold_word(word, idx, bold_output_type) -> str:
        ansi_bold = "\033[1m"
        ansi_end = "\033[0m"
        markdown_bold = "**"
        html_bold = "<b>"
        html_bold_end = "</b>"
        rtf_bold = "\b"
        rtf_bold_end = "\b0"
        if idx == 0:
            return word
        if bold_output_type == "ansi":
            return f"{ansi_bold}{word[:idx]}{ansi_end}{word[idx:]}"
        elif bold_output_type == "markdown":
            return f"{markdown_bold}{word[:idx]}{markdown_bold}{word[idx:]}"
        elif bold_output_type == "html":
            return f"{html_bold}{word[:idx]}{html_bold_end}{word[idx:]}"
        elif bold_output_type == "rtf":
            return f"{rtf_bold}{word[:idx]}{rtf_bold_end}{word[idx:]}"

    def word_len(word: str) -> int:
        word_split_idx = floor(len(word) / 2)
        if len(word) == 3:
            word_split_idx = 2
        return word_split_idx

    def input_handler(text: str, file_path: str) -> list:
        text_list = []
        if text:
            text_list.extend(text.split())
            return text_list
        if file_path:
            file_name, extension = os.path.splitext(file_path)
            try:
                if extension == ".txt":
                    with open(file_path) as file:
                        text_list.extend(file.readlines())
            except OSError as e:
                print(f"{e}")
            return text_list

    def process_words(words_list, bold_output_type) -> str:
        bolded_text = []
        for word in words_list:
            word_split_idx = word_len(word)
            word = bold_word(word, word_split_idx, bold_output_type)
            bolded_text.append(word)
        text = " ".join(bolded_text)
        return text

    def process_markdown(file_path: str, bold_output_type):
        with open(file_path) as file:
            file_name, extension = os.path.splitext(file_path)
            file_lines = file.readlines()
            line_words = []
            special_characters = ["`", "-", "--", "**", "#", "##", "###", "####"]

            for line in file_lines:
                line_words.append(line.split())

            file_lines.clear()
            line_words = (
                (
                    bold_word(word, word_len(word), bold_output_type)
                    if not word.startswith(tuple(special_characters))
                    else word
                    for word in line_word
                )
                for line_word in line_words
            )

            for string in line_words:
                file_lines.append(" ".join(string))

            with open(f"{file_name}_bold" + extension, "w") as edited_file:
                for line in file_lines:
                    edited_file.write(line + " \n")


if __name__ == "__main__":
    bionic_reader(text=args.text, bold_output_type=args.output_type, file=args.file)
