import pandas as pd
import sys

def map_new_headings_csv(old_data_csv, new_headings_csv):
    '''
    Description:
    Takes two paths as string to files and maps one heading to 
    another and produces a new csv.
    
    Parameters:
    :old_data_csv: Path to a csv file with headings to be updates
    :new_headings_csv: Path to a csv file with new headings
    
    Returns:
    Creats a new csv file with new headings
    '''
    
    #Varibles
    data_df = pd.read_csv(old_data_csv)
    
    #create heading lists
    new_headings_lst = pd.read_csv(new_headings_csv).columns.values
    data_headings_lst = data_df.columns.values
    
    #create a mapping dictionary
    mapping = dict(zip(data_headings_lst, new_headings_lst))
    
    #rename columns in old data
    data_df = data_df.rename(columns=mapping)
    
    #create the new csv
    data_df.to_csv('data_with_new_headings.csv')

if __name__ == "__main__":
    map_new_headings_csv(sys.argv[1], [2])