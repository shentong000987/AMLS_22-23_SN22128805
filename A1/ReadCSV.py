import pandas as pd
import numpy as np

def csv(file_path, column_name):

    #read csv file with separator symbol '\t'
    df = pd.read_csv(file_path,sep='\t')

    #column_name = 'gender'

    column_data= df[column_name]

    #change the list to Num array for later use
    labels = np.array(column_data)

    print(labels.size)

    return labels
