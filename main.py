import requests


def proccessPage(page: int):
    print(f"Processing page {page}")
    url = "https://gcsservices.careers.microsoft.com/search/api/v1/search"
    params = {
        'pg': page,
    }
    res = requests.get(url, params=params).json()
    jobs = res['operationResult']['result']['jobs']
    for job in jobs:
        properties = job['properties']
        data = {
            'jobId': job['jobId'],
            'title': job['title'],
            'postingDate': job['postingDate'],
            'description': properties['description'],
            'locations': ", ".join(properties['locations']),
            'primaryLocation': properties['primaryLocation'],
            'workSiteFlexibility': properties['workSiteFlexibility'],
            'profession': properties['profession'],
            'discipline': properties['discipline'],
            'jobType': properties['jobType'],
            'roleType': properties['roleType'],
            'employmentType': properties['employmentType'],
            'educationLevel': properties['educationLevel'],
        }
        print(data)


def main():
    url = "https://gcsservices.careers.microsoft.com/search/api/v1/search"
    res = requests.get(url).json()
    totalJobs = res['operationResult']['result']['totalJobs']
    perPage = len(res['operationResult']['result']['jobs'])
    print(f"Total Jobs: {totalJobs}")
    for page in range(1, totalJobs // perPage + 2):
        proccessPage(page)


if __name__ == '__main__':
    main()
