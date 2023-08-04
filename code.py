#get info from site
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path = "D:\\Desktop\\SSRRIIDD\\Materials used\\web automation\\chromedriver-win64\\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
    title_element = container.find_element(by="xpath", value='./a/h3')
    title = title_element.text

    # Handle missing subtitle element
    subtitle_elements = container.find_elements(by="xpath", value='./a/p')
    subtitle = subtitle_elements[0].text if subtitle_elements else ""

    link_element = container.find_element(by="xpath", value='./a')
    link = link_element.get_attribute("href")

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)

# Save data to an Excel file
df_headlines.to_excel('headline_news.xlsx', index=False)

driver.quit()