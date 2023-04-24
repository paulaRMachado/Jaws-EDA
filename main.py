import src.aquire_data as aquire
import src.clean as clean
import src.visualization as viz

df = extract.downloading("global_shark_attacks")
df_clean = clean.basic_cleaning(df)
viz.visualizing(df_clean)