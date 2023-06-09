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

# Front-End

The front-end is very single Command Line Interface (CLI). It's the
file named `frontend_cli.py`. You must pass as required parameter the
path to the csv file containing the g2crowd info.

The output is saved in JSON format in a file. By default this file is 
is `scraped_sites.json` that can be overriden with `--output` or `-o`
optional arg.

The output format for each row of the csv file is:

```json
{
  "Company": {
    "tag_element1": {
      "attributes": { ... }, 
      "value": "..."
    },
    "tag_element2": {
      "attributes": { ... }, 
      "value": "..."
    }, 
    ...
  }
}
```

# Running

Follow the next steps on a Linux machine (preferably ubuntu):

1. Run script `setup.bash` to setup the virtual env.
2. Run `source venv/bin/activate`.
3. Run `uvicorn backend_api:app --reload &` to activate API backend.
4. *Optional*: you can test api is working in `http://localhost:8000`.
5. Play with `frontend_cli.py`. Example: `python3 frontend_cli.py g2crowd.csv`.
6. *Optional*: you can kill API backend with `killall uvicorn` 