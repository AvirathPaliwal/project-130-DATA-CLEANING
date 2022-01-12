import pandas as pd
import csv

df = pd.read_csv("Dwarf_stars_converted.csv")
print(df.shape)


del df["Distance"]

print(df.shape)

print(list(df))

df = df.rename({
    "Name" : "P_name",
    "Mass" : "P_mass",
    "Rdius" : "P_radius"
},axis='columns' )

print(list(df))
df.to_csv("main.csv")