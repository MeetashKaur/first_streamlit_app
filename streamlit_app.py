import streamlit
import requests
import pandas 
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Mom's New Healthy Diner");

streamlit.header('Breakfast Menu')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥣 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  #normalizing the JSON version of the response
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  
streamlit.header("Fruityvice Fruit Advice!")
  
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.write('The user entered ', fruit_choice)
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except UTLError as e:
  streamlit.error()
