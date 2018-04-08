from grapher import Grapher
from writer import RowWriter, ColumnWriter
from parameters import Parameters

params = Parameters()
params.use_37C_parameters()

excel_writer = RowWriter()
excel_writer.save_row('Mix,Measurement,Result,Diff')

subtracted_writer = ColumnWriter()

for sheet in params.sheets:
	print('\n======== ' + sheet + ' ========')
	grapher = Grapher()
	grapher.load_sheet_from_excel(params.filename, sheet)
	grapher.set_params(params)

	subtracted_writer.save_column('Wavelength', grapher.sheet.get_measurements('Wavelength'))

	for mixture in params.mixtures:
		resultMap = {}

		column_names = [c for c in list(grapher.sheet.dataframe) if c != 'Wavelength']
		for column_name in column_names:
			print('\n' + column_name)

			grapher.calc_exp_model('Wavelength', column_name)
			graph_name = mixture + '_' + column_name
			grapher.save_graph(graph_name)

			resultMap[column_name] = (grapher.get_subtracted_peak_intensity(), grapher.subtracted_amount)

			excel_writer.save_row(mixture + ',' + column_name + ','
				+ str(resultMap[column_name][0]) + ',' + str(resultMap[column_name][1]))

			subtracted_writer.save_column(column_name, grapher.y_data_subtract)

out_filename = 'subtraction_results-' + str(params.filename.replace('.xlsx', '')) + '.csv'
excel_writer.export_to_excel(out_filename)

data_filename = 'data_after_subtraction-' + str(params.filename)
subtracted_writer.export_to_excel(data_filename, 'subtracted data')

print('\nDone writing results to ' + out_filename)
