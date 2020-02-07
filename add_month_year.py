import pandas

df = pandas.read_csv('sample.csv')

df['Day'] = pandas.to_datetime(df['Day'])
df['Month_Year'] = df['Day'].dt.to_period('M')

df.to_csv(r'sampleoutput.csv', index = None, header = True)

