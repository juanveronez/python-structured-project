from pipeline.extract import extract_from_excels_folder

df_list = extract_from_excels_folder('data', 'input')
print(df_list)