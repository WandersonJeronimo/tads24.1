import pandas as pd
from functions.create_dataframe import create_dataframe_example

#load example table
df = create_dataframe_example (seed = 83)

# filter by colums
df [['Nome', 'Turno']]
df [['Turno', 'Nome']].head(n = 6)
df [['Nome', 'Turno']].tail()

#filter by filter
type (df['Nota_1'])
type (df[['Nota_1']])

df [
    (df ['Nota_1'] > 80) &
    (df ['Turno'] == 'Evening')
]

df.query ("Nota_1 > 80 and Turno == 'Evening'")

# Combine rows and colums
df \
    .query ("Nota_1 > 80 and Turno == 'Evening'") \
    [['Nome']]

# aggregate
df \
    .groupby('Turno')


df \
    .groupby('Turno') \
    .agg(
         Nota_1_media = ('Nota_1', 'mean'),
         Nota_2_media = ('Nota_2', 'mean')
    ) \
    .reset_index()


# Change or create colums
df \
    .groupby('Turno') \
    .agg(
         Nota_1_media = ('Nota_1', 'mean'),
         Nota_2_media = ('Nota_2', 'mean')
    ) \
    .reset_index() \
    .assign(    
        Nota_1_media = lambda x: round(x['Nota_1_media'], 2),
        Nota_2_media = lambda x: round(x['Nota_2_media'], 2),
        Nota_media_soma = lambda x: x['Nota_1_media'] + x['Nota_2_media']
    )
