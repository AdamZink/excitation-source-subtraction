from grapher import Grapher
from writer import RowWriter
from parameters import Parameters

params = Parameters()
params.use_second_parameters()

excel_writer = RowWriter()
excel_writer.save_row('Time,Mix,Measurement,'
	+ ','.join(params.gases) + ','
	+ ','.join([g + '_diff' for g in params.gases]))

for sheet in params.sheets:
	print('\n======== ' + sheet + ' ========')
	grapher = Grapher()
	grapher.load_sheet_from_excel(params.filename, sheet)
	grapher.set_params(params)

	for mixture in params.mixtures:
		for measurement in params.measurements:
			resultMap = {}
			for gas in params.gases:

				column_name = params.column_name_function(mixture, measurement, gas)
				print('\n' + column_name)

				if column_name in grapher.sheet.measurements:

					grapher.calc_exp_model('Wavelength', column_name)
					graph_name = gas + '_' + sheet + '_' + mixture + '_' + measurement
					grapher.save_graph(graph_name)

					resultMap[gas] = (grapher.get_subtracted_peak_intensity(), grapher.subtracted_amount)

				else:
					resultMap[gas] = (0, 0)

			excel_writer.save_row(sheet + ',' + mixture + ',' + measurement + ','
				+ ','.join([str(resultMap[gas][0]) for gas in params.gases]) + ','
				+ ','.join([str(resultMap[gas][1]) for gas in params.gases]))

out_filename = 'subtraction_results-' + str(params.filename.replace('.xlsx', '')) + '.csv'
excel_writer.export_to_excel(out_filename)

print('\nDone writing results to ' + out_filename)
