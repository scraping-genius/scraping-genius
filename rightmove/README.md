# Rightmove Scraper

This project contains scraper files for extracting data from https://www.rightmove.co.uk/property-for-sale/find.html?searchLocation=London&useLocationIdentifier=true&locationIdentifier=REGION%5E87490&radius=0.0&_includeSSTC=on.

## Files

- `create_scraper_list.py` - Creates a scraper for the website
- `extract_data.py` - Extracts data using the created scraper
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Get your Minexa API key from [Minexa.ai](https://minexa.ai)

3. Replace `YOUR_API_KEY` in both Python files with your actual API key

## Usage

### Step 1: Create the scraper
```bash
python create_scraper_list.py
```

This will create a scraper and return a scraper ID. Note this ID for the next step.

### Step 2: Extract data
1. Replace the `scraper_id` value in `extract_data.py` with your actual scraper ID
2. Replace the `urls` value in `extract_data.py` with your actual URLs
3. Run the extraction:
```bash
python extract_data.py
```

## Output

The data extraction script will generate:
- `extraction_YYYY_MM_DD_HH_MM.json` - Raw JSON data
- `extraction_YYYY_MM_DD_HH_MM.csv` - CSV format
- `extraction_YYYY_MM_DD_HH_MM.xlsx` - Excel format
