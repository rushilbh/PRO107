import pandas as pd
import plotly.express as go
import csv

#code to read csv using pandas
df  = pd.read_csv('students.csv')


#filtering the data for graph
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()

fig = go.scatter(mean,x = 'student_id', y = 'level',size = 'attempt',color = 'attempt')
fig.show()