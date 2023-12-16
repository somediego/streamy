class var_names:
	places=[
		'Bahrain',
		'Saudi Arabia',
		'Australia',
		'Japan',
		'China',
		'Miami',
		'Emilia Romagna',
		'Monaco',
		'Canada',
		'Spain',
		'Austria',
		'United Kingdom',
		'Hungary',
		'Belgium',
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
		'February 29 – March 2 	Bahrain 	Sakhir',
		'March 7-9 	Saudi Arabia 	Jeddah',
		'March 22-24 	Australia 	Melbourne',
		'April 5-7 	Japan 	Suzuka',
		'April 19-21 	China 	Shanghai',
		'May 3-5 	Miami 	Miami',
		'May 17-19 	Emilia Romagna 	Imola',
		'May 24-26 	Monaco 	Monaco',
		'June 7-9 	Canada 	Montreal',
		'June 21-23 	Spain 	Barcelona',
		'June 28-30 	Austria 	Spielberg',
		'July 5-7 	United Kingdom 	Silverstone',
		'July 19-21 	Hungary 	Budapest',
		'July 26-28 	Belgium 	Spa',
		'August 23-25 	Netherlands 	Zandvoort',
		'August 30 – September 1 	Italy 	Monza',
		'September 13-15 	Azerbaijan 	Baku',
		'September 20-22 	Singapore 	Singapore',
		'October 18-20 	USA 	Austin',
		'October 25-27 	Mexico 	Mexico City',
		'November 1-3 	Brazil 	Sao Paulo',
		'November 21-23 	Las Vegas 	Las Vegas',
		'November 29 – December 1 	Qatar 	Lusail',
		'December 6-8	Abu Dhabi 	Yas Marina',
	]
	players=['Pericazo','Joseles','Diegis']
	pilots= [
		'Norris',
		'Verstappen',
		'Alonso',
		'Sainz',
		'Hamilton',
		'Perez',
		'Lecrecr',
		'Russel',
		'Piastri',
		'Stroll',
		'Ocon',
		'Gasly',
		'Albon',
		'Tsunoda',
		'Bottas',
		'Hulkenberg',
		'Ricardo',
		'Zhou',
		'Magnussen',
		'Lawson',
		'Sargeant',
		'De Vries',
	]

# passwords stuff.
########################
#  .streamlit/secrets.toml
# [passwords]
# # Follow the rule: username = "password"
# alice_foo = "streamlit123"
# bob_bar = "mycrazypw"
########################
import hmac
import streamlit as st

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
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False

#if not check_password():
#    st.stop()

