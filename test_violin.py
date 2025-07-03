import pandas as pd
import plotly.express as px

df = pd.read_csv('datasets/iris.csv')
df1 = df.groupby(['species']).mean()
print(df1)
plot = px.violin(
    data_frame=df,
    x='species',
    y='sepal_width',
    color='species',
    #box = True,
    title='Violin plot showing average petal width across species'
)
plot.show()