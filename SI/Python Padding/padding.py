from PyPDF2 import PdfFileReader,PdfFileWriter
def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        number_of_pages = pdf.getNumPages()
        output = PdfFileWriter()
       
        for i in range(0,number_of_pages):    
            page=pdf.getPage(i)
            page.mediaBox.lowerLeft = [-50,-20]
            page.mediaBox.upperRight = [850,630]

            output.addPage(page)

        outputStream = open('padded.pdf','wb')
        output.write(outputStream)

if __name__ == '__main__':
    path = 'wink.pdf'
    get_info(path)