"""
File: data.py
---------------
Names: <Mel Guo>

Processes Airbnb listing data.
"""

import pandas as pd
import os
import re
import datetime
from dateutil.parser import parse

# Add a month column to dataframe
def add_month_col(df, month):

	df['month'] = month
	return df

# Returns a pared down dataframe of short-term listings of short-term listings of entire home/apartments
def only_str_entire_apt(df):

	# Get dataframe of short-term rentals (less than 30 days)
	df_str = df[df["minimum_nights"] < 30] 

	# Get dataframe of short-term rentals of entire homes/apartments
	df_str_entire_apt = df_str[df_str["room_type"] == "Entire home/apt"]

	return df_str_entire_apt

# Converts dataframe of select columns into list
def reduce(df):
	return df[['id', 'latitude', 'longitude', 'price', 'price_color', 'month']]

# Create color gradient based on price level
def price_color(df):
	price_categories = []

	for price_per_night in df['price']:
	    if price_per_night <= 85:
	        price_categories.append(0.1)
	    elif 85 < price_per_night <= 115:
	        price_categories.append(0.15)
	    elif 115 < price_per_night <= 150:
	        price_categories.append(0.3)
	    elif 150 < price_per_night <= 180:
	        price_categories.append(0.45)
	    elif 180 < price_per_night <= 235:
	        price_categories.append(0.6)
	    elif 235 < price_per_night <= 500:
	        price_categories.append(0.75)
	    elif 500 < price_per_night <= 1000:
	        price_categories.append(0.9)
	    else:
	        price_categories.append(1)

	df['price_color'] = price_categories
	return df

# Return dataframe of specific month's data from multimonth dataframe
def get_month_data(df, month_num):
	return df[df['month'] == month_num]

