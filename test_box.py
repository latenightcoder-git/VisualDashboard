import pandas as pd
import plotly.express as px

df = pd.read_csv('datasets/iris.csv')
df1 = df.groupby(['species']).mean()
print(df1)
plot = px.box(
    data_frame=df,
    x='species',
    y='sepal_width',
    title='Box plot showing average petal width across species'
)
plot.show()