from PyPDF2 import PdfFileReader,PdfFileWriter
file_path='book.pdf'
pdf = PdfFileReader(file_path)
with open('my_output.txt','w') as f:
    for page_num in range(pdf.numPages):
        print('page: {}'.format(page_num))
        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText()
            print(''.center(100,'-'))
        except:
            f.write('Page {0}\n'.format(page_num+1))
            f.write(''.center(100,'-'))
            f.write(txt)
    f.close()