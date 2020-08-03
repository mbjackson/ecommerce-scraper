# eCommerce Scraper

## 1) Description
This Python class can be used to scrape information from an eCommerce Website (specifically shopDisney.com).

## 2) Installation
All you need to do is download the files and meet the prerequisities below!

### a) Prerequisities
- Python 3+
- Beautiful Soup

### 3) Usage
The scraper class can be imported as follows...

``` python
from Scrape import Scraper
```

Then the Scraper class takes a single variable, SKU (Stock Keeping Unit)

``` python
item = Scraper("400922563483")
```

To extract infomration from the web page, call the extract function

``` python
item.extract()
```

The returned results are a JSON full of useful information!
