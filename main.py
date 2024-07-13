import csv
import os
import deepl
import dotenv


AUTH_KEY = ""  # Replace with your key, or put it into .env
PRODUCTTON = False

target_columns = (0,)


def translate(text: str):
    if not PRODUCTTON:
        return text.upper()
    if AUTH_KEY == "":
        AUTH_KEY = os.getenv("AUTH_KEY")
    translator = deepl.Translator(AUTH_KEY)
    result = translator.translate_text(text, target_lang="PL")
    return result

def put(text: str, lst: list, index: int):
    outlist = []
    for i in range(index):
        if i <= len(lst-1):
            outlist[i] = lst[i]
        if i == index:
            outlist[i] = text
    lst.append(text)
    
    return text.upper()


def parse_file(input_path: str, output_path: str):
    input_file = open(input_path)
    output_file = open(output_path, 'w')
    csv_reader = csv.reader(input_file, delimiter=',')
    csv_writer = csv.writer(output_file, delimiter=',')

    for row in csv_reader:
        for i, column in enumerate(row):
            if i not in target_columns:
                continue
            translated = translate(column)
            row.append(translated)
        csv_writer.writerow(row)

    input_file.close()
    output_file.close()


def parse_directory(path: str):
    """Parse all files from a directory"""
    for file in os.listdir(path):
        if not file.endswith(".csv"):
            continue
        input_path = os.path.abspath(os.path.join(path, file))
        out_dir = os.path.abspath(os.path.join(path, "..", "output"))
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
        output_path = os.path.abspath(os.path.join(out_dir, file))
        parse_file(input_path, output_path)


if __name__ == '__main__':
    dotenv.load_dotenv()
    
    parse_directory("input")
