import pandas as pd

df = pd.read_table("/Users/jameschen/Dropbox/GradSchool/*Spring_18/hort503/ClassExercises/Feb27/data.txt")
# df.iloc(row, col])
drugname = list(df.iloc[:,1:9])
drugname
df_drop = df.drop(drugname, axis = 1)
df_drop
df2 = pd.melt(frame = df_drop, id_vars = ['SeqID'], var_name="AA_pos", value_name="AA")
df2
