import requests
from bs4 import BeautifulSoup


def scrape_book():
	url = "https://books.toscrape.com"
	
	headers = {"User-Agent": "Mozilla/5.0"}

	response = requests.get(url, headers=headers)

	soup = BeautifulSoup(response.text, 'html.parser')
	books = []

	for book in soup.find_all('article', class_='product_pod'):
		title = book.h3.a['title']
		price = book.find('p', class_='price_color').text.replace('$', '')
		rating = book.find('p", class = "star_rating')['class'][1]
		availability = book.find('p', class_='instock availability').text.strip()
		
		books.append({
			"title":title,
			"price":price,
			"rating":rating,
			"availability": availability
		})
		
		print(f"Scraped: {title} - ${price}")
        
	return books

if __name__ == "__main__":
    scrape_book()
