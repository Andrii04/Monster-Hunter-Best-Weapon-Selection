import pandas as pd

monster_base = pd.read_csv("monster_base.csv")
monster_weaknesses = pd.read_csv("monster_weaknesses.csv")
monster_hitzones = pd.read_csv("monster_hitzones.csv")
monster_breaks = pd.read_csv("monster_breaks.csv")
monster_ailments = pd.read_csv("monster_ailments.csv")

mhDFs = {"monster_base" : monster_base,
         "monster_weaknesses" : monster_weaknesses,
         "monster_hitzones" : monster_hitzones,
         "monster_breaks" : monster_breaks,
         "monster_ailments" : monster_ailments}

weak_fire = monster_weaknesses.loc[monster_weaknesses["fire"] >= 2]
weak_fireblight = monster_ailments.loc[monster_ailments["fireblight"] == True]
#da fare quella cosa di rinominare tutto in name_en e avere i tipi compatibili e eliminare la colonna id 
#da monster_base così ho tutti i df pronti se devo fare un merge o qualcosa!