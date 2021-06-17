import PyPDF2
import re

extracted_text = list()
pdfFileObj = open(
    'CIS_Microsoft_Windows_Server_2012_R2_Benchmark_v2.4.0.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


def write_to_file(lines):
    with open('extracted_text.txt', 'w+') as f:
        for line in lines:
            # remove multiple . (dot)
            line = re.sub('\n\.+', '', line)

            # remove (L*)
            line = re.sub('\((L\d*?)\)', '', line)

            # remove (Scored)
            line = re.sub('\((Scored)\)', '', line)

            # remove page number
            line = re.sub('\n\d{2,3}\n', '', line)

            # remove new lines \n
            line = re.sub('\s+\n', '\n', line)

            # remove Page
            line = re.sub('\n+Page', '', line)

            f.write(line)
        f.close()


def edit_file(file):
    with open(file, 'a') as f:
        for line in file:
            line = re.sub('^([^-]*?)\s*\s', ',', line)
            print('test')
            f.write(line)
    f.close()


for page in range(2, 33):
    raw_text = pdfReader.getPage(page).extractText()
    extracted_text.append(raw_text)

# write_to_file(extracted_text)
edit_file('extracted_text.txt')
