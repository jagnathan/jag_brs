!pip install git+https://github.com/jagnathan/jag_brs.git
from jag_brs import Analysis

analysis_obj = Analysis('tc_config.yml')
analysis_obj.load_data()


#analysis_output = analysis_obj.compute_analysis()
#print(analysis_output)

#analysis_figure = analysis_obj.plot_data()
