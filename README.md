# HeadlinesWebScraper
This project is a web scraper that fetches the latest football news headlines and links from a popular sports news website. The script uses Selenium, a powerful web automation tool, to navigate the website, extract relevant information, and store it in a structured Excel format.
# Football News Headlines Web Scraper

![Football]

## Video Demo
[![Football News Web Scraper](https://img.youtube.com/vi/qRJA1GZJB9c/0.jpg)](https://www.youtube.com/watch?v=qRJA1GZJB9c)

## Description
This project is a web scraper that fetches the latest football news headlines and links from a popular sports news website. The script uses Selenium, a powerful web automation tool, to navigate the website, extract relevant information, and store it in a structured format.

## Features
- Web Scraping: The script employs Selenium to automate the process of navigating to the sports news website and scraping the headlines, subtitles (if available), and links to the articles.
- Data Storage: The scraped data is stored in a Pandas DataFrame, making it easy to manipulate and analyze.
- Excel Export: The DataFrame is then exported to an Excel file named "headline_news.xlsx" for easy sharing and further processing.
- Error Handling: The script includes error handling to deal with any potential issues, such as missing elements on the webpage.

## How to Use
1. Install the required dependencies: Make sure you have Python and the necessary libraries (Selenium and Pandas) installed. You can install them using pip:
    ```
    pip install selenium pandas
    ```

2. Download and configure the Chrome WebDriver: Download the appropriate Chrome WebDriver for your operating system and place it in the project directory. Update the `path` variable in the script with the path to the downloaded Chrome WebDriver.

3. Run the script: Simply execute the `football_news_scraper.py` script, and it will start scraping the website for football news headlines and links. The results will be saved in the "headline_news.xlsx" file in the same directory.

4. Customize the script: You can modify the script to scrape headlines from other websites or add additional data fields, such as timestamps or article summaries.

## Contribution
Contributions are welcome! If you find any issues, have suggestions for improvements, or want to add new features, feel free to open an issue or submit a pull request.

Please Note:
- Web scraping may be subject to the terms of service of the website being scraped. Ensure that you have the right to scrape the data or consult the website's terms of service for guidance.
- This project is intended for educational and personal use only and should not be used for any commercial or unauthorized purposes.

## License
[MIT License](LICENSE)
