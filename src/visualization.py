import pandas as pd
import matplotlib.pyplot as mplot
import seaborn as sbn
import os

def visualizing (jaws):
    """This function groups by type 
    and creates a bar chart with avgeprice
    Arguments
    :df: df. dataframe to group
    """
    # General deaths per time
    fatality = jaws.loc[(jaws.fatal == "Fatal")]
    death_time = sbn.countplot(x=fatality.time, palette="mako", order = ["Morning","Afternoon", "Evening", "Night"])
    death_time.set(xlabel='Times of the day', title="Time of deaths", ylabel= 'Number of deaths')
    death_time.figure.savefig("images/Time of deaths.png", dpi=100)
    ## Deaths by gender
    death_gender = sbn.countplot(x=fatality.gender, palette="rocket")
    death_gender.set(xlabel='Gender', title="Deaths by gender", ylabel= 'Number of deaths')
    death_gender.figure.savefig("images/Deaths by gender.png", dpi=100)
    ## Womens deaths
    df_death_women = fatality.loc[(fatality.gender == "Female")]
    death_women_time = sbn.countplot(x=df_death_women.time, hue =df_death_women.species, palette="rocket", hue_order = ["Unidentified","White Shark", "Bull Shark","Tiger Shark", "Hammerhead Shark"],order = ["Morning","Afternoon", "Evening", "Night"])
    death_women_time.set(xlabel='Times of the day', title="Women's time of deaths ", ylabel= 'Number of deaths')
    death_women_time.figure.savefig("images/Womens time of death and sharks.png", dpi=100)
    ###attacks after 1900
    condition_1 = jaws.year >= 1900
    hist_df = jaws[condition_1]
    shark_attacks_hist = sbn.histplot(x=hist_df.year, hue = hist_df.fatal, binwidth=10, multiple = "stack", palette="mako").set(title="Incidents involving sharks after 1900")
    mplot.savefig("images/incidents involving sharks.png", dpi=100)
    ### Deaths in history
    death_hist = sbn.lineplot(data =hist_df, x="year", y="number_deaths", estimator="sum").set(title="Deaths per year involving sharks from 1900 to 2020")
    mplot.savefig("images/history of death.png", dpi=100)
    ## Deaths of women per continent
    women_death_continent= sbn.countplot(data=df_death_women, x= df_death_women["fatal"], hue=df_death_women["continent"], palette="rocket", hue_order=["OCEANIA", "NORTH AMERICA","EUROPE","AFRICA","ASIA","CENTRAL AMERICA","SOUTH AMERICA"])
    women_death_continent.set(xlabel='Continents', title="Women's deaths per continent", ylabel= 'Number of deaths')
    women_death_continent.figure.savefig("images/Womens deaths per continent.png", dpi=100)

    # 2. Open
    os.system(f"open images/Womens_deaths_per_continent.png")
    os.system(f"open images/history_of_death.png")
    os.system(f"open images/incidents_involving_sharks.png")
    os.system(f"open images/Womens_time_of_death_and_sharks.png")
    os.system(f"open images/Deaths_by_gender.png")
    os.system(f"open images/Time_of_deaths.png")