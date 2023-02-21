import pandas as pd

# create dataframe

rounds = ['first', 'second', 'third', 'forth', 'fifth', 'sixth']
vals = [1,2,3,4,5,6]
whos = ['teamA', 'teamB', 'teamC', 'teamD', 'teamE', 'teamF']

df_dict = {'Rounds': rounds, 'Vals': vals, 'Teams': whos}

df = pd.DataFrame(df_dict)

print(df)