#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Task 1: Data Preparation
import pandas as pd
import numpy as np


sw_df = pd.read_csv('StarWars.csv', sep = ',', decimal='.', encoding='ISO-8859-1', skiprows=[1])
                    

sw_df.shape
sw_df.head()



# #  1.2 Checking data types

# In[3]:


sw_df.dtypes # Checking data types


# # Extra White Spaces

# In[4]:


# Extra Whitespace
print(sw_df['Have you seen any of the 6 films in the Star Wars franchise?'].str.isspace())
print(sw_df['Have you seen any of the 6 films in the Star Wars franchise?'].value_counts())
sw_df['Have you seen any of the 6 films in the Star Wars franchise?'] =  sw_df['Have you seen any of the 6 films in the Star Wars franchise?'].str.strip()
print(sw_df['Have you seen any of the 6 films in the Star Wars franchise?'].value_counts())


# # Typos

# In[5]:


sw_df['Have you seen any of the 6 films in the Star Wars franchise?'].unique() # No typo


# In[6]:


sw_df['Do you consider yourself to be a fan of the Star Wars film franchise?'].unique() # typo2 


# In[7]:


sw_df = sw_df.mask(sw_df['Do you consider yourself to be a fan of the Star Wars film franchise?'] == 'Yess', other = 'Yes')
sw_df = sw_df.mask(sw_df['Do you consider yourself to be a fan of the Star Wars film franchise?'] == 'Noo', other = 'No')

print(sw_df['Do you consider yourself to be a fan of the Star Wars film franchise?'].value_counts())


# In[8]:


sw_df['Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.'].unique() # No typos 
       


# In[9]:


sw_df['Do you consider yourself to be a fan of the Expanded Universe?æ'].unique() # typos 3


# In[10]:


mask3 = sw_df['Do you consider yourself to be a fan of the Expanded Universe?æ'].map({'Yes':True,'No':False}) #== 1
mask3 == 1


# In[11]:


mask3.unique()


# In[12]:


sw_df['Do you consider yourself to be a fan of the Star Trek franchise?'].unique() # typos 4


# In[13]:


mask4 = sw_df['Do you consider yourself to be a fan of the Star Trek franchise?'].map({'Yes':True,'No':False})
mask4 == 1


# In[14]:


mask4.unique()


# In[15]:


sw_df['Gender'].unique() # typos 5


# In[16]:


sw_df = sw_df.mask(sw_df['Gender'] == 'F', other = 'Female')
sw_df = sw_df.mask(sw_df['Gender'] == 'female', other = 'Female')
sw_df = sw_df.mask(sw_df['Gender'] == 'male', other = 'Male')
sw_df = sw_df.mask(sw_df['Gender'] == 'Yes', other = 'Male')
sw_df = sw_df.mask(sw_df['Gender'] == 'No', other = 'Female')
print(sw_df['Gender'].value_counts())


# In[17]:


sw_df['Education'].unique() # notypos


# In[18]:


sw_df['Location (Census Region)'].unique() # notypos


# # Upper case

# In[19]:


sw_df.apply(lambda x: x.astype(str).str.upper()) # converting to upper case


# # Sanity Checks

# In[20]:


sw_df['Age'].unique()


# In[21]:


print(sw_df['Age'].value_counts())


# In[22]:


sw_df = sw_df[(sw_df.Age>='18-29') & (sw_df.Age <= '> 60') & (sw_df.Age != '500')]


# In[23]:


print(sw_df['Age'].value_counts())


# # Missing values

# In[24]:


sw_df.isnull().sum()


# In[25]:


## Missing Values
## Removing the nan in 'respondent ID' variable since it is having unique values. We only need rows in which 'respondent ID' is not null
sw_df = sw_df[pd.notnull(sw_df['Have you seen any of the 6 films in the Star Wars franchise?'])]
sw_df = sw_df[pd.notnull(sw_df['Do you consider yourself to be a fan of the Star Wars film franchise?'])]
sw_df = sw_df[pd.notnull(sw_df['Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 11'])]
sw_df = sw_df[pd.notnull(sw_df['Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 16'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 17'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 18'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 19'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 20'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 21'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 22'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 23'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 24'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 25'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 26'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 27'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 28'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 4'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 5'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 6'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 7'])]
sw_df = sw_df[pd.notnull(sw_df['Unnamed: 8'])]
sw_df = sw_df[pd.notnull(sw_df['Which of the following Star Wars films have you seen? Please select all that apply.'])]

sw_df = sw_df[pd.notnull(sw_df['Do you consider yourself to be a fan of the Expanded Universe?æ'])]
sw_df = sw_df[pd.notnull(sw_df['Household Income'])]
sw_df = sw_df[pd.notnull(sw_df['Education'])]
sw_df = sw_df[pd.notnull(sw_df['Location (Census Region)'])]


