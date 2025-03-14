Title: NYC, Airbnb, Data Sharing Law, Short-Term Rental Registration Law

Project Overview

For years, New York City and Airbnb have battled over the legality of short-term rentals. NYC is one of the top tourist destinations worldwide, making short-term rentals in the city a profitable commodity for Airbnb. However, city officials have long suspected that many Airbnb short-term rentals are illegal. By law, individuals cannot rent out an entire house or apartment to a visitor for less than 30 days. If a host is renting out a room in their home for less than 30 days, they must also be living in the unit. 

In 2018, NYC passed a mandatory data sharing law, Local Law 146, requiring Airbnb and similar companies to provide city officials with information on every short-term listing (less than 30 days) in NYC, including hosts’ addresses and identities, in order to crack down on those that violate New York’s short-term rental laws. In response, Airbnb filed a lawsuit against the city, claiming that the data sharing law violated the hosts’ Fourth Amendment right against illegal searches. In June 2020, Airbnb dismissed the lawsuit and the data sharing law went into effect in December 2020.

On September 5th of 2023, the short-term rental registration law, Local Law 18, went into effect and mandated that all hosts offering short-term rentals for less than 30 days must register with the city. This reinforces existing laws and prohibits individuals from renting out an entire home or apartment unless they are physically present for their guests' stay and provide full access to the property.

The goal of the project is to show how NYC’s data sharing law and short-term rental registration law has directly impacted short-term Airbnb rentals of entire apartments and homes in the city. The Airbnb listing data is publicly available thanks to Inside Airbnb (http://insideairbnb.com/). A previous version of the project visualized the distribution of short-term rentals in wake of the data sharing law; however, that data from 2018 has since been archived by Inside Airbnb. This version of the project utilizes currently available data to visualize the distribution of NYC Airbnb short-term rentals in the year following the implementation of Local Law 18.

Using Streamlit and Pydeck, I mapped the distribution of short-term Airbnb rentals of entire homes and apartments in NYC from February 2024 to Janaury 2025. The height and color of the columns correspond to the price of the listing.

Data

The datasets come as csvs of Airbnb listings on a monthly basis, with the following columns:
id: Unique identification code for the listing
name: Descriptive name of the listing
host_id: Unique identification code for the host
host_name: First name of the host
neighbourhood_group: Neighbourhoods are grouped into NYC boroughs
neighbourhood: The name of neighbourhood of the listing
latitude: A numeric variable that combining the longitude to represent the location of the listing
longitude: A numeric variable that combining the latitude to represent the location of the listing
room_type: A categorical variable including Shared Room, Private Room or Entire Room/Apt
price: The price of the listing
minimum_nights: The minimum number of nights the host requires to book their property
number_of_reviews: Number of customer reviews regarding the listing
last_review: Date of the last review
reviews_per_month: Number of customer reviews per month
calculated_host_listings_count: Number of listings each host has simultaneously
availability_365: The number of days that the listing is available in 365 days, which is pre-defined by the host

Code Design

	vis.py - loads and visualizes data

	data.py - processes data 

	plot.py - plots data

Libraries

In my code, I used Pandas, Pydeck, Streamlit, datetime, dateutil.

Installation Instructions
1. Download vis.py, data.py, and plot.py. 
2. Install pydeck (https://deckgl.readthedocs.io/en/latest/installation.html) and streamlit (https://docs.streamlit.io/en/stable/). 
3. Obtain Mapbox API Key (https://account.mapbox.com/).
4. Run the project with streamlit run vis.py

Contact Information
Reach me at melguo236@gmail.com

