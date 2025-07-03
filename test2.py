import pandas as pd
import plotly.express as px

df = pd.read_csv('datasets/iris.csv')
print(df)
print(df.columns)
plot = px.scatter(
    data_frame=df,
    size='sepal_width',
    template='plotly_dark',
    x='sepal_length',
    color='species',
    facet_col='species',
    y='petal_length',
    title='plot of sepal length and petal length'
)
plot.show()