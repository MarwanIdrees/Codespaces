# by Marwan Nheli
def kurdish_to_latin_converter(text):
    # Kurdish characters acourding to its latin words
    words = {
        "ئ": "", "ا": "a", "ب": "b", "پ": "p", "ت": "t", "ج": "j", "چ": "ch",
        "ح": "h", "خ": "kh", "د": "d", "ر": "r", "ڕ": "r", "ز": "z", "ژ": "zh",
        "س": "s", "ش": "sh", "ع": "a", "غ": "gh", "ف": "f", "ڤ": "v", "ق": "q",
        "ک": "k", "گ": "g", "ل": "l", "ڵ": "l", "م": "m", "ن": "n", "ھ": "h","ه": "h",
        "و": "w", "ۆ": "o", "ە": "e", "ی": "i", "ێ": "e"
    }

    converted_text = "" #initialize 
    vowels = "aeiou"

    for i, char in enumerate(text):
        converted_char = words.get(char, char)

        if i > 0 and char in vowels and text[i - 1] in vowels and converted_char != 'w':
            converted_text += "w" + converted_char
        else:
            converted_text += converted_char

    return converted_text.capitalize()

# Converting Text
kurdish_text = "" #initialize  
latin_text = kurdish_to_latin_converter(kurdish_text)

