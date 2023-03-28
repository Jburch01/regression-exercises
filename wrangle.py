import pandas as pd
import numpy as np

from env import get_db_url



def get_zillow_data():
    '''
    Function will try to return ad database from csv file if file is local and in same directory.
    IF file doesn't exist it will create and store in same directory
    Otherwise will pull from codeup database.
    Must have credentials for codeup database.
    '''
    try:
        csv_info = pd.read_csv('zillow.csv', index_col=0 )
        return csv_info
    except FileNotFoundError:
        url = get_db_url('zillow')
        info = pd.read_sql('''
            select bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips from properties_2017 
            where propertylandusetypeid = 261;
        ''', url)
        info.to_csv("zillow.csv", index=True)
        return info




def wrangle_zillow():
    '''
    Funtion will return a zillow dataframe with the nulls dropped and the data cleaned
    (floats that didn't need to be floats converted to ints)
    '''
    df = get_zillow_data()
    df.bedroomcnt.fillna(3, inplace=True)
    df.bathroomcnt.fillna(2, inplace=True)
    df.dropna(inplace=True)
    df.bedroomcnt = df.bedroomcnt.astype(int)
    df.bathroomcnt = df.bathroomcnt.astype(int)
    df.yearbuilt = df.yearbuilt.astype(int)
    df.calculatedfinishedsquarefeet = df.calculatedfinishedsquarefeet.astype(int)
    return df
    