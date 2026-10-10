import pandas as pd
import glob as g
import re
import os
import json
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL





schemas = json.load(open('Upload_Files_to_Postgresdb/schemas.json'))
load_dotenv()

# get column names for datasets

def get_col_names(schemas, ds_name, sorting_key='column_position'):
    column_details = schemas[ds_name]
    columns = sorted(column_details, key=lambda col: col[sorting_key])
    return [col['column_name'] for col in columns]


def read_csv(file, schemas):
    file_path_list = re.split('[/]', file)
    ds_name = file_path_list[-2]
    columns = get_col_names(schemas, ds_name)
    df_reader = pd.read_csv(file, names=columns, chunksize=10000)
    return df_reader


def to_sql(df, db_conn_url, ds_name):
    df.to_sql(ds_name,db_conn_url,if_exists='append', index=True)


def db_loader(src_dir, db_conn_url, ds_name):
    files = (f'{src_dir}/{ds_name}/part-00000')
    if len(files) == 0:
        raise NameError(f'No files found for {ds_name}')

    df_reader = read_csv(files, schemas)
    for idx, df in enumerate(df_reader):
        print(f'Populating chunk {idx} of {ds_name}')
        to_sql(df, db_conn_url, 'orders')



def process_files(ds_names=None):
    src_dir = os.environ.get('SRC_DIR')
    db_host = os.environ.get('DB_HOST')
    db_port = int(os.environ.get('DB_PORT'))
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_conn_url = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
    schemas = json.load(open(f'{src_dir}/schemas.json'))
    
    if not ds_names:
        ds_names = schemas.keys()
    for ds_name in ds_names:
        try:
            print(f'Processing {ds_name}')
            db_loader(src_dir, db_conn_url, ds_name)
        except NameError as ne:
            print(ne)
            pass
        except Exception as e:
            print(e)
            pass
        finally:
            print(f'Error Processing {ds_name}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        ds_names = json.loads(sys.argv[1]) 
        process_files(ds_names)
    else:
        process_files()

