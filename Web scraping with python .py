#Necessary library for web scarping
!pip install newspaper3k feedparser
 # Install the newspaper3k module

from newspaper import Article

# URL of the article to scrape
article_url = 'https://timesofindia.indiatimes.com/'

def extract_article_info(url):
    try:
        # Initialize the Article object with the URL
        article = Article(url)

        # Download the article's HTML content
        article.download()

        # Parse the downloaded HTML content
        article.parse()

        # Extract relevant information
        title = article.title
        authors = article.authors
        publish_date = article.publish_date
        content = article.text

        # Print the extracted information
        print(f"Title: {title}")
        print(f"Authors: {', '.join(authors) if authors else 'No authors listed'}")
        print(f"Publish Date: {publish_date}")
        print(f"Content: {content[:500]}...")  # Print the first 500 characters of the content

    except Exception as e:
        print(f"Failed to process article: {url}\nError: {e}")

# Extract and print information from the example article
extract_article_info(article_url)
