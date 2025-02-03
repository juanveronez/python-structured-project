from pipeline.extract import extract_from_excels_folder
from pipeline.load import load_to_excel
from pipeline.transform import concat_dataframes

if __name__ == '__main__':
  df_list = extract_from_excels_folder(path=['data', 'input'])
  df = concat_dataframes(df_list)
  load_to_excel(df, 'output', path=['data', 'output'])