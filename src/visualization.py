import pandas as pd
import matplotlib.pyplot as mplot
import seaborn as sbn
import os


def visualizing_1 (jaws):
    """This function groups by type 
    and creates a bar chart with avgeprice
    Arguments
    :df: df. dataframe to group
    """
    # General deaths per time
    fatality = jaws.loc[(jaws.fatal == "Fatal")]
    death_time = sbn.countplot(x=fatality.time, palette="mako", order = ["Morning","Afternoon", "Evening", "Night"])
    death_time.set(xlabel='Times of the day', title="Time of deaths", ylabel= 'Number of deaths')
    death_time.figure.savefig("images/Time_of_deaths.png", dpi=100)
    os.system(f"open images/Time_of_deaths.png")

def visualizing_2 (jaws):
    ## Deaths by gender
    fatality = jaws.loc[(jaws.fatal == "Fatal")]
    death_gender = sbn.countplot(x=fatality.gender, palette="rocket")
    death_gender.set(xlabel='Gender', title="Deaths by gender", ylabel= 'Number of deaths')
    death_gender.figure.savefig("images/Deaths_by_gender.png", dpi=100)
    os.system(f"open images/Deaths_by_gender.png")

def visualizing_3 (jaws):
    ## Womens deaths
    fatality = jaws.loc[(jaws.fatal == "Fatal")]
    df_death_women = fatality.loc[(fatality.gender == "Female")]
    death_women_time = sbn.countplot(x=df_death_women.time, hue =df_death_women.species, palette="rocket", hue_order = ["Unidentified","White Shark", "Bull Shark","Tiger Shark", "Hammerhead Shark"],order = ["Morning","Afternoon", "Evening", "Night"])
    death_women_time.set(xlabel='Times of the day', title="Women's time of deaths ", ylabel= 'Number of deaths')
    death_women_time.figure.savefig("images/Womens_time_of_death_and_sharks.png", dpi=100)
    os.system(f"open images/Womens_time_of_death_and_sharks.png")

def visualizing_4 (jaws):    
    ###attacks after 1900
    condition_1 = jaws.year >= 1900
    hist_df = jaws[condition_1]
    shark_attacks_hist = sbn.histplot(x=hist_df.year, hue = hist_df.fatal, binwidth=10, multiple = "stack", palette="mako").set(title="Incidents involving sharks after 1900")
    mplot.savefig("images/incidents_involving_sharks.png", dpi=100)
    os.system(f"open images/incidents_involving_sharks.png")

def visualizing_5 (jaws):      
    ### Deaths in history
    condition_1 = jaws.year >= 1900
    hist_df = jaws[condition_1]
    death_hist = sbn.lineplot(data =hist_df, x="year", y="number_deaths", estimator="sum", ci=None).set(title="Deaths per year involving sharks from 1900 to 2020")
    mplot.savefig("images/history_of_death.png", dpi=100)
    os.system(f"open images/history_of_death.png")

def visualizing_6 (jaws):  
    ## Deaths of women per continent
    fatality = jaws.loc[(jaws.fatal == "Fatal")]
    df_death_women = fatality.loc[(fatality.gender == "Female")]
    women_death_continent= sbn.countplot(data=df_death_women, x= df_death_women["fatal"], hue=df_death_women["continent"], palette="rocket", hue_order=["OCEANIA", "NORTH AMERICA","EUROPE","AFRICA","ASIA","CENTRAL AMERICA","SOUTH AMERICA"])
    women_death_continent.set(xlabel='Continents', title="Women's deaths per continent", ylabel= 'Number of deaths')
    women_death_continent.figure.savefig("images/Womens_deaths_per_continent.png", dpi=100)

    os.system(f"open images/Womens_deaths_per_continent.png")
    

 
  
