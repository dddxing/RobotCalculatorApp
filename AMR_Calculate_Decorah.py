#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd 
from openpyxl.workbook import Workbook
import matplotlib.pyplot as plt
import numpy as np


# In[14]:


############## Access Excel ##############
df = pd.read_excel('C:\\Users\\DXX0511A\\Desktop\\Automation\\Projects\\SEF\\Decorah\\AMR\\Data_Input_Decorah.xlsx')


# In[15]:


############## Input ##############
RobotSpeed_ms = 0.8			# unit in m/s
DropOffTime_s = 60			# unit in s
PlanningTime_s = 15			# unit in s
StopAndResumeTime_s = 10	# unit in s
NumberOfCrossSection = 0	# unitless
TrafficFactor = 0.85
ChargingFactor = 0.95


# In[16]:


df['CycleTime_min'] = (1 / df.ProductionRate) * 60
df['TotalTime_min'] = ((df.Distance_m / RobotSpeed_ms) * 2 + (DropOffTime_s + PlanningTime_s) * 2 + (NumberOfCrossSection * StopAndResumeTime_s)) / 60
df['NumberOfAMRRequired'] = df.TotalTime_min/(df.CycleTime_min * TrafficFactor * ChargingFactor)


# In[17]:


print(f" You will need {round(df.NumberOfAMRRequired.sum(),2)} robots")


# In[18]:


plt.bar(df.From, df.NumberOfAMRRequired)
plt.title("Work Load Requirement from Each Job")
plt.xlabel("Number of Robot Required")
plt.ylabel("Line Name")


# In[ ]:




