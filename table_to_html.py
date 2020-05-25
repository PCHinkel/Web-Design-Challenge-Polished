import pandas as pd

data = pd.read_csv("Resources/cities.csv")

# the below structure came from https://pythonexamples.org/pandas-render-dataframe-as-html-table/

#render dataframe as html
html = data.to_html()

#write html to file
text_file = open("table_data.html", "w")
text_file.write(html)
text_file.close()