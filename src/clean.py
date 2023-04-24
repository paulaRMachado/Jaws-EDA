import pandas as pd
import re

def basic_cleaning (df):
    """
    This function renames columns, drops a few unnecessary columns, fills nans, creates a new column CONTINENT.
    args
    :df: dataframe to be cleaned
    return: cleaned dataframe
    """
    # 1. Overall cleaning
    df.drop_duplicates(inplace=True)
    df.dropna(thresh=3, inplace=True)
    df.drop(columns=['pdf', 'href formula', 'href', 'Unnamed: 22', 'Unnamed: 23', 'Case Number','original order', 'Case Number.1','Case Number.2'], inplace=True)
    df.columns = [i.lower().replace(" ", "-") for i in df.columns]
    df.rename(columns={"species-": "species", "sex-":"gender", "fatal-(y/n)":"fatal"})
    
    # 2. Specific cleaning
    ##YEAR column
    df.year.fillna(0, inplace=True) 
    df.year = df["year"] = [int(i) for i in df.year]
    ##GENDER column
    df.gender.fillna("Unidentified", inplace=True) 
    df.gender.replace({"M ": "Male", "lli":"Unidentified", ".":"Unidentified", "N":"Unidentified", "M":"Male", "F":"Female"}, inplace=True)
    # #FATAL column and NUMBER OF DEATHS
    df.fatal.fillna("UNKNOWN", inplace=True)
    df.fatal.replace({" N" : "Non Fatal", "N ":"Non Fatal", "2017":"UNKNOWN", "M":"UNKNOWN", "y": "Fatal", "Y": "Fatal", "N":"Non Fatal"}, inplace=True)
    df.at[76,"fatal"] = "Fatal"
    conta = {"Fatal": 1}
    df['number_deaths'] = df['fatal'].map(conta).fillna(0)

    ##COUNTRY and ADD CONTINENT
    df.country.fillna("UNKNOWN", inplace=True)

    continent_dict = {'AFRICA': ['SOUTH AFRICA', 'LIBYA', 'COMOROS', 'REUNION', 'SENEGAL', 'Sierra Leone', 'SIERRA LEONE', 'LIBERIA', 'ANGOLA', 'NAMIBIA', 'GABON', 'MAYOTTE','DJIBOUTI', 'SUDAN?', 'GUINEA', 'EQUATORIAL GUINEA / CAMEROON', 'GHANA','MOZAMBIQUE','CAPE VERDE'],
    'ASIA': ['THAILAND', 'MALAYSIA', 'JAPAN', 'CHINA', 'TAIWAN', 'PALESTINIAN TERRITORIES', 'PHILIPPINES', 'INDONESIA', 'ISRAEL', 'VIETNAM', 'INDIA', 'BANGLADESH', 'ANDAMAN / NICOBAR ISLANDAS', 'JAVA' , 'CENTRAL PACIFIC', 'SOUTHWEST PACIFIC OCEAN', 'BAY OF BENGAL', 'LEBANON', 'GEORGIA', 'SYRIA', 'TUVALU', 'INDIAN OCEAN?', 'ANDAMAN ISLANDS', 'KOREA', 'ASIA?','CEYLON'],
    'OCEANIA': ['FRENCH POLYNESIA','AUSTRALIA', 'NEW CALEDONIA', 'NEW ZEALAND', 'FIJI', 'VANUATU', 'NEW GUINEA', 'COOK ISLANDS','MALDIVES', 'SAMOA', 'SOLOMON ISLANDS', 'TONGA', 'MARSHALL ISLANDS', 'WESTERN SAMOA', 'PACIFIC OCEAN ', 'PACIFIC OCEAN', 'ADMIRALTY ISLANDS', 'PERSIAN GULF', 'RED SEA / INDIAN OCEAN', 'NORTH SEA', 'MALDIVE ISLANDS', 'AMERICAN SAMOA', 'BRITISH ISLES', 'SOUTH PACIFIC OCEAN'],
    'EUROPE': ['ENGLAND', 'SPAIN', 'FRANCE', 'ITALY', 'GREECE', 'AZORES', 'MALTA', 'RUSSIA', 'CROATIA', 'PORTUGAL', 'SLOVENIA', 'MONACO', 'IRELAND', 'SWEDEN', 'Between PORTUGAL & INDIA','SLOVENIA','CYPRUS'],
    'NORTH AMERICA': ['USA', 'MEXICO', 'CANADA'],
    'SOUTH AMERICA': ['BRAZIL', 'ECUADOR', 'COLUMBIA', 'NICARAGUA', 'CHILE', 'URUGUAY', 'ARGENTINA', 'PERU', 'FALKLAND ISLANDS', 'PARAGUAY'],
    'CENTRAL AMERICA':['GRENADA','COSTA RICA', 'BAHAMAS', 'CUBA', 'DOMINICAN REPUBLIC', 'CAYMAN ISLANDS', 'ARUBA','PUERTO RICO', 'TRINIDAD & TOBAGO', 'ST. MARTIN', 'JAMAICA', 'BELIZE','TURKS & CAICOS', 'BERMUDA', 'NETHERLANDS ANTILLES', 'NORTHERN MARIANA ISLANDS', 'CURACAO', 'BARBADOS','BRITISH WEST INDIES']
}
    d = {k: oldk for oldk, oldv in continent_dict.items() for k in oldv}

    df['continent'] = df['country'].map(d)

    ##SPECIES colum and stardadization of species
    df["species"] = df["species"].fillna("Unidentified")
    df["species"] = df["species"].replace(r"\dm?'?\sto\s\d", "unidentified", regex=True)
    df["species"] = df["species"].replace(r"\d\s?['.m?]\d?\sm?", "unidentified", regex=True)
    df["species"] = df["species"].replace(r'\d+"?-?[lb]?', "unidentified", regex=True)

    shark_types = {"white": "White Shark", "unidentified": "Unidentified","small shark":"Unidentified", "tiger": "Tiger Shark", "bull": "Bull Shark", "dusky":"Dusky Shark",
               "blue": "Blue Shark", "nurse":"Nurse Shark", "blacktip":"Blacktip Shark", "wobbegong" : "Wobbegong Shark", "hammerhead":"Hammerhead Shark", "dog":"Dogfish Shark",
               "bronze":"Bronze Whaler Shark","whaler":"Bronze Whaler Shark", "mako":"Mako Shark", "spinner":"Spinner Shark", "lemon":"Lemon Shark", "Unknown":"Unidentified",
               "raggedtooth":"Raggedtooth Shark", "reef":"Caribbean reef Shark", "sand":"Nurse Shark","sevengill":"Broadnose Sevengill Shark", "C. macrurus":"Dusky Shark",
               "broadnose":"Broadnose Sevengill Shark","7-gill":"Broadnose Sevengill Shark", "zambesi":"Bull Shark", "porbeagle":" SharkPorbeagle","carpet":"Carpet Shark","sharks":"Unidentified",
               "doubtful":"Shark involvement doubtful", "not confirmed":"Shark involvement not confirmed", "shovelnose":"No shark involved", "questionable":"Shark involvement doubtful"}

    search_dict = {k.lower(): v for k, v in shark_types.items()}
    df["species"] = df["species"].map(lambda x: search_dict.get(next((i for i in search_dict if i in str(x).lower()), x), x))

    ## TIME
    df.time.fillna("00", inplace=True)
    df.time.replace({"Late Afternoon":"Afternoon","Late afternoon":"Afternoon","Early afternoon":"Afternoon", "Late afternon":"Afternoon", '"Early evening"':"Evening","Late morning":"Morning","Late night":"Night" }, inplace=True)
    df["time"] = [i[:3] for i in df["time"] ]
    df.time.replace({"Nig": "Night","nig": "Night","02h": "Night","00": "UNKOWN","01h": "Night","00h": "Night","Aft": "Afternoon","Noo": "Afternoon", "Mid":"Night",
            "23h":"Night","22h": "Night","21h": "Night","Eve": "Evening",'"Ev': "Evening","20h": "Evening","19h": "Evening","18h": "Evening","17h": "Afternoon","16h": "Afternoon",
            "15h": "Afternoon","14h": "Afternoon",'"Af': "Afternoon","13h": "Afternoon", "12h":"Afternoon", "11h":"Morning", "10h":"Morning","Dus":"Evening",
            "09h":"Morning", "08h":"Morning", "07h":"Morning","06h":"Morning","Mor":"Morning","05h":"Morning", "04h":"Night", "03h":"Night"}, inplace=True)
    def clean_time(x):
        '''
        Function to clean the rest of the inconsistent values
        args: info from column time 
        returns UNKOWN if info is not in the presset list of times
        '''
        times = ["Evening","Afternoon","Morning","Night"]
        if x not in times:
            return "UNKOWN"
        else:
            return x
    
    df["time"] = df["time"].apply(clean_time)
    
    # 3. Export and read
    df.to_csv("data/jaws_clean.csv", index=False)
    jaws = pd.read_csv("data/jaws_clean.csv")
    return jaws