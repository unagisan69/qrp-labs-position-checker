# qrp-labs-position-checker

Check your position in the QRP Labs assembly wait list.

## Description

This script fetches the QRP Labs QCX-mini assembled orders page and parses the table to find the position of a given order ID.

## Requirements

- Python 3
- requests
- beautifulsoup4

Install dependencies:

pip3 install requests beautifulsoup4

## Usage

python3 qrp-position.py

### Example

python3 qrp-position.py 123

## Output

The script will return:

- Position in the queue
- Serial number
- Model
- Order date

If the order ID is not found, it will notify you.

## Notes

- The script relies on the structure of the QRP Labs webpage. If the page layout changes, updates to the parser may be required.
