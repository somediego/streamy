import streamlit as st
import time

from globals import var_names
# get class
v1= var_names()

st.markdown("""
	# Add_bet
	Left panel to choose different options.
	"""
)
st.sidebar.markdown('# Add_bet')

# Initialize connection.
conn = st.connection("postgresql", type="sql")

with st.form("my_form"):
     st.write("Just one bet per player and week, or the whole system will break apart.")
     my_race = st.selectbox('Pick', v1.places)
     my_selector = st.selectbox('Pick yourself', v1.players)
     st.write("Write 0 if you think he is out.")
     my_alo = st.number_input('alo', value=1)
     my_sai = st.number_input('sai', value=1)
     sentence1 = st.selectbox('Your winner:', v1.pilots)
     sentence2 = st.selectbox('Your cali:', v1.pilots)
     #sentence2 = st.text_input('Your cal:', 'Where\'s the tuna?')

     if st.form_submit_button("Add the results!"):
       with conn.session as session:
         session.execute("INSERT INTO src_stream.bets(race, bettor, alo, sai, win, cal) VALUES (:a, :b, :c, :d, :e, :f);", {"a": my_race, "b": my_selector, "c": my_alo, "d": my_sai, "e": sentence1, "f": sentence2})
         session.commit()

       time.sleep(1.5)
       # Perform query.
       df = conn.query('SELECT * FROM src_stream.bets order by id;', ttl="10m")
       st.write(df)

with st.form("my_deleted_bet"):
     st.write("""
	# To remove a bet
	By id.
	""")
     my_bet_number = st.number_input('bet_number', value=99, format='%i')

     if st.form_submit_button("Remove bet!"):
       with conn.session as session:
         session.execute("DELETE FROM src_stream.bets WHERE id=:a;", {"a": my_bet_number})
         session.commit()

       time.sleep(1.5)
       # Perform query.
       df = conn.query('SELECT * FROM src_stream.bets order by id;', ttl="10m")
       st.write(df)