# In[26]:


#imputing categorical Feature
for column in ['Gender', 'Household Income', 'Education', 'Location (Census Region)']:
    sw_df[column].fillna(sw_df[column].mode()[0], inplace=True)


# In[27]:


sw_df.isnull().sum()


# # 2.1 Explore a survey question

# In[28]:


# 1. Explore the survey question: \textit{Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.	(Star Wars: Episode I  The Phantom Menace; Star Wars: Episode II  Attack of the Clones; Star Wars: Episode III  Revenge of the Sith;	Star Wars: Episode IV  A New Hope; Star Wars: Episode V The Empire Strikes Back; Star Wars: Episode VI Return of the Jedi)}, then analysis how people rate Star Wars Movies. 


# In[29]:


## converting the ranking columns from string type to float type
sw_df[sw_df.columns[9:15]] = sw_df[sw_df.columns[9:15]].astype(float)


# In[30]:



## renaming the ranking columns
sw_df_ranking={
    'Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.': 'Rank_1',
    'Unnamed: 10' : 'Rank_2',
    'Unnamed: 11' : 'Rank_3',
    'Unnamed: 12' : 'Rank_4',
    'Unnamed: 13' : 'Rank_5',
    'Unnamed: 14' : 'Rank_6'
    
}

sw_df.rename(columns=sw_df_ranking, inplace=True)
sw_df[sw_df.columns[9:15]].head()


# In[31]:


import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
sw_de1 = sw_df[sw_df.columns[9:15]].mean().plot(kind = 'bar')
sw_de1.set_xticklabels(['Episode I The Phantom Menace','Star Wars: Episode II Attack of the Clones','Star Wars: Episode III Revenge of the Sith','Star Wars: Episode IV A New Hope','Star Wars: Episode V The Empire Strikes Back',
                'Star Wars: Episode VI Return of the Jedi'])


# We can Depict that Star wars V is most popular movie as we know least being the favourite in this survey.

# # 2.2 Relationships between columns

# In[32]:


# Task 2: Data Exploration
# 2. Explore the relationships between columns; at least 3 visualisations with plausible hypothesis


# In[33]:


#  Males had seen more Star wars movies than Females

sw_df.groupby(['Gender', 'Have you seen any of the 6 films in the Star Wars franchise?']).size().unstack().plot(kind='bar',stacked=True)


# In[34]:


rank_by_age = sw_df.groupby("Age")["Rank_5"].count()
rank_by_age.head()
rank_by_age.plot.bar()

# if we look at the highest ranked movie and age of the respondents, we can interpret that youth between age of 18-29 loves the franshise and has probably voted for that


# In[35]:


## relaton between age and movies seen by them

## the columns 3:9 have been changed to make the data simple
schema1 = {
  'Star Wars: Episode I  The Phantom Menace': True,
  'Star Wars: Episode II  Attack of the Clones': True,
  'Star Wars: Episode III  Revenge of the Sith': True,
  'Star Wars: Episode IV  A New Hope': True,
  'Star Wars: Episode V The Empire Strikes Back': True,
  'Star Wars: Episode VI Return of the Jedi': True,
  True: True,
  False: False,
  np.nan: False
 }

sw_df[sw_df.columns[3:9]] = sw_df[sw_df.columns[3:9]].apply(lambda col: col.map(schema1) , axis = 0)
sw_df[sw_df.columns[3:9]].head()
## renaming the six columns
seen_col={
  'Which of the following Star Wars films have you seen? Please select all that apply.': 'seen1',
  'Unnamed: 4': 'seen2',
  'Unnamed: 5': 'seen3',
  'Unnamed: 6': 'seen4',
  'Unnamed: 7': 'seen5',
  'Unnamed: 8': 'seen6'
}
sw_df.rename(columns=seen_col, inplace=True)
sw_df[sw_df.columns[3:9]].head()


# In[36]:


eighteen_to_twentynine = sw_df[sw_df["Age"] == "18-29"]
thirty_to_fortyfour= sw_df[sw_df["Age"] == "30-44" ]
fortyfive_to_sixty = sw_df[sw_df["Age"] == "45-60" ]
above_sixty = sw_df[sw_df["Age"] == "> 60" ]


# In[37]:


age_seen = pd.DataFrame({'eighteen_to_twentynine':eighteen_to_twentynine[eighteen_to_twentynine.columns[3:9]].sum(),
                              'thirty_to_fortyfour':thirty_to_fortyfour[thirty_to_fortyfour.columns[3:9]].sum(),
                              'fortyfive_to_sixty':fortyfive_to_sixty[fortyfive_to_sixty.columns[3:9]].sum(),
                              'above_sixty':above_sixty[above_sixty.columns[3:9]].sum()})

