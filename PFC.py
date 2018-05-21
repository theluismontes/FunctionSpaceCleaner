"""Bare Bones CI
May 15th, 2018 Version 1.0.0.100
This program is designed to speed up the process of gathering information for function agendas within CI.
"""

#Below is the core function of the program. It opens a 
#predetermined CSV file and eliminates a couple rows 
#before releasing an output CSV file product.  

import csv
def Core():
	with open("messyfunction.csv", "rt") as function_in, open("cleanfunction.csv", "wt") as function_out:
		reader = csv.reader(function_in, delimiter=",")
		writer = csv.writer(function_out, delimiter=",")
		for row in reader:
			del row[0]
			del row[1]
			del row[2]
			writer.writerow(row)
Core()
