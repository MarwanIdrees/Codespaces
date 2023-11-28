#Kurdish to Latin Converter

This Python script converts Kurdish text to Latin script using a simple and efficient algorithm. It is particularly useful for transliterating Kurdish content into a format that uses Latin characters, facilitating easier communication and representation in various contexts.

##Usage
To use the Kurdish to Latin converter, simply follow these steps:

Clone the Repository:
```
git clone https://github.com/MarwanIdrees/Codespaces.git
```

##Navigate to the Project Directory:
```
cd Codespaces
```
##Run the Converter:
```
python ku2latin.py
```
Replace `ku2latin.py` with the name of the file where your `Codespaces` function is defined.

##Enter Kurdish Text:
Input the Kurdish text you want to convert when prompted.

##View the Latin Script Output:
The script will output the corresponding Latin script for the entered Kurdish text.

###Example
```
from Codespaces import Codespaces

## Kurdish text to be converted
kurdish_text = "ئێلۆن موسک ل باژارێ پرەتۆرا ژ دایک بوویە، و دەمەکێ کورت ل زانینگەها وێ خواندیە."

## Convert to Latin script
latin_text = Codespaces(kurdish_text)

## Print the result
print(latin_text)

```

##Methodology
The converter utilizes a mapping of Kurdish characters to their Latin equivalents. The algorithm also handles the placement of the letter 'w' between consecutive vowels to ensure accurate transliteration.

##Contribution
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

##License
This project is licensed - see the LICENSE file for details.
