from grapher import Grapher

grapher = Grapher()
grapher.load_sheet_from_excel('Solvent_variation_condensed_data.xlsx', 'Initial')

grapher.calc_exp_model('Wavelength', '90_10_1_Air')
grapher.show_graph()

grapher.calc_exp_model('Wavelength', '90_10_2_Air')
grapher.show_graph()

grapher.calc_exp_model('Wavelength', '90_10_3_Air')
grapher.show_graph()
