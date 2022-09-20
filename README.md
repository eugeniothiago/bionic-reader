# Bionic Reader
A simple python implementation of the bionic reading script/algorithm.

### What does it do? 

It turns the first letters of a word into bold so you can focus better on reading.

Example: **Lo**rem **ip**sum **do**lor **si**t **am**et, **conse**ctetur **adipi**scing **el**it, **se**d **d**o **eiu**smod **tem**por **incid**idunt **u**t **lab**ore **e**t **dol**ore **ma**gna **ali**qua. **U**t **en**im **a**d **mi**nim **ven**iam, **qu**is **nos**trud **exerci**tation **ull**amco **lab**oris **ni**si **u**t **ali**quip **e**x **e**a **com**modo **conse**quat. **Du**is **au**te **ir**ure **do**lor **i**n **repreh**enderit **i**n **volu**ptate **ve**lit **es**se **cil**lum **dol**ore **e**u **fug**iat **nu**lla **pari**atur.

### Script parameters:
- `--text`: The string/text to be processed.
- `--output_type`: So you can select in what language/type you want to apply boldness. The script currently supports **html, RTF, markdown and ANSI** outputs.

The script **will process entire files in the future**. Currently working on that :D 

### How to run it

On the same level of the script, open a terminal of your preference and type `python bionic_reader.py --text="text" --output-type='ansi'(example)`.