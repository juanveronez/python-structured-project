import pandas as pd

from src.pipeline.transform import concat_dataframes

df_1 = pd.DataFrame({"a": [1, 2], "b": [1, 2]})
df_2 = pd.DataFrame({"a": [3, 4], "b": [3, 4]})
df_res = pd.DataFrame({"a": [1, 2, 3, 4], "b": [1, 2, 3, 4]})


def test_transform():
    transformed_df = concat_dataframes([df_1, df_2])

    assert transformed_df.shape[0] == 4
    assert list(transformed_df.columns) == ["a", "b"]

    assert transformed_df.equals(df_res)
    assert not concat_dataframes([df_2, df_1]).equals(df_res)
