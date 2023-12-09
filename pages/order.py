import streamlit as st

from globals import var_names
# get class
v1= var_names()

st.markdown("""
	# Order
	"""
)
st.sidebar.markdown('# Order')

counter=1;
list_=[]
for i, x in enumerate(v1.dates):
  if i % 3 == 0:
    list_.append([x, v1.players[1].title(), v1.players[2].title(), v1.players[0].title()])
  elif (i+1) % 3 == 0:
    list_.append([x, v1.players[2].title(), v1.players[0].title(), v1.players[1].title()])
  else :
    list_.append([x, v1.players[0].title(), v1.players[1].title(), v1.players[2].title()])

st.dataframe(list_)

