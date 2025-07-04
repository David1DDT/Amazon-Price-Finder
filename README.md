# Amazon Price Finder

A simple Python script to monitor the price of a specific Amazon product and send an email alert when the price drops below a specified threshold.

## Features
- Fetches product page from Amazon
- Parses the product price
- Sends email notification if the price condition is met

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`
- `smtplib` (standard library)
- Environment variables for email credentials and password

## Setup

1. Clone the repository or create a new Python file with the code.

2. Install necessary packages:
```bash
pip install requests beautifulsoup4
```

3. Set your environment variables:
```bash
export EMAIL='your_email@example.com'
export PASSWORD='your_email_password'
```

*Note:* For enhanced security, consider using app-specific passwords or OAuth2 for email authentication.

## Usage

- Update the URL in the script to the Amazon product you want to monitor.
- Adjust the price threshold in the script (`if price > 100:`) to your desired value.
- Run the script:
```bash
python amazon_price_finder.py
```

## Notes
- The script currently checks a fixed product URL.
- Amazon may change its page structure, which could require updates to the parsing logic.
- For continuous monitoring, consider scheduling the script with cron or a task scheduler.

## Disclaimer
This script is for personal use only. Be mindful of Amazon's terms of service regarding web scraping.

## License
This project is licensed under the MIT License.

---

Feel free to customize and expand upon this script to suit your needs!


