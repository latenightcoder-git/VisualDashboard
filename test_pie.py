import pandas as pd
import plotly.express as px

df = pd.read_csv('datasets/tips.csv')
print(df.columns)
plot = px.pie(
    data_frame=df,
    values='tip',
    #names='sex',
    names='day',
    hole=0.5,
    title='tips for male and female'
)
plot.show()
