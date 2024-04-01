import re

def extract_lab_work(string):
    lab_number = "2"  # Example string variable
    pattern = re.escape(lab_number) + r'\s'
    match = re.search(pattern, string)
    if match:
        return match.group(0)
    else:
        return None

# Example usage:
test_strings = [
    "Лабораторная работа 1: Introduction",
    "Some text before Лабораторная работа 2, then some text after",
    "No lab work mentioned in this string"
]

for test_string in test_strings:
    result = extract_lab_work(test_string)
    if result:
        print("Extracted:", result)
    else:
        print("No lab work found in:", test_string)
