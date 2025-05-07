import requests
from bs4 import BeautifulSoup


def fetch_jobs():
    url = "https://realpython.github.io/fake-jobs"
    html_content = requests.get(url).content
    soup = BeautifulSoup(html_content, "html.parser")

    job_cards = soup.find_all("div", class_="card-content")
    jobs = []
    for job_card in job_cards:
        # Get job data
        title = job_card.find("div", class_="media").find("div", class_="media-content").find("h2").text.strip()
        company = job_card.find("div", class_="media").find("div", class_="media-content").find("h3").text.strip()
        location = job_card.find("div", class_="content").find("p", class_="location").text.strip()
        link = job_card.find("footer", class_="card-footer").find_all("a")[1].get("href").strip()

        # Fetch description
        job_link_content = requests.get(link).content
        job_soup = BeautifulSoup(job_link_content, "html.parser")
        desc = job_soup.find("div", class_="content").find("p").text.strip()

        # Create Job object and add it to the list
        job = [title, company, location, desc, link]
        jobs.append(job)
    return jobs
