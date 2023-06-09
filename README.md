# Thinkbridge Challenge

Was created a Python module called `scrape_sites` with 
a unique file and a function `scrape` to get information 
from a site url passed as a parameter.

# CSV File structure

The CSV file must contain at least two columns, the 
former being a name and the latter being the **WebSite URL** 
to visit. For example:

```
Company,Website
Company A,https://www.google.com
```

**Note**: You must respect the header names `Company` and 
`Website` respectively.

# API Backend

Was used FastAPI to write a very simple endpoint using
GET method in `/scrape` and receives a query paramater
called `site_url`. Example:
```
http://localhost:8000/scrape?site_url=https://www.google.com
```

The API was run with `uvicorn` package, opening a terminal and typing:
```commandline
uvicorn backend_api:app --reload 
```
If this was made in your local machine, you can test
if everything was fine accessing with a web browser
to `http://localhost:8000/ ` and see `"It works!"`
on the page.

