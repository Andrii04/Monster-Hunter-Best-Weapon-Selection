import pandas as pd
monster_base = pd.read_csv("monster_base.csv")
monster_ailments = pd.read_csv("monster_ailments.csv")
monster_breaks = pd.read_csv("monster_breaks.csv")
monster_hitzones = pd.read_csv("monster_hitzones.csv")
monster_weaknesses = pd.read_csv("monster_weaknesses.csv")

#renaming to have a unique key in the first column (monster name)
monster_dataframes = [monster_base, monster_ailments, monster_breaks, monster_hitzones, monster_weaknesses]
for df in monster_dataframes:
    df.rename(columns={df.columns[0] : "name en"}, inplace=True)
#fixing type to allow merge based on key
monster_base["name en"] = monster_base["name en"].astype(object)
#Merging DataFrames
monster_dataset = monster_base.merge(monster_ailments, on="name en", how="left")
monster_dataset = monster_dataset.merge(monster_breaks, on="name en", how="left")
monster_dataset = monster_dataset.merge(monster_hitzones, on="name en", how="left")
monster_dataset = monster_dataset.merge(monster_weaknesses, on="name en", how="left")
print(monster_dataset.head())
#errori dopo il merge dei dataframe, controllare meglio