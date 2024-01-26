import pandas as pd
from jobspy import scrape_jobs


def main(args):
    jobs = scrape_jobs(
        site_name=["indeed"],
        search_term="software engineer",
        location="London, UK",
        results_wanted=10,
        country_indeed="UK",  # only needed for indeed / glassdoor
        full_description=True
    )   

    return {"body": jobs}
