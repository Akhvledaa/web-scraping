Web scraping using python
This Python script is designed to scrape information about Irish whiskeys from "https://www.thewhiskyexchange.com" (for educational purposes only). It utilizes the requests library to send HTTP requests and retrieve the HTML content of the web page. The HTML is then parsed using the BeautifulSoup library to extract essential details such as the whiskey name, alcohol percentage, price, and product link.

The extracted data is stored in a CSV file and also printed to the console for immediate viewing. The script supports scraping multiple pages of whiskey listings, ensuring there are no duplicate entries. The script also introduces random delays between requests using the time library to be respectful of the server's resources.

To run the script, make sure you have the required libraries installed.
