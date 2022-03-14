import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract(page):
    """
    choose a page to the url
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    url = f"https://www.indeed.com/jobs?q=software%20engineer&l=United%20States&start={page}&vjk=c3cce2281e1035ab"
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def transform(soup):
    divs = soup.find_all("div", class_="job_seen_beacon")
    title = []
    for tag in soup.select(".resultContent span[title]"):
        title.append(tag.text)
    for item in divs:
        # title = item.find("span").text
        company = item.find("span", class_="companyName").text.strip()
        try:
            salary = item.find("svg", class_="attribute-snippet").text().strip()
        except:
            salary = ""
        location = item.find(class_="companyLocation").text.strip()
        print(location)
        post_date = item.find("span", {"class": "date"}).text.strip()
        print(post_date)
        summary = (
            item.find("div", {"class": "job-snippet"}).text.strip().replace("\n", "")
        )

        # single_job_url = "https://www.indeed.com/viewjob?jk=" + item["data-jk"]
        # print(single_job_url)
        job = {"title": title, "company": company, "salary": salary, "summary": summary}
        joblists.append(job)
    return


joblists = []
c = extract(0)
print(transform(c))

# for i in range(0, 40, 10):
#     print(f"Getting page", "{i}")
#     c = extract(0)
#     transform(c)
# df = pd.DataFrame(joblists)
# print(df.head())
# df.to_csv("jobs.csv")


# def get_single_page(joblists, soup):
#     divs = soup.find_all("div", class_="job_seen_beacon")
#     job_posts = []
#     for div in divs:
#         job = dict()
#         job = transform(job, div)
#         job_posts.append(div["data-jk"])

#         print(single_job_url)
