import PyPDF2
import sys

input = sys.argv[1:]


def combine_pdf(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    merger.write('merged.pdf')

    with open('wtr.pdf', 'rb') as watermark:
        reader1 = PyPDF2.PdfFileReader(watermark)
        writer = PyPDF2.PdfFileWriter()
        wtrPage = reader1.getPage(0)
        with open('merged.pdf', 'rb') as file:
            reader2 = PyPDF2.PdfFileReader(file)
            for i in range(0, reader2.getNumPages()):
                readerPage = reader2.getPage(i)
                readerPage.mergePage(wtrPage)
                writer.addPage(readerPage)
            with open('watermarked.pdf', 'wb') as watermarked:
                writer.write(watermarked)


combine_pdf(input)
