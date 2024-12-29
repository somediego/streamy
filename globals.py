class var_names:
	places=[
		'Melbourne',
		'China',
		'Suzuka',
		'Bahrain',
		'Saudi Arabia',
		'Miami',
		'Imola',
		'Monaco',
		'Spain',
		'Canada',
		'Austria',
		'United Kingdom',
		'Belgium',
		'Hungary',
		'Netherlands',
		'Italy',
		'Azerbaijan',
		'Singapore',
		'USA',
		'Mexico',
		'Brazil',
		'Las Vegas',
		'Qatar',
		'Abu Dhabi',
	]
	dates=[
		'March 14-16	Australia	Melbourne',
		'March 21-23	China	Shanghai',
		'April 4-6	Japan	Suzuka',
		'April 11-13	Bahrain	Sakhir',
		'April 18-20	Saudi Arabia	Jeddah',
		'May 2-4	USA	Miami',
		'May 16-18	Italy	Imola',
		'May 23-25	Monaco	Monaco',
		'May 30 – June 1	Spain	Barcelona',
		'June 13-15	Canada	Montreal',
		'June 27-29	Austria	Spielberg',
		'July 4-6	United Kingdom	Silverstone',
		'July 25-27	Belgium	Spa',
		'August 1-3	Hungary	Budapest',
		'August 29-31	Netherlands	Zandvoort',
		'September 5-7	Italy	Monza',
		'September 19-21	Azerbaijan	Baku',
		'October 3-5	Singapore	Singapore',
		'October 17-19	USA	Austin',
		'October 24-26	Mexico	Mexico City',
		'November 7-9	Brazil	Sao Paulo',
		'November 20-22	USA	Las Vegas',
		'November 28-30	Qatar	Lusail',
		'December 5-7	Abu Dhabi	Yas Marina',
	]
	players=['Pericazo','Joseles','Diegis']
	pilots= [
		'Norris',
		'Verstappen',
		'Alonso',
		'Sainz',
		'Hamilton',
		'Lecrecr',
		'Russel',
		'Piastri',
		'Antonelli',
		'Lawson',
		'Stroll',
		'Ocon',
		'Gasly',
		'Albon',
		'Tsunoda',
		'Hadjar',
		'Hulkenberg',
		'Bearman',
		'Doohan',
		'Bortoleto',
	]

# passwords stuff.
########################
#  .streamlit/secrets.toml
# [passwords]
# # Follow the rule: username = "password"
# alice_foo = "streamlit123"
# bob_bar = "mycrazypw"
########################
import secrets as secr
import streamlit as st

import extra_streamlit_components as stx	# for cookies
#@st.cache_resource
def get_manager():
    return stx.CookieManager()

def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and secr.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # load cookies
    cookie_manager = get_manager()

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        # save dummy cookie stx_ckeck
        cookie_manager.set("stx_check", True) # Expires in a day by default
        # give open access
        return True

    # checking dummy cookie test
    if cookie_manager.get(cookie="stx_check"):
        # give open access
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False




##test
#if not check_password():
#    st.stop()

##################
# cookies
##################
#import extra_streamlit_components as stx
#import datetime
#st.write("# Cookie Manager")
#
#@st.cache_resource
#def get_manager():
#    return stx.CookieManager()
#
#cookie_manager = get_manager()
#
#st.subheader("All Cookies:")
#cookies = cookie_manager.get_all()
#st.write(cookies)
#
#c1, c2, c3 = st.columns(3)
#
#with c1:
#    st.subheader("Get Cookie:")
#    cookie = st.text_input("Cookie", key="0")
#    clicked = st.button("Get")
#    if clicked:
#        value = cookie_manager.get(cookie=cookie)
#        st.write(value)
#with c2:
#    st.subheader("Set Cookie:")
#    cookie = st.text_input("Cookie", key="1")
#    val = st.text_input("Value")
#    if st.button("Add"):
#        cookie_manager.set(cookie, val) # Expires in a day by default
#with c3:
#    st.subheader("Delete Cookie:")
#    cookie = st.text_input("Cookie", key="2")
#    if st.button("Delete"):
#        cookie_manager.delete(cookie)
