import plotly.express as px
from preswald import text, table, get_df, connect, query, plotly

text("# Hello Preswald")
connect()
df = get_df("titanic")
filtered_df = query("SELECT Name FROM titanic", "titanic")
table(filtered_df, title="Filtered Data")

new_df = query("SELECT COUNT(*) / (SELECT COUNT(*) FROM titanic) * 100 AS Percentage, Sex, Survived FROM titanic GROUP BY Sex, Survived", "titanic")
text("## plot")
fig = px.bar(new_df, x="Sex", y="Percentage", color="Survived")
plotly(fig)