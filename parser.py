import PyPDF2
import pandas as pd
import re

def extract_text_from_pdf(pdf_path,start_keyword):
    """
    Extract text from a PDF file.
    """
    text = ""
    start_flag = False
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            page_text = page.extract_text()
            if start_flag:
                text += page_text
            elif start_keyword in page_text:
                start_flag = True
    return text


def parse_pdf_to_dataframe(pdf_path, keyword):
    """
    Parse a PDF file and create a dataframe with lines containing the keyword
    along with the corresponding page numbers.
    """
    text = extract_text_from_pdf(pdf_path, "Содержание")
    lines = text.split('\n')

    relevant_lines = []
    current_page = 0
    pattern_page = r'\s*-\s*\d+\s*-\s*'
    pattern_lab = r'{}\s+(\d+)'
    for line in lines:
        match = re.search(pattern_page, line)
        if match:
            for i in line.split():
                if i.isnumeric():
                    current_page = int(i)
                    break
        match = re.search(r'{}\s+(\d+)'.format(keyword), line)
        if match:
            relevant_lines.append({'Laboratory Work': match.group(0), 'Page Number': current_page})

    df = pd.DataFrame(relevant_lines)
    return df


# Path to your PDF file
pdf_path = 'Metodic1.pdf'

# Keyword to search for
keyword = 'Лабораторная работа'

# Parse PDF and create dataframe
df = parse_pdf_to_dataframe(pdf_path, keyword)

# Display the dataframe
print(df)
