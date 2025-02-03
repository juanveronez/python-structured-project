import os
import pandas as pd

def load_to_excel(df: pd.DataFrame, filename: str, path: list[str] ):
  """
  Salva um DataFrame no formato Excel (xlsx)

  args:
  df: pd.DataFrame: Dataframe que será salvo em Excel
  filename: str: nome do arquivo que será gerado.
  path: list[str]: caminho que será usado para salvar o arquivo.
  """


  folder_path = os.path.join(*path)
  
  if not os.path.exists(folder_path):
    os.makedirs(folder_path)

  full_path = os.path.join(folder_path, f'{filename}.xlsx')
  df.to_excel(full_path, index=False)