import pandas as pd 
import sqlite3
import numpy as np
import math
# from openpyxl.workbook import Workbook

file_name = "store.db"

# con = sqlite3.connect(file_name)
# df = pd.read_sql_query("SELECT * from inputs", con)

# df['w'] = df.production_rate.astype(float) * df.distance.astype(float) * 0.3048
def calculate():
	con = sqlite3.connect(file_name)
	df = pd.read_sql_query("SELECT * from inputs", con)
	df['w'] = df.production_rate * df.distance * 0.3048
	U = df.production_rate.sum()
	d = df.w.sum()/U
	d_dot = d
	t = 2
	v = 42
	f = 0.85
	NumOfRobot = ((d/v+t)*U + ((d_dot/v)*U))/(60*f)
	Efficientcy = ((d/v)*U/((d/v+t)*U+(d_dot/v)*U))*f
	result = round(NumOfRobot,3)
	# print(result)
	result_round_up = math.ceil(NumOfRobot)
# print(result_round_up)

def display_result():
	con = sqlite3.connect(file_name)
	df = pd.read_sql_query("SELECT * from inputs", con)
	df['w'] = df.production_rate * df.distance * 0.3048
	U = df.production_rate.sum()
	d = df.w.sum()/U
	d_dot = d
	t = 2
	v = 42
	f = 0.85
	NumOfRobot = ((d/v+t)*U + ((d_dot/v)*U))/(60*f)
	Efficientcy = ((d/v)*U/((d/v+t)*U+(d_dot/v)*U))*f
	result = round(NumOfRobot,2)
	# print(result)
	result_round_up = math.ceil(NumOfRobot)
	return result

def display_result_ru():
	con = sqlite3.connect(file_name)
	df = pd.read_sql_query("SELECT * from inputs", con)
	df['w'] = df.production_rate * df.distance * 0.3048
	U = df.production_rate.sum()
	d = df.w.sum()/U
	d_dot = d
	t = 2
	v = 42
	f = 0.85
	NumOfRobot = ((d/v+t)*U + ((d_dot/v)*U))/(60*f)
	Efficientcy = ((d/v)*U/((d/v+t)*U+(d_dot/v)*U))*f
	result = round(NumOfRobot,3)
	# print(result)
	result_round_up = math.ceil(NumOfRobot) 
	return result_round_up
# print(df.w)

#####################################
