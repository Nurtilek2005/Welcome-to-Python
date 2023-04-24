import jupyter
import jupyter_client
import pandas as pd

df = pd.read_csv("./california_housing_test.csv")

max = df['median_house_value'].max()
filter = df['median_income'] == 3.1250
filter_1 = df[df['median_house_value'] == max]
print(type(filter_1['median_income'] == 3.1250))