from PyPDF2 import PdfWriter, PdfReader
import getpass
import sys

pdf_writer = PdfWriter()
pdf = PdfReader("kenlandtan_html-5.pdf")


def main():
    for page in range(len(pdf.pages)):
        pdf_writer.add_page(pdf.pages[page])

    if sys.stdin.isatty():
        password = getpass.getpass('Getpass: ')
    else:
        print('Readline')
        password = sys.stdin.readline().rstrip()

    pdf_writer.encrypt(password)

    with open("protected.pdf", "wb") as file:
        pdf_writer.write(file)


if __name__ == '__main__':
    main()
