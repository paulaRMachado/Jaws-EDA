import pandas as pd
import os

def aquire_data (name):
    """This function downloads from a raw link and saves the dataframe locally.
    args:
    :name: string. name to save the file
    """
    
    # 0. Establish variables
    path = f"data/{name}.csv"
    
    # 1. We read from the path
    df = pd.read_csv(path)
    
    return df