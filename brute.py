#!/usr/bin/env python3 

import PyPDF2 as pd 
import re 
import random

# get the passwords line by line and store them in a list 

spaceREG = re.compile(r'(\w+)')

filepath = 'dictionary.txt'

file1 = open(filepath,'r')
lines= file1.readlines()

passwords = []
passwords1 = ['123123213213','123','123213213214234']
for i in range(len(lines)) :
  mo = spaceREG.search(lines[i])
  passwords.append(mo.group())


# try to open the file with every password possible

fileName = 'meetingminutes_encrypted.pdf'
pdfFile = open('meetingminutes_encrypted.pdf','rb')

pdfReader = pd.PdfFileReader(pdfFile)

if pdfReader.isEncrypted == True :
    for word  in passwords :  
     pdfReader.decrypt(word)
     if  pdfReader.decrypt(word) == 1 :             # break if  the incryption is false 
          print(f'password Cracked =>  \n{word}') 
          break

pdfWriter = pd.PdfFileWriter()


for pageNum in range(pdfReader.numPages) :
  pageObj = pdfReader.getPage(pageNum)
  pdfWriter.addPage(pageObj)

crackedFileName = fileName[:-14]+'decrypted.pdf'
print(f'Cracked file Name : {crackedFileName}')
result = open(crackedFileName,'wb')
files = pdfWriter.write(result)
  
