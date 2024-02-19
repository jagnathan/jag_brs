from typing import Any, Optional
import matplotlib.pyplot as plt
import yaml
import requests
import pandas as pd
import os


class Analysis():

    def __init__(self, analysis_config: str) -> None:
        CONFIG_PATHS = ['configs/system_config.yml', 'configs/user_config.yml']

        # add the analysis config to the list of paths to load
        print(analysis_config)
        paths = CONFIG_PATHS + [analysis_config]

        # initialize empty dictionary to hold the configuration
        config = {}
        data = None
        analyzed_data = None

        # load each config file and update the config dictionary
        for path in paths:
            print (path)
            with open(path, 'r') as f:
                this_config = yaml.safe_load(f)
            config.update(this_config)

        self.config = config

    def load_data(self) -> None:
        print(self.config['figure_title'])
        #print(self.config['nasa_url'])
        #print(self.config['pokemon_url'])

        #'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY'
        response = requests.get(url=self.config['pokemon_url'],
                        headers={'Authorization': 'Bearer ' + self.config['token']})

        # print raw response
        #print(response.status_code)
        #print(response.text)

        # parse json
        self.data = response.json()


    def calc_roverid(self, x):
        return x['rover']['id'] 
    
    def calc_cameraid(self, x):
        return x['camera']['id'] 

    def getabbrev(self, x):
        return x[0] 

    def compute_analysis(self) -> Any:
        #print(self.data)
        try:
            df_pokemon = pd.json_normalize(self.data['results'])
            #print(df_pokemon.columns)
            df_pokemon['name_code'] = df_pokemon['name'].apply(self.getabbrev)
            self.analyzed_data = df_pokemon.groupby('name_code').size().reset_index(name='count')
            #print(self.analyzed_data)
            # df_photos['roverid'] = df_photos['rover'].apply(self.calc_roverid)
            # df_photos['cameraid'] = df_photos['rover'].apply(self.calc_cameraid)
            # df_photos.drop(columns=['rover', 'camera'], inplace=True)
        except:
            return "Error: Could not parse data"

    def plot_data(self, save_path: Optional[str] = None) -> plt.Figure:
        fig, ax = plt.subplots()
        ax.scatter(self.analyzed_data['name_code'], self.analyzed_data['count'], color=self.config['color'])
        ax.set_xlabel('Pokemon Fans Starting Letter')
        ax.set_ylabel('Count')
        ax.set_title(self.config['figure_title'])
        try:
            if save_path is not None:
                plt.savefig(save_path+self.config['figure_title']+'.png')
        except:
            plt.savefig('Analysis'+ self.config['figure_title']+'.png')
        return fig
    

    def notify_done(self, message: str) -> None:
        pass
    