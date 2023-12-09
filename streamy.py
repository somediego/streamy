import click
import json
import os  # os.path.isfile()
import subprocess	# to execute bash commands
#import pkg_resources  # part of setuptools # version = pkg_resources.require("MyProject")[0].version

import requests
import pandas as pd
import numpy as np
#from sqlalchemy import create_engine

#import clickhouse_connect


#import pandas_gbq
#import datetime
#from datetime import timedelta

import streamlit as st
import time

st.markdown("""
	# Main
	Left panel to choose different options.
	"""
)
st.sidebar.markdown('# Main')

# Initialize connection.
conn = st.connection("postgresql", type="sql")

@st.cache_data
def update_value():
 # Perform query.
 st.write('Total points per player')
 st.session_state.df1= conn.query('SELECT * FROM src_stream.total;', ttl="10m")
 st.write(st.session_state.df1)
 st.write('Points per player')
 st.session_state.df2 = conn.query('SELECT * FROM src_stream.points;', ttl="10m")
 st.write(st.session_state.df2)
 st.write('Race results')
 st.session_state.df3 = conn.query(f"SELECT * FROM src_stream.results where win is not null order by id;", ttl="10m")
 st.write(st.session_state.df3)
 st.write('Race bets')
 st.session_state.df4 = conn.query(f"SELECT id, race, bettor, alo, sai, win, cal FROM src_stream.bets order by id;", ttl="10m")
 st.write(st.session_state.df4)

# execute
#update_value()

##### Option using a callback #####
#st.header(st.session_state.df1)
#st.header(st.session_state.df2)
#st.header(st.session_state.df3)
#st.header(st.session_state.df4)

if st.button("Clear cache_data"):
#  update_value.clear()
  st.cache_data.clear()

update_value()
