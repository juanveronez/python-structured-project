import os
import glob

import pandas as pd

def extract_from_excels_folder(path: list[str]) -> list[pd.DataFrame]: 
  """
  função para ler os arquivos de uma pasta em path e retornar uma lista de DataFrames

  args: input_path (str): caminho da pasta para extração

  return: df_list: lista de DataFrames
  """

  full_path = os.path.join(*path, '*.xlsx')
  path_files = glob.glob(full_path)

  dataframes = [pd.read_excel(file) for file in path_files]
  return dataframes

if __name__ == '__main__':
  dataframes = extract_from_excels_folder(path=['data', 'input'])
  print(dataframes)