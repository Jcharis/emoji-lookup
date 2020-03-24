# Core Pkgs
import streamlit as st 
import json
import pandas as pd 
import itertools

# Fxn to Load Data
@st.cache
def load_data(json_file):
	with open(json_file) as f:
		data = json.load(f)
	return data 

# Get the Value
def get_value(val,my_dict):
	for key ,value in my_dict.items():
		if val == key:
			return value
# Get the Keys
def get_key(val,my_dict):
	for key ,value in my_dict.items():
		if val == value:
			return key

def main():
	"""Emoji Lookup App"""

	st.title("Emoji Lookup")
	st.subheader("Built with Streamlit and :heart:")

	activities = ["Search","Reverse-Search","Emoji-2-Unicode","Unicode-2-Emoji","Combi","Sentiment-Table","About"]
	menu = st.sidebar.selectbox("Select Task",activities)
	data = load_data("data/emoji.json")


	if menu == 'Search':
		st.subheader("Search Emoji")
		raw_text = st.text_input("Search Emoji","Type Here")
		search_text = raw_text.lower()
		if raw_text is not 'Type Here':

			if search_text in tuple(data.keys()):
				result = ':{}:'.format(search_text)

				st.success("Found {}".format(result))
				st.markdown(result)
				st.text("Usage :=> {}".format(result))
			else:
				st.warning("{} Not Found".format(search_text))


	elif menu == 'Reverse-Search':
		st.subheader("Reverse-Search Emoji")
		raw_text = st.text_input("Search Emoji","Type Here")
		rsearch_text = raw_text.lower()

		if raw_text is not 'Type Here':
			if rsearch_text in tuple(data.values()):
				st.success("Found {}".format(rsearch_text))
				result2 =  get_key(rsearch_text,data)
				st.text("Emoji Text is => :{}:".format(result2))
			else:
				st.warning("{} Not Found".format(rsearch_text))



	elif menu == 'Emoji-2-Unicode':
		st.subheader("Search Unicode for Emoji")
		raw_text = st.text_input("Search Unicode","Emoji Here")
		df = pd.read_csv("data/Emoji_Sentiment_Data.csv")
		new_df = df.loc[df['Emoji'] == raw_text]
		
		if new_df.empty:
			st.warning("{} Not Found".format(raw_text))
		else:
			st.dataframe(new_df[['Emoji','Unicode codepoint','Unicode name']])



	elif menu == 'Unicode-2-Emoji':
		st.subheader("Unicode-2-Emoji")
		raw_text = st.text_input("Search Emoji","Unicode Here")
		df = pd.read_csv("data/Emoji_Sentiment_Data.csv")
		new_df = df.loc[df['Unicode codepoint'] == raw_text]
		
		if new_df.empty:
			st.warning("{} Not Found".format(raw_text))
		else:
			st.dataframe(new_df[['Emoji','Unicode codepoint','Unicode name']])


	elif menu == 'Combi':
		st.subheader("Combine Multiple Emojis")
		limit = st.number_input("Select Number of Emoji Limit",5,len(data.items()))
		c_data = dict(itertools.islice(data.items(),limit))
		multi_combi = st.multiselect("Select Multiple Emoji",tuple(c_data.keys()))

		combi_list = [':{}:'.format(i) for i in multi_combi]
		# for i in multi_combi:
		# 	rsult = ':{}:'.format(i)

		st.markdown(' '.join(combi_list))



	elif menu == 'Sentiment-Table':
		st.subheader("Sentiment-Table For Emoji")
		df = pd.read_csv("data/Emoji_Sentiment_Data.csv")
		st.dataframe(df)

	elif menu == 'About':
		st.subheader("About Emoji Lookup App")
		st.markdown("Built with [Streamlit](https://www.streamlit.io/) by [JCharisTech](https://www.jcharistech.com/)")
		st.text("Jesse E.Agbe(JCharis)")
		st.text("Credits to [Omnidan,Thomasseleck,JCharis]")

		st.success("Jesus Saves @JCharisTech")





if __name__ == '__main__':
	main()

