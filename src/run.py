from grapher import Grapher
from writer import Writer
from parameters import Parameters

params = new Parameters()
params.use_second_parameters()

excel_writer = Writer()
excel_writer.save_row('Time,Mix,Measurement,' + ','.join(gases))

for sheet in params.sheets:
	print('\n======== ' + sheet + ' ========')
	grapher = Grapher()
	grapher.load_sheet_from_excel(params.filename, sheet)

	for mixture in params.mixtures:
		for measurement in params.measurements:
			resultMap = {}
			for gas in params.gases:

				column_name = mixture + '_' + measurement + '_' + gas
				print('\n' + column_name)

				grapher.calc_exp_model('Wavelength', column_name)
				grapher.save_graph(gas + '_' + sheet + '_' + mixture + '_' + measurement)

				resultMap[gas] = grapher.get_subtracted_peak_intensity()

			excel_writer.save_row(sheet + ',' + mixture + ',' + measurement + ',' + ','.join([str(resultMap[gas]) for gas in gases]))

excel_writer.export_to_excel('subtraction_results.csv')

print('\nDone writing file')
