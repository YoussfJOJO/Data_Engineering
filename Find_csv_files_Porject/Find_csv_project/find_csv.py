import pandas as pd
import os
import glob as g

src_base_dir = os.environ.get('SRC_BASE_DIR')

def find_csv_files(src_base_dir):
    csv = g.glob(f'{src_base_dir}*.csv', recursive=True)
    return csv

print(find_csv_files(src_base_dir))