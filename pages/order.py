import streamlit as st

from globals import var_names
# get class
v1= var_names()

st.markdown("""
	# Order
	"""
)
st.sidebar.markdown('# Order')

#df = pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3'],
#                   'role' : ['member', 'admin', 'moderator']})
counter=1;
list_=[]
for i, x in enumerate(v1.places):
  if i % 3 == 0:
    list_.append([x, v1.players[1].title(), v1.players[2].title(), v1.players[0].title()])
  elif (i+1) % 3 == 0:
    list_.append([x, v1.players[2].title(), v1.players[0].title(), v1.players[1].title()])
  else :
    list_.append([x, v1.players[0].title(), v1.players[1].title(), v1.players[2].title()])

st.dataframe(list_)

## Initialize connection.
#conn = st.connection("postgresql", type="sql")
#
#with st.form("my_form"):
#     st.write("Just one bet per player and week, or the whole system will break apart.")
#     my_race = st.selectbox('Pick', v1.places)
#     my_selector = st.selectbox('Pick yourself', v1.players)
#     st.write("Write 0 if you think he is out.")
#     my_alo = st.number_input('alo', value=1)
#     my_sai = st.number_input('sai', value=1)
#     sentence1 = st.selectbox('Your winner:', v1.pilots)
#     sentence2 = st.selectbox('Your cali:', v1.pilots)
#     #sentence2 = st.text_input('Your cal:', 'Where\'s the tuna?')
#
#     if st.form_submit_button("Add the results!"):
#       with conn.session as session:
##         session.execute("INSERT INTO src_stream.bets VALUES (:a, :b, :c, :d, :e, :f);", {"a": my_race, "b": my_selector, "c": my_alo, "d": my_sai, "e": sentence1, "f": sentence2})
#         session.execute(text(f"INSERT INTO src_stream.bets VALUES ( '{my_race}', '{my_selector}', '{my_alo}', '{my_sai}', '{sentence1}', '{sentence2}')"))
#         session.commit()
#
#       time.sleep(1.5)
#       # Perform query.
#       df = conn.query('SELECT * FROM src_stream.bets order by id;', ttl="10m")
#       st.write(df)
#
#with st.form("my_deleted_bet"):
#     st.write("""
#	# To remove a bet
#	By id.
#	""")
#     my_bet_number = st.number_input('bet_number', value=99, format='%i')
#
#     if st.form_submit_button("Remove bet!"):
#       with conn.session as session:
#         session.execute(text(f"DELETE FROM src_stream.bets WHERE id='{my_bet_number}';"))
#         session.commit()
#
#       time.sleep(1.5)
#       # Perform query.
#       df = conn.query('SELECT * FROM src_stream.bets order by id;', ttl="10m")
#       st.write(df)
