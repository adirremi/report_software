import re
import unicodedata



def remove_non_letters_from_end(input_string):
    # Use regular expression to remove non-letter characters from the end of the string
    result = re.sub(r'[^a-zA-Z]+$', '', input_string)
    return result

def normalize_string(input_str):
    # Remove leading and trailing whitespace
    input_str = input_str.strip()

    # Convert to lowercase
    input_str = input_str.lower()

    # Normalize Unicode characters to a common form (NFC)
    input_str = unicodedata.normalize('NFC', input_str)

    return input_str
def clean_location(location):
    # Remove leading and trailing spaces
    location = location.strip()

    # Remove common city names if they are at the end of the string
    common_city_names = ['new york', 'queens', 'the bronx', 'brooklyn','staten island']
    for city in common_city_names:
        if location.endswith(city):
            location = location[:-len(city)].strip()

    return location.lower()


