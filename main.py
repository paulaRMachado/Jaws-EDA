import src.aquire_data as aquire
import src.clean as clean
import src.visualization as viz

df = aquire.aquire_data("global_shark_attacks")
df_clean = clean.basic_cleaning(df)
viz.visualizing(df_clean)