#!/usr/bin/python3

from PyPDF2 import PdfFileReader, PdfFileWriter

def get_sub_pdf(name,super_pdf,start_page,end_page):
    pdf_read = PdfFileReader(open(super_pdf,'rb'))
    pdf_output = PdfFileWriter()
    
    #for page in range(start_page,end_page+1):
    for page in range(start_page-1,end_page):
        pdf_output.addPage(pdf_read.getPage(page))

    pdf_output.write(open(name,'wb'))

def merger_pdf(pdfs,name,pages_index):
    output=PdfFileWriter()

    for pdf in pdfs:
        pdf_read = PdfFileReader(open(pdf, "rb"))
        pages = pdf_read.getNumPages()
        pages_index.append(pages)

        for page in range(pages):
            output.addPage(pdf_read.getPage(page))
        if pages%2 == 1:
            output.addBlankPage(width=None,height=None)

    output.write(open(name,'wb'))

import sys
import os

#super_pdf = sys.argv[1]  # You should input the name of file you would like to split 


if __name__ == "__main__":
       
    #file = open(index_file,'r')

    #lines = file.readlines()
    #os.system('mkdir '+super_pdf)

    #for i in range(len(lines)):
    #    indexs = lines[i].split()
    #    file_id = indexs[5]
    #    if not file_id == super_pdf:
    #        continue
    #    start_page = int(indexs[0])
    #    end_page = int(indexs[1])
    #    name = '_'.join(indexs[2:5])+".pdf"

    #    get_sub_pdf(name,super_pdf+'.pdf',start_page,end_page)
    #    os.system('mv '+name+' '+super_pdf)

    files = os.listdir('.')

    index_file = open('index0','r')
    indexs = index_file.read().split()
    new_files = []
    for index in indexs:
        for file in files:
            if index in file:
                new_files.append(file)
                break
    files = new_files
    
    pages = []
    file2 = open('index2','w')
    merger_pdf(files,'total.pdf',pages)
    for i,page in enumerate(pages):
        if page%2==0:
            file2.write(str(files[i])+'_'+str(int(page/2))+"\n")
        else:
            file2.write(str(files[i])+'_'+str(int(page/2)+1)+"\n")
    file2.close()

