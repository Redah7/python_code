# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:37:36 2020

@author: redah7
"""

import PyPDF2    
# pdf file object
# you can find find the pdf file with complete code in below
pdfFileObj = open('name.pdf', 'rb')
# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# number of pages in pdf
print(pdfReader.numPages)
# a page object
pageObj = pdfReader.getPage(0)
# extracting text from page.
# this will print the text you can also save that into String
print(pageObj.extractText())
#save object into variable
x=pageObj.extractText()