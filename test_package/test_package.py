#!pip install git+https://github.com/user/yourteamrepo
#run this file from the root of the repository as test_package/test_package.py
from Analysis import Analysis

analysis_obj = Analysis('test_package/tc_config.yml')
analysis_obj.load_data()


#analysis_output = analysis_obj.compute_analysis()
#print(analysis_output)

#analysis_figure = analysis_obj.plot_data()
