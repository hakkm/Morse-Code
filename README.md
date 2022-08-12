# Morse-Code
Morse Code encrypter
# Assess The Task:
**Inpute:** Hakim Khabir <br>
**Output:** .... .- -.- .. -- / -.- .... .- -... .. .-.

1. space = ' / '
2. space between characters

### Needs:
Data: what i can do:

|what |quality  | Difficulty| Time|
--- | --- | ---| ---|
| scrape morsedecoder.com Or morsecoder.org/  |*****|***| ****|
| scrape wikipedea|***|*****|
| fill csv file with what messed| *****| *| ***|

#### Conclusion:
I will choose the csv file

# Plan:
Use Pandas to read the csv file.

# Problems:
pandas.errors.ParserError: Error tokenizing data. C error: EOF inside string

This error occurred when reading the csv file, specifically with reading  " and ' 


Sol:

|instead of| i write|
| --- | --- |
| ' | " ' " |
| " | ' " ' |

