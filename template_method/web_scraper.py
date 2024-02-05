from abc import ABC, abstractmethod
import requests
import urllib

from bs4 import BeautifulSoup


# Step 1: Abstract Class (Web Scraper Template)
class WebScraperTemplate(ABC):
    @abstractmethod
    def send_request(self, url):
        """Abstract method for sending HTTP requests."""
        pass

    @abstractmethod
    def parse_html(self, content):
        """Abstract method for parsing HTML content."""
        pass

    @abstractmethod
    def extract_data(self, soup):
        """Abstract method for extracting data from parsed HTML."""
        pass

    # Template method orchestrating the steps
    def scrape_website(self, url):
        """The template method for web scraping."""
        content = self.send_request(url)
        soup = self.parse_html(content)
        data = self.extract_data(soup)
        return data

# Step 2: Concrete Class 1 (RequestsAndBeautifulSoupWebScraper)
class RequestsAndBeautifulSoupWebScraper(WebScraperTemplate):
    def send_request(self, url):
        """Concrete implementation for sending HTTP requests using requests library."""
        response = requests.get(url)
        return response.content

    def parse_html(self, content):
        """Concrete implementation for parsing HTML content using BeautifulSoup."""
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def extract_data(self, soup):
        """Concrete implementation for extracting data from parsed HTML."""
        # Example: Extracting all hyperlinks from the webpage
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links

# Step 3: Concrete Class 2 (UrllibAndRegexWebScraper)
class UrllibAndRegexWebScraper(WebScraperTemplate):
    def send_request(self, url):
        """Concrete implementation for sending HTTP requests using urllib."""
        with urllib.request.urlopen(url) as response:
            return response.read()

    def parse_html(self, content):
        """Concrete implementation for parsing HTML content using custom parser."""
        # Custom HTML parsing logic
        return content

    def extract_data(self, content):
        """Concrete implementation for extracting data using regex."""
        import re
        # Example: Extracting all email addresses from the webpage
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content.decode('utf-8'))
        return emails

# Main Section (Client Code)
if __name__ == "__main__":
    # Creating instances of the concrete classes
    web_scraper_requests_beautifulsoup = RequestsAndBeautifulSoupWebScraper()
    web_scraper_urllib_regex = UrllibAndRegexWebScraper()

    # Using the template method to scrape websites
    target_url = "https://amirlavasani.vercel.app/"

    print("Scraped Data using RequestsAndBeautifulSoupWebScraper:")
    data_requests_beautifulsoup = web_scraper_requests_beautifulsoup.scrape_website(target_url)
    for link in data_requests_beautifulsoup:
        print(link)

    print("\nScraped Data using UrllibAndRegexWebScraper:")
    data_urllib_regex = web_scraper_urllib_regex.scrape_website(target_url)
    for email in data_urllib_regex:
        print(email)
