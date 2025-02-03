import pandas as pd


def concat_dataframes(dataframes: list[pd.DataFrame]) -> pd.DataFrame:
  """
  Função que transforma uma lista de DataFrames em um DataFrame unido.
  """
  concated_df = pd.concat(dataframes, ignore_index=True)
  return concated_df

