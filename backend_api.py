'''
Back-end API endpoint
@Author: GENTILE, Francisco
'''
from scrape_sites.utils import aio_scrape_site
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return "It works!"

@app.get("/scrape")
async def scrape(site_url: str):
    document = await aio_scrape_site(site_url)
    return document
