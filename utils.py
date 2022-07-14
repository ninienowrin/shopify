import pandas as pd
import numpy as np

def create_dataframe(data):

    columns = data[0].split(',')

    lst = []

    for line in data:
        entries = line.split(',')

        if entries[0].isnumeric() == False:
            continue
        
        lst.append(entries)

    array = np.array(lst)
    print(array.ndim)

    df = pd.DataFrame(array,columns=columns)
    return df

def modified_dataframe(df,columns):
    new_df = df[columns]
    return new_df

def get_frequency_of_purchase(data):
    gk = data.groupby(by = 'customer\.id')['order_id'].count().reset_index(name = 'order_count')
    gk = gk[:-1]
    sorted_gk = gk.sort_values('order_count',ascending=False)
    unique_values = sorted_gk.order_count.value_counts()

    return unique_values