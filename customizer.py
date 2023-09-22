#%%
import pandas as pd
df = pd.read_csv("../data/actuals_and_forecasts.csv")
df.head()
# %%
new_dept =[
"Refrigerators",
"Washers",
"Dryers",
"Ranges",
"Microwaves",
"Wall Ovens",
"Dishwashers",
"Cooktops",
"Hoods",
"Freezers",

]
# %%
old_dept = df.dept_name.unique().tolist()

# a dict that maps old dept name to new dept name
dept_map = dict(zip(old_dept, new_dept))

# %%
#update the df such that old_dept is replaced by new_Dept
df.dept_name = df.dept_name.map(dept_map)
# %%
df.wk_date = pd.to_datetime(df.wk_date)
#extract unique years from df.wk_date
years = df.wk_date.dt.year.unique().tolist()
#a function to update 2010 to 2021, 2011 to 2022 and 2012 to 2023 based on the date supplied
def update_year(dt):
    year = dt.year
    if year == 2010:
        year = 2021
    elif year == 2011:
        year = 2022
    elif year == 2012:
        year = 2023
    new_date = dt.replace(year=year)
    return pd.to_datetime(new_date)

#apply the function on df
df['new_date'] = df.apply(lambda x: update_year(x.wk_date), axis=1)
# %%
#drop wk_date and rename new_date to wk_date
df.drop(columns=['wk_date'], inplace=True)
df.rename(columns={'new_date':'wk_date'}, inplace=True)

# %%
df.to_csv("../data/actuals_and_forecasts_whrl.csv", index=False)
# %%
