#!/usr/bin/env python3
import PyPDF2 as pd 
import os 

filePath = '/home/johnripper/Desktop/exercices/automation/advanced_practiceProjects/pdf_encrypter/test/root/pdf.pdf'

pdfFileObj = open(filePath,'rb')

pdfReader = pd.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)


