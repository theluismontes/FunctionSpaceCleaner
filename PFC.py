"""Bare Bones CI
May 15th, 2018 Version 1.0.0.100
May 22nd, 2018 Version 1.0.0.101
This program is designed to speed up the process of gathering information for function agendas within CI.
"""

#Below is the core function of the program. It opens a 
#predetermined CSV file and eliminates a couple rows 
#before releasing an output CSV file product.  

import csv

print ("Welcome to the Python Function Cleaner. This program is used to pre format function agendas in order to save time in creating proposals for Large Group Sales.")

def Core():
	with open("reallymessyfunction.csv", "rt") as function_in, open("cleanfunction.csv", "wt") as function_out:
		reader = csv.reader(function_in, delimiter=",")
		writer = csv.writer(function_out, delimiter=",")
		for row in reader:
			del row[46]
			del row[45]
			del row[44]
			del row[43]
			del row[42]
			del row[41]
			del row[40]
			del row[39]
			del row[38]
			del row[37]
			del row[36]
			del row[35]
			del row[34]
			del row[33]
			del row[32]
			del row[31]
			del row[30]
			del row[29]
			del row[28]
			del row[27]
			del row[26]
			del row[25]
			del row[24]
			del row[23]
			del row[22]
			del row[21]
			del row[20]
			del row[19]
			del row[18]
			del row[17]
			del row[16]
			del row[15]
			del row[14]
			del row[13]
			del row[12]
			del row[11]
			del row[9]
			del row[8]
			del row[2]
			writer.writerow(row)
Core()