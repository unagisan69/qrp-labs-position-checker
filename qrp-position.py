#!/usr/bin/env python3
import sys
import requests
from bs4 import BeautifulSoup

URL = "https://www.qrp-labs.com/qcxmini/assembled.html"
ORDER_ID = sys.argv[1] if len(sys.argv) > 1 else "1"

html = requests.get(URL, timeout=20).text
soup = BeautifulSoup(html, "html.parser")

for row in soup.find_all("tr"):
    cells = [td.get_text(" ", strip=True) for td in row.find_all("td")]
    if len(cells) >= 2 and cells[1] == ORDER_ID:
        print(f"Order {ORDER_ID} is position {cells[0]}")
        print(f"Serial: {cells[2] if len(cells) > 2 else 'N/A'}")
        print(f"Model: {cells[3] if len(cells) > 3 else 'N/A'}")
        print(f"Order date: {cells[4] if len(cells) > 4 else 'N/A'}")
        sys.exit(0)

print(f"Order {ORDER_ID} was not found on the waiting list.")
sys.exit(1)
