import pandas as pd
import numpy as np


# for each description of a bank transaction
# it checks if it is described by an existing label
# if the bank transaction is described by an existing label, it returns the labels
# if it is described by more than one label, it returns "We fucked up"
# if it is described by no labels, it returns "input needed"
def catagorize(company,catagories_for_mapping):
    if(isinstance(company,float)):
        print(company)
    catagory_list = []
    for row in catagories_for_mapping.itertuples():

        if row.Store in company:
            catagory_list.append(row.Category)
    if len(catagory_list)>1:
        return "Duplicate"
    if len(catagory_list)==0:
        return "input needed"
    return catagory_list[0]
def problematic(string):
    if string == "Duplicate" or string == "input needed":
        return False
    return True
def produce(df,labels):
    for i in range(0,len(df["company"])):
        if isinstance(df["Category"][i],float) or df["Category"][i] == 'input needed' or df["Category"][i] == 'Duplicate':
            df["Category"][i]=catagorize(df["company"][i],labels)
    efficent = pd.DataFrame({'company': df[df["Category"]=='input needed']["company"]})
    labels = pd.concat([labels,efficent], ignore_index=True,sort=False)
    df["sortable"] = df.Category.apply(problematic)
    df=df.sort_values(by="sortable").drop(columns="sortable").reindex()
    return df,labels
def getmonth(date):
    if type(date)==str:
        return int(date.split('/')[0])
    else:
        return date.month
def getyear(date):
    if type(date)==str:
        return int(date.split('/')[2])
    else:
        return date.year
def getday(date):
    if type(date)==str:
        return int(date.split('/')[1])
    else:
        return date.day

def make_pivot(df):
    df["year"]=df.date.apply(getyear)
    df["month"]=df.date.apply(getmonth)
    df["day"]=df.date.apply(getday)


    return pd.pivot_table(df, values='ammount', index=['year', 'month'], columns=['Category'], aggfunc=np.sum, margins=True)
