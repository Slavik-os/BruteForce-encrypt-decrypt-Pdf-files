#!/usr/bin/env python3
import PyPDF2 as pd 
import sys
import os
import shutil



if (len(sys.argv) < 2 )   :
		print('[+] usage : encrypter.py <Password>')
else :
# Create a folder and get all the pdf files in the folder path
	path = 'root'
	absPath = os.path.abspath(path)



	os.makedirs('secure',exist_ok=True)

	filesNamesWithPath = []
	filesNameList = []

	for root , dirs , files in os.walk(absPath) : 
		for filesName in files : 
			if filesName.endswith('.pdf') :
				filesNamesWithPath.append(os.path.join(root,filesName))
				filesNameList.append(filesName)


	# read the files 


	for file in filesNamesWithPath :
			pdfFileObj =open(file,'rb')
			pdfReader = pd.PdfFileReader(pdfFileObj)


	pdfWriter = pd.PdfFileWriter()

	for pageNum in range(pdfReader.numPages) :
			pageObj = pdfReader.getPage(pageNum)
			pdfWriter.addPage(pageObj)


	password = str(sys.argv[1])
	os.chdir('secure')
	
	for i in range(len(filesNameList)) :

		result = open(filesNameList[i][:-4]+'_encrypted.pdf','wb')
		folderPath = os.path.abspath('secure')
		pdfWriter.encrypt(password)
		files = pdfWriter.write(result)


	filesBytes = []
	for root , dirs , files in os.walk('.') :
		for file in files :
			stats = os.stat(file)
			filesBytes.append(stats.st_size)


	for i in range(len(filesBytes)) :

		print('Encripting Files ... %s , new size : ' %filesBytes[i])

			

			


	for i in range(len(filesBytes)) :
			if filesBytes[i] != 0 :
					os.chdir(absPath)
					for root , dirs , files in os.walk(absPath) :
			  			for file in files :
			  				
			  				os.remove(os.path.join(root,file))

