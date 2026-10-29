# 7.1a Import required libraries
import requests
from bs4 import BeautifulSoup
import csv
import time

# 8.1 Create a CSV file named books_data.csv
# 8.2 Store Title, Price, and Availability in the CSV
csv_file = open("books_data.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)

# Write the column headings
csv_writer.writerow(["Title", "Price", "Availability"])

# 8.3 Scrape data from at least 2 pages using a loop
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

for page_number in range(1, 3):  # Pages 1 and 2
    url = base_url.format(page_number)

    # 7.1b Send a request to the website
    response = requests.get(url)

    # 7.1c Print the response status code
    print(f"\nPage {page_number} response status code: {response.status_code}")

    # 7.2 Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # 7.3 Extract book title, price, and availability status
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        availability = book.find("p", class_="instock availability").text.strip()

        # 7.4 Display the extracted results in the terminal
        print("Title:", title)
        print("Price:", price)
        print("Availability:", availability)
        print("-" * 50)

        # 8.2 Write each book's data into the CSV file
        csv_writer.writerow([title, price, availability])

    # Be polite to the website between requests
    time.sleep(1)

# Close the CSV file after scraping is complete
csv_file.close()

print("\nScraping complete. Data saved to books_data.csv")