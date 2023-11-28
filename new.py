# new.py
from Codespaces.ku2latin import kurdish_to_latin_converter

# Kurdish text to be converted
kurdish_text = "ئێلۆن موسک ل باژارێ پرەتۆرا ژ دایک بوویە، و دەمەکێ کورت ل زانینگەها وێ خواندیە"

# Convert to Latin script
latin_text = kurdish_to_latin_converter(kurdish_text)

# Print the result
print(latin_text)
