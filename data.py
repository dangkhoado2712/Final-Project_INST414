import pandas as pd
import matplotlib.pyplot as plt 

# Read data into dataframe
df = pd.read_csv("G:\My Drive\Fall2022\INST414\Final Project\data.csv")
df

# Get to know the data
df.columns
df['date'].min()
df['date'].max()

df['location'].value_counts()

# Get the data for the United State and each state seperate for futher analysis
df_US = df[df['location'] == 'United States']
df_US

# Remove the value is not the state of the US
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska','Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York State', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee','Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming' ]
df_states = df[df['location'].isin(states) == True]
df_states

df_states['location'].value_counts()


# Ingest data frame to csv
df_US.to_csv("G:\My Drive\Fall2022\INST414\Final Project\cleaned_US.csv")
df_states.to_csv("G:\My Drive\Fall2022\INST414\Final Project\cleaned_states.csv")



