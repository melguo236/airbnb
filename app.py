"""
File: nyc_airbnb.py
---------------
Names: <Mel Guo>

Interactive map visualizing the change in NYC Airbnbs in light of Local Law 18.
"""

import pandas as pd
import os
import pydeck as pdk
import streamlit as st
import data
import plot
import datetime
from dateutil.parser import parse
import re

# Project Blurb
st.title('Airbnb and NYC Data Sharing Law')
st.write('For years, New York City and Airbnb have battled over the legality of short-term rentals. NYC is one of the top tourist destinations worldwide, making short-term rentals in the city a profitable commodity for Airbnb. However, city officials have long suspected that many Airbnb short-term rentals are illegal. By law, it is illegal to rent out an entire house or apartment to a visitor for less than 30 days. If a host is renting out a room in their home for less than 30 days, they must also be living in the unit.')
st.write('In 2018, NYC passed a mandatory data sharing law, Local Law 146, requiring Airbnb and similar companies to provide city officials with information on every short-term listing (less than 30 days) in NYC, including hosts’ addresses and identities, in order to crack down on those that violate New York’s short-term rental laws. In response, Airbnb filed a lawsuit against the city, claiming that the data sharing law violated the hosts’ Fourth Amendment right against illegal searches. In June 2020, Airbnb dismissed the lawsuit and the data sharing law went into effect in December 2020. On September 5th of 2023, the short-term rental registration law, Local Law 18, went into effect and mandated that all hosts offering short-term rentals for less than 30 days must register with the city. This reinforces existing laws and prohibits individuals from renting out an entire home or apartment unless they are physically present and provide full access to the property. The goal of the project is to show how NYC’s data sharing law and short-term rental registration law has directly impacted short-term Airbnb rentals of entire apartments and homes in the city. This work is made possible by data from Inside Airbnb. A previous version of the project visualized the distribution of short-term rentals in wake of the data sharing law; however, that data from 2018 has since been archived by Inside Airbnb. This version of the project utilizes currently available data to visualize the distribution of NYC Airbnb short-term rentals in the year following the implementation of Local Law 18.')


st.sidebar.markdown(
    "Data source: [Inside Airbnb](http://insideairbnb.com), "
    "licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)."
)

# Function to extract the date from the filename
def extract_date_from_filename(filename):
    match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)  # Looks for YYYY-MM-DD pattern
    if match:
        return parse(match.group(1))  # Convert string to datetime object
    else:
        raise ValueError(f"Could not extract date from filename: {filename}")
	
	
# Load Data

#@st.cache
def load_data(nrows):
	
	folder_path = "nyc-listings-data"  # Define the folder containing the files
	all_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]  # Get all CSV files

	dfs = []

	# Read files into dataframes, process data, and combine dataframes into a single dataframe containing multiple months of data

	for filename in all_files:
		#date = parse(filename, fuzzy_with_tokens = True)
		print(f"Loading file: {filename}")  # Debugging output
	
		date = extract_date_from_filename(filename)  # Extract the date
		month_num = date.month  # Get the month number

		df = pd.read_csv(filename) 
		df_1 = data.only_str_entire_apt(df)
		#df_2 = data_revised.add_month_col(df_1, date[0].month)	
		df_2 = data.add_month_col(df_1, month_num)	
		df_3 = data.price_color(df_2)
		df_4 = data.reduce(df_3)
		dfs.append(df_4)

	if dfs:
		multidf = pd.concat(dfs, ignore_index=True)
	else:
		multidf = pd.DataFrame()  # Return empty DataFrame if no files loaded

	return multidf

def main():

	loaded_df = load_data(500)
 
	st.subheader('Map of Short-term NYC Airbnbs of Entire Homes/Apartments')

	# Select month and year to view on map
	option = st.select_slider('Month and Year', ['February 2024', 'March 2024', 'April 2024', 'May 2024', 'June 2024', 
     'July 2024', 'August 2024', 'September 2024', 'October 2024', 'November 2024', 'December 2024', 'January 2025'], value = 'February 2024')

	# Get numerical month of chosen month and yeaar from slider
	date = parse(option, fuzzy_with_tokens = True)
	month_num = date[0].month

	## MAP
	plot.set_view()

	# Load data of selected month and year into a dataframe
	current_df = data.get_month_data(loaded_df, month_num)

	# Create a pydeck map based on selected month and year
	r = plot.create_map(current_df, month_num)

	# Render the deck.gl map in the Streamlit app as a Pydeck chart based on slider option
	st.pydeck_chart(r)

	# Map Blurb
	st.write('Map shows the monthly distribution of NYC Airbnb short-term rentals of entire homes and apartments between February 2024 and January 2025. Height of bars indicates price level of each Airbnb unit.')


if __name__ == '__main__':
		main()


