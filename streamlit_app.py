
import streamlit
streamlit.title('My Parents Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('ð¥£ Omega3 and Blue Berry Omlet')
streamlit.text('ð¥ kale Spinach & Rocket Smoothie')
streamlit.text('ð hard Boiled Free Range Eggs')
streamlit.text('ð¥ðAvocado Toast')
streamlit.header('ðð¥­ Build Your Own Fruit Smoothie ð¥ð')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page.
streamlit.dataframe(my_fruit_list)