fig = plt.figure(figsize=(10, 5))
s_age = fig.add_subplot(1, 2, 2)
s_age = age_seen.plot(kind = 'bar' ,ax=s_age)
s_age.set_xticklabels(['Episode I The Phantom Menace','Star Wars: Episode II Attack of the Clones','Star Wars: Episode III Revenge of the Sith','Star Wars: Episode IV A New Hope','Star Wars: Episode V The Empire Strikes Back',
                'Star Wars: Episode VI Return of the Jedi'])


# In[38]:


# relation between gender and movie ranking

males = sw_df[sw_df["Gender"] == "Male"]
females = sw_df[sw_df["Gender"] == "Female" ]

gender_ranking = pd.DataFrame({'females':females[females.columns[9:15]].mean(),'males':males[males.columns[9:15]].mean(),})
print(gender_ranking)


fig = plt.figure(figsize=(15, 5))
s1 = fig.add_subplot(1, 2, 1)
s1 = gender_ranking.plot(kind = 'bar' ,ax=s1)
s1.set_xticklabels(['Episode I The Phantom Menace','Star Wars: Episode II Attack of the Clones','Star Wars: Episode III Revenge of the Sith','Star Wars: Episode IV A New Hope','Star Wars: Episode V The Empire Strikes Back',
                'Star Wars: Episode VI Return of the Jedi'])


# In[39]:


## relation between fans and Education
fan = sw_df[sw_df["Do you consider yourself to be a fan of the Star Wars film franchise?"] == 'Yes']
no_fan= sw_df[sw_df["Do you consider yourself to be a fan of the Star Wars film franchise?"] == 'No']
sw_df["Education"].value_counts()

fans_education = pd.DataFrame({'fans':fan[fan.columns[36]].value_counts(),
                              'not_fans':no_fan[no_fan.columns[36]].value_counts()})

fig3 = plt.figure(figsize=(15, 5))
s3 = fig3.add_subplot(1, 2, 2)
s3 = fans_education.plot(kind = 'bar' ,ax=s3)
s3.set_xticklabels(['Bachelor Degree','Graduate Degree','High school Degree','Less than high school','Some College',
                ])

# Task 2: Data Exploration

sw_df2={
    'Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.': 'view towards Han Solo',
    'Unnamed: 16' : 'view towards Luke Skywalker',
    'Unnamed: 17' : 'view towards Princess Leia Organa',
    'Unnamed: 18' : 'view towards Anakin Skywalker',
    'Unnamed: 19' : 'view towards Obi Wan Kenobi',
    'Unnamed: 20' : 'view towards Emperor Palpatine',
    'Unnamed: 21' : 'view towards Darth Vader',
    'Unnamed: 22' : 'view towards Lando Calrissian',
    'Unnamed: 23' : 'view towards Boba Fett', 
    'Unnamed: 24' : 'view towards C-3P0',
    'Unnamed: 25' : 'view towards R2 D2',
    'Unnamed: 26' : 'view towards Jar Jar Binks',
    'Unnamed: 27' : 'view towards Padme Amidala',
    'Unnamed: 28' : 'view towards Yoda',
}

sw_df.rename(columns=sw_df2, inplace=True)


# In[44]:


fav_char = {'Very favorably':1,'Somewhat favorably':2,
            'Neither favorably nor unfavorably (neutral)': 3,
            'Unfamiliar (N/A)':4,
             'Somewhat unfavorably': 5,
             'Very unfavorably': 6}


# In[45]:


for i in list(range(15,29)):
    sw_df.iloc[:, i] = sw_df.iloc[:,i].map(fav_char)


# In[46]:


sw_df.iloc[:,15:29].mean().plot.bar()


# In[47]:


sw_df.iloc[:,15:29].mean().sort_values() # we will explore han solo and yoda


# In[48]:


sw_df.groupby('Age')['view towards Han Solo'].count().plot(kind='bar') # Relation between Age and atitute towards han solo


# In[49]:


sw_df.groupby('Gender')['view towards Yoda'].count().plot(kind='bar')# Relation between gender and atitute towards Yoda


# In[50]:


sw_df.groupby('Education')['view towards Han Solo'].count().plot(kind='bar') #Relation between Education and atitute towards han solo


# In[51]:


sw_df.groupby('Household Income')['view towards Han Solo'].count().plot(kind='bar') #Relation between income and atitute towards han solo


# In[52]:


sw_df.groupby('Location (Census Region)')['view towards Han Solo'].count().plot(kind='bar')
 #Relation between Location and atitute towards han solo

