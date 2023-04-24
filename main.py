import src.aquire_data as aquire
import src.clean as clean
import src.visualization as viz

df = extract.downloading("data/global_shark_attacks.csv", "global_shark_attacks")
## don't know how to solve this link issue
df_clean = clean.basic_cleaning(df)
viz.visualizing(df_clean, "avg_price_by_type")