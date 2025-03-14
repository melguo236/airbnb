"""
File: plot.py
---------------
Names: <Mel Guo>

Plots map visualization using Pydeck library.
"""

import pandas as pd
import os
import pydeck as pdk

# Set viewport for the deckgl map
def set_view():
	return pdk.ViewState(
		latitude=40.7128,
	  	longitude=-74.0060,
	  	zoom=12,
	  	max_zoom=16,
	  	pitch=75,
	  	bearing=60
	)

# Create layer
def create_layer(df, month):
	layer = pdk.Layer(
		'ColumnLayer',
		data=df[df['month'] == month],
		get_position=['longitude', 'latitude'],
	    get_elevation='price',
	    elevation_scale=0.6,
	    radius=38,
	    pickable=True,
	    get_fill_color='[255, price_color*255, 255]',
	    elevation_range=[0, 3000],
	    auto_highlight=True,
	)
	return layer

# Create deckgl map
def create_map(df, month):
	token = 'pk.eyJ1IjoibWVsZ3VvIiwiYSI6ImNrcm1ocXI4MzFqeW8ydW1sZzJteGU1M3MifQ.aQ8sFMFX7P9LYVjQm4t30Q'
	r = pdk.Deck(map_style='mapbox://styles/mapbox/light-v9',
	initial_view_state=set_view(),
	layers=[create_layer(df, month)])
	return r