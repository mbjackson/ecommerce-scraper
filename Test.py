# Import Scraper Class
from Scrape import Scraper

# Create Empty List
results = list()

# Loop Through Given Product ID Numbers
for sku in ["400920513473", "400920415951", "465050237354"]:
    results.append(Scraper(sku).extract())

# Print Out Results
print(results)
