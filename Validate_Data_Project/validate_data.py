import pandas as pd
import glob as g
import re
import os
import json


files_path = os.environ.get('PATH')
files = g.glob(f'{files_path}/*', recursive=True)
schemas = json.load(open('Validate_Data_Project/schemas.json'))


# get column names for datasets

def get_col_names(schemas, ds_name, sorting_key='column_position'):
    column_details = schemas[ds_name]
    columns = sorted(column_details, key=lambda col: col[sorting_key])
    return [col['column_name'] for col in columns]






    
def Validate_files():
    for f in files:
        file_name = re.split('[/]', f)
        print(f'\nProcessing file: {file_name[-1]}')
        col_names = get_col_names(schemas, file_name[-1], 'column_position')
        df = pd.read_csv(f, names=col_names)
        has_duplicates = df.duplicated().any()
        if has_duplicates == True:
            print(f'this dataset: {file_name[-1]} has duplicates')
        else:
            print(f'this dataset: {file_name[-1]} does not contain dublicate values')

        # check if column values has the right data type

        dt = df.dtypes
        dt_valid = True
        for col in schemas[file_name[-1]]:
            col_name = col["column_name"]
            schemas_dt = col["data_type"]
            if schemas_dt != df[str(col_name)].dtype:
                dt_valid = False
                break
        if dt_valid:
            print(f'all columns data_types in the Dataset: {file_name[-1]} match the schema data_types assigned for the columns')
        else:
            print(f'columns has mismatch value data_types in {file_name[-1]} Dataset')


        # checks if the file's path exists

        if not os.path.exists(f):
            print("File does not exist")

        # checks if its a file
        
        if not os.path.isfile(f):
            print("This is not a file")

        # checks if the file has data and not empty
        
        if os.path.getsize(f) == 0:
            print("File is empty")

        count = df.count()
        vcount = count.iloc[0]
        count_valid = True
        for c in count:
            if c != vcount:
                count_valid = False
                break
        if count_valid:
            print('all columns counts are valid\n')
        else:
            print('file has missing values\n')

Validate_files()





