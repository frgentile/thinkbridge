'''
Module for getting site elements
@Author: GENTILE, Francisco
'''
import playwright.async_api as pw_async
from bs4 import BeautifulSoup


async def aio_scrape_site(url):
    document = {
        'errno': 0,
        'page': {}
    }

    async with pw_async.async_playwright() as playwright:
        # Prepare browser
        browser = await playwright.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        try:
            # Go to URL
            response = await page.goto(url)
            # And get content
            html_content = await page.content()
            # Analize HTML for getting DOM using BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            # For every element
            for element in soup.find_all():
                # Get label, attributes and value
                tag = element.name
                attributes = element.attrs
                text = element.text

                document['page'][tag] = {
                    'attributes': attributes,
                    'value': text
                }
        except Exception as exc:
            document['errno'] = -1
            document['page'] = f"Exception: {exc}"
        finally:
            # Close browser
            await context.close()
            await browser.close()
    return document
