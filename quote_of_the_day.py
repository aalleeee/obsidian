import requests
import time
from bs4 import BeautifulSoup
from datetime import date


def main():
	#print("Starting submittions!")
	sess = requests.Session()
	req = sess.get("https://www.brainyquote.com/quote_of_the_day")
	soup = BeautifulSoup(req.content, 'html.parser')
	#print(soup.prettify())
	quote_of_the_day = soup.find(class_="b-qt").get_text().strip()
	print(quote_of_the_day)
	author = soup.find(class_="bq-aut").get_text().strip()
	print(author)
	
	print("-----------------------------------")
	path = "G:/Il mio Drive/Vault0.1/Daily Notes/"
	today = date.today()
	filename = today.strftime("%Y-%m-%d")+".md"
	print(filename)
	file = open(path + filename,"a")
	file.write(">"+quote_of_the_day+"\n>---\n>"+author)
	file.close()
	
if __name__ == "__main__":
    main()