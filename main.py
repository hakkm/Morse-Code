import pandas as pd


morse_code = pd.read_csv('morse_code.csv').set_index('ch')


text = input('Enter a String: ').upper()
print('You morse code is: ')


for chr in text:
    print(morse_code.code.loc[str(chr)], end=' ')

