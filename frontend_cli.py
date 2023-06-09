'''
Front-end for Thinkbridge Challenge
@Author:  GENTILE, Francisco
'''
import asyncio
import aiofiles
from aiocsv import AsyncDictReader
import csv
import json
import requests_async as requests
from scrape_sites.utils import aio_scrape_site

#Rashmi K  rashmi.koravi@thinkbridge.in


async def main():
    html_documents = {}
    with open('g2crowd.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            company = row['Company']
            site_url = row['Website']
            document = await aio_scrape_site(site_url)
            html_documents[company] = document
    print(f"FINAL: {html_documents}")


async def main2(args):
    scrape_api_endpoint = "http://localhost:8000/scrape"
    html_documents = {}
    try:
        async with aiofiles.open(args.csv_file, 'r') as file:
            reader = AsyncDictReader(file)
            async for row in reader:
                company = row['Company']
                site_url = row['Website']
                params = {'site_url': site_url}
                try:
                    print(f"Fetching {site_url}")
                    response = await requests.get(scrape_api_endpoint, params)
                    json_response = response.json()
                    html_documents[company] = json_response['page']
                except Exception as exc:
                    print("ERROR ", exc)

        with open(args.output_file, "w") as file:
            json.dump(html_documents, file)
        print(f"FINAL: {html_documents}")

    except FileNotFoundError:
        print(f"ERROR: File {args.csv_file} was NOT FOUND!.")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        prog='frontend_cli.py',
        description='Front-end for Thinkbridge Challenge')

    parser.add_argument('csv_file')  # positional argument
    parser.add_argument('-o', '--output', dest='output_file', default='scraped_sites.json',
                        help='JSON Output filename. Default: scraped_sites.json')
    args = parser.parse_args()
    #
    print(__doc__)
    asyncio.run(main2(args))
    print("Done!")
