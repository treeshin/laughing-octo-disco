import pandas as pd


testset = 'Co_5km_test10'
filename = testset + '.m'

df = pd.read_csv(filename, header = None, names = range(21), skiprows = 0, sep = ',|\s+', engine = 'python', on_bad_lines='skip')

ending_index = df.loc[df[0] == 11].index
starting_index = 0
for i in range(len(ending_index)):
    df_chunk = df.iloc[starting_index:ending_index[i]+1,:]
    grouped = df_chunk.groupby(df_chunk.columns[0])
    df_group = grouped.get_group(14)
    df_group = df_group[::-1]
    # print(df_group)
    savefilename = 'BKG_' + testset + '_' + str(i+1) + '.csv'
    df_group.to_csv(savefilename, sep = ',', index = False, header = False)
    starting_index = ending_index[i]+1 
