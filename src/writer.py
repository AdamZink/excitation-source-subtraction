import pandas as pd
import os
import io
import csv


class Writer:

	def __init__(self):
		# self.csv_data = io.StringIO()
		# self.csv_writer = csv.writer(self.csv_data, delimiter=',')
		self.data_string = ''
		self.excel_out_path = None
		self.sheet_name = None
		self.dataframe = None

	def save_row(self, row_string):
		self.data_string += row_string + '\n'
		# print(row_string)
		# self.csv_writer.writerow([row_string])
		# print(self.csv_data.getvalue())

	def export_to_excel(self, filename):  #, sheet_name
		# self.csv_data.seek(0)
		# print(self.csv_data)
		# self.dataframe = pd.read_csv(self.csv_data, delimiter=',', quoting=1)
		# print(self.dataframe)

		self.excel_out_path = os.path.join('..', 'output', filename)
		with open(self.excel_out_path, 'w') as f:
			f.write(self.data_string)

		# self.sheet_name = sheet_name
		# pdWriter = pd.ExcelWriter(self.excel_out_path, engine='xlsxwriter')
		# self.dataframe.to_excel(pdWriter, sheet_name=self.sheet_name)
		# pdWriter.save()
