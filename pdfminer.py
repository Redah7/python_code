# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:37:36 2020

@author: redah7
"""

   
import os    
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO

#use if setting current wd
#path=os.chdir('')


path='C:\\Users\\MLCMOG001\\Desktop\\CV Ranker\\CV data'

path = ' '
def pdf_to_text(path):
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    filepath.close()
    device.close()
    retstr.close()
    return text


if __name__ == "__main__":
    text = pdf_to_text("Name.pdf")
    print(text)    