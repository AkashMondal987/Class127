from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

starturl="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("/Users/krishnendu/Downloads/chromedriver")
browser.get(starturl)
time.sleep(10)
def scrap():
    header = ["name","light_years_from_earth","planet_mass","stellar_magnitude","discover_date"]
    planetData = []
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,"html.parcer")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")
            tempList = []
            for index,li_tag in enumerate(li_tags):
                if index == 0:
                    tempList.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        tempList.append(li_tag.contents[0])
                    except:
                        tempList.append("")
            planetData.append(tempList)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrap()