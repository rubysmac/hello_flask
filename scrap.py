from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup


def scrap(search):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(f"https://www.wanted.co.kr/search?query={search}&tab=position")
    time.sleep(4)
    for i in range(3):
        page.keyboard.down("End")
        time.sleep(5)
    content = page.content()
    p.stop()
    soup = BeautifulSoup(content, "html.parser") # parse란, 문법적 해부. 
    jobs = soup.find_all("div", class_="JobCard_container__REty8") #find_all하면 list로 저장

    jobs_db = []

    for job in jobs:
        link = f"https://www.wanted.co.kr{job.find('a')['href']}" 
        title = job.find("strong", class_="JobCard_title__HBpZf").text 
        company_name = job.find("span", class_="JobCard_companyName__N1YrF").text

        #db리스트에 job dictionary 저장 
        job = { 
            "title":title,
            "company_name":company_name,
            "link":link
        }
        jobs_db.append(job)
    return jobs_db

