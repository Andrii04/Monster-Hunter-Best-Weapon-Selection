import pandas as pd


#Data of Monsters 
monster_base = pd.read_csv(r"C:\Users\andri\OneDrive\Desktop\VsProjects\monster_base.csv")
#filling in Missing Values
monster_base["ecology_en"].fillna("Not Specified", inplace=True)
monster_base.fillna({"pitfall_trap":"False", "shock_trap":"False", "vine_trap":"False"}, inplace=True)
monster_base.to_csv(r"C:\Users\andri\OneDrive\Desktop\VsProjects\monster_base.csv", index=False)

#Data of Monster Ailments
monster_ailments = pd.read_csv(r"C:\Users\andri\OneDrive\Desktop\VsProjects\monster_ailments.csv")
#dropping colums I don't need for the project
monster_ailments.drop(["roar", "wind", "tremor"], axis=1, inplace=True)
#filling in Missing Values
monster_ailments.iloc[:, 1::] = monster_ailments.iloc[:, 1::].fillna("False")
monster_ailments.to_csv(r"C:\Users\andri\OneDrive\Desktop\VsProjects\monster_ailments.csv", index=False)


#Data of Monster Breaks
monster_breaks = pd.read_csv(r"C:\Users\andri\OneDrive\Desktop\VsProjects\monster_breaks.csv")
#dropping useless column (no values)
monster_breaks.drop("part_ja", axis=1, inplace=True)
#filling in Missing Values
monster_breaks.iloc[:, 2:5] = monster_breaks.iloc[:, 2:5].fillna(0)
monster_breaks.to_csv(r"C:\Users\andri\OneDrive\Desktop\VsProjects\monster_breaks.csv", index=False)


#Data of Monster Hitzones
monster_hitzones = pd.read_csv(r"C:\Users\andri\OneDrive\Desktop\VsProjects\monster_hitzones.csv")
monster_hitzones.to_csv(r"C:\Users\andri\OneDrive\Desktop\VsProjects\monster_hitzones.csv", index=False)


#Data of Monster Weaknesses
monster_weaknesses = pd.read_csv(r"C:\Users\andri\OneDrive\Desktop\VsProjects\monster_weaknesses.csv")
#filling in Missing Values
monster_weaknesses["alt_description"].fillna("N/A", inplace=True)
monster_weaknesses.iloc[:, 8::] = monster_weaknesses.iloc[:, 8::].fillna(0)
monster_weaknesses.to_csv(r"C:\Users\andri\OneDrive\Desktop\VsProjects\monster_weaknesses.csv", index=False)