import pandas as pd
import numpy as np

import streamlit as st
import time

from globals import var_names
# get class
v1= var_names()


st.markdown('# Add_results')
st.sidebar.markdown('# Add_results')

# Initialize connection.
conn = st.connection("postgresql", type="sql")

with st.form("my_results"):
     st.write("Just one result per week, or the whole system will break apart.")
     my_race = st.selectbox('Pick', v1.places)
     st.write("Write 0 if he is out.")
     my_alo = st.number_input('alo', value=1)
     my_sai = st.number_input('sai', value=1)
     sentence1 = st.selectbox('winner:', v1.pilots)
     #sentence2 = st.text_input('cal:', 'Where\'s the tuna?')
     sentence2 = st.selectbox('cali:', v1.pilots)

     if st.form_submit_button("Add the results!"):
       with conn.session as session:
         session.execute("UPDATE src_stream.results set race=:a, alo=:c, sai=:d, win=:e, cal=:f where race=:a;", {"a": my_race, "c": my_alo, "d": my_sai, "e": sentence1, "f": sentence2})
         session.commit()

       time.sleep(1.5)
       # Perform query.
       df = conn.query(f"SELECT * FROM src_stream.results where race='{my_race}';", ttl="10m")
       st.write(df)

# Perform query.
#df = conn.query('SELECT * FROM src_stream.results;', ttl="10m")
#
#st.data_editor(df)
## Print results.
##st.write(df)
#
#if st.submit_button("Add the results!"):
#       with conn.session as session:
#         session.execute("UPDATE src_stream.results VALUES (:a, :c, :d, :e, :f);", {"a": my_race, "c": my_alo, "d": my_sai, "e": sentence1, "f": sentence2})
#         session.commit()
#



#############################################
# update sqlite db using pandas and aggrid.
#############################################
#import streamlit as st
#import pandas as pd
#from st_aggrid import AgGrid
#from sqlalchemy import create_engine
#
#
#sqlfn = 'mydb.sqlite'
#table_name = 'users'
#engine = create_engine(f'sqlite:///{sqlfn}', echo=False)
#
#
#def add_data():
#    """Add sample data to sql table."""
#    df = pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3'],
#                       'role' : ['member', 'admin', 'moderator']})
#    try:
#        df.to_sql(table_name, con=engine, if_exists='fail')
#    except ValueError:
#        pass
#
#
#def edit_data(editable_df, label):
#    with st.expander(label):
#        with st.form('edit'):
#            grid_return = AgGrid(editable_df, editable=True, theme='streamlit')
#            new_df = grid_return['data']
#            st.form_submit_button('confirm', on_click=sent_to_db(new_df))
#
#
#def sent_to_db(new_df):
#    new_df.to_sql(name=table_name, con=engine, if_exists='replace')
#
#
#def sql_to_df():
#    df = pd.read_sql(table_name, con=engine)
#    df = df.drop(['index'], axis=1)
#    return df
#
#
#def main():
#    add_data()
#
#    df = sql_to_df()
#    st.dataframe(df)
#
#    editable_df = df.copy()
#    edit_data(editable_df, 'Edit')
#
#    updated_df = sql_to_df()
#    if not editable_df.equals(updated_df):
#        st.experimental_rerun()
#
#
#if __name__ == '__main__':
#    main()
