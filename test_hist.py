import pandas as pd
import plotly.express as px

df = pd.read_csv('datasets/iris.csv')

plot = px.histogram(
    data_frame=df,
    x='sepal_length',
    color='species',
    barmode='group',
    title='Distribution of sepal length'
)
plot.show()