import pandas as pd
import matplotlib.pyplot as plt
import sys
import yaml


def get_config():
    """
    Reads config from config.yaml
    """
    with open("config.yaml","r") as file_object:
        data=yaml.load(file_object,Loader=yaml.SafeLoader)
        return data

config = get_config()

if len(sys.argv) < 2:
    print("Missing filename :(")
    exit(1)

file_name = sys.argv[1]

data = pd.read_csv(f'data\\{file_name}.txt', sep='\s+', header=None)
window_size = config["rolling_avg"]["window_size"]
column = config["rolling_avg"]["index_base_column"]

data['roling_avg'] = data.iloc[:, column].rolling(window=window_size).mean()

new_file_name = f'data\\{file_name}_with_moving_avg.csv'
data.to_csv(new_file_name, index=False)
