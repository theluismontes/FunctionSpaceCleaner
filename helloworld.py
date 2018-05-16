"""Bare Bones CI
May 15th, 2018 Version 1.0.0.100
This program is designed to speed up the process of gathering information for function agendas within CI.
"""

import csv


def CC():
	with open("test.csv", "rb") as fp_in, open("product1.csv", "wb") as fp_out:
		reader = csv.reader(fp_in, delimiter=",")
		writer = csv.writer(fp_out, delimiter=",")
		for row in reader:
			del row[3]
			del row[1]
			writer.writerow(row)
CC()