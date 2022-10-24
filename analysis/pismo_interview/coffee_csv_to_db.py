import pandas as pd
import sqlite3

conn = sqlite3.connect("quotes.db")

df = pd.read_csv('entries/coffee.csv', header = 0, sep = ",", encoding = "utf8")

df.to_sql('coffee', conn, if_exists='replace', index = False)