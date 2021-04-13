#!/usr/bin/env python3

import PyPDF2 as pd 
import sys
import os

if len(sys.argv) < 2 : 
  print('[+] usage :  decrypter.py <password>')
else :
  path = os.path.abspath('secure')

  os.makedirs('Readable',exist_ok =True)
  dycrtpedPath = os.path.abspath('Readable')
  filesName= [] 
  filesNameOnly = []

  for root, dirs, files in os.walk(path) : 
    for filename in files :
      if filename.endswith('.pdf') : 
         filesName.append(os.path.join(root,filename))
         filesNameOnly.append(filename)

  
  try : 
      for pdfFiles in filesName : 
        pdf = open(pdfFiles,'rb')
        pdfReader = pd.PdfFileReader(pdf)
        pdfReader.decrypt(sys.argv[1])
      pdfWriter = pd.PdfFileWriter()

      for pageNum in range(pdfReader.numPages) :
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

      os.chdir(os.path.abspath(dycrtpedPath))
      print(os.getcwd())
      for i in range(len(filesNameOnly)) : 
        result = open(filesNameOnly[i][:-13]+'_deycrpted.pdf','wb')
        files = pdfWriter.write(result)
        print('Dycrpting files .... : %s '% filesNameOnly[i])
  except : 
    print('something went wrong or the password is incorrect')
