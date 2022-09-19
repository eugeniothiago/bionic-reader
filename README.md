# Bionic Reader
A simple python implementation of the bionic reading script/algorithm.

### What does it do? 

It turns the first letters of a word into bold so you can focus better on reading.

Example: **Atte**ntion **wh**en **read**ing **i**s **impo**rtant

### Script parameters:
- `--text`: The string/text to be processed.
- `--output_type`: So you can select in what language/type you want to apply boldness. The script currently supports **html, markdown and ANSI** outputs.

The script **will process entire files in the future**. Currently working on that :D 

### How to run it

On the same level of the script, open a terminal of your preference and type `python bionic_reader.py --text="text" --output-type='ansi'(example)`.