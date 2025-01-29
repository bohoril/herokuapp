# README

## Project Overview

This project contains automated tests for a simple login flow using Playwright and `pytest-playwright`. The tests are designed to verify both valid and invalid login scenarios on the web application.

## Setup Instructions

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Installation

1. **Install dependencies:** 
   
`pip install -r requirements.txt`

2. **Install Playwright browsers:**

`playwright install`

### Running Tests

Tu run the tests, execute the following command:

`pytest`

This will execute the tests using Chromium, Firefox, and WebKit browsers as specified in the `pytest.ini` configuration file.

To run the tests in headed mode, use the `--headed` flag:

`pytest --headed`

## Changes Made

### Initial Script

The initial script provided was an asynchronous Playwright script that tested a login flow. Here is the initial script for reference:

```python
# python3

import asyncio
from playwright.async_api import async_playwright

async def run():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch()
    page = await browser.new_page()

    await page.goto("http://the-internet.herokuapp.com/login")

    await page.fill("#user", "tomsmith")
    await page.fill("#pass", "SuperSecretPassword!")

    await page.click("#login")

    await page.wait_for_timeout(5000)

    await browser.close()
    await playwright.stop()

asyncio.run(run())
```

### Changes and Improvements

1. **Converted to Synchronous Script:**

- The initial script was an asynchronous script. I converted it to a synchronous script to make it easier to understand and maintain. Also in this case, the script is simple and does not require the use of asynchronous operations.

2. **Integrated with `pytest-playwright`:**

- The script was converted to a `pytest` test function and integrated with `pytest-playwright`. This allows the test to be executed using the `pytest` test runner and provides additional features such as fixtures and configuration options.

3. **Created Page Object Model (POM):**

- Created a Page Object Model (POM) to encapsulate the page elements and actions related to the login page. This helps in organizing the test code and makes it easier to read, maintain and update in the future.

4. **Added Test Cases:**

- Added test cases for both valid and invalid login scenarios.

5. Project Structure:

- Organized the project structure to follow best practices.

### Errors in the initial script:

Speaking of the initial script, there are a few issues that I would like to highlight:

- Asynchronous script for a simple login flow.
- Keyword `with` is recommended to ensure ensures that Playwright resources are properly initialized and cleaned up, even if an error occurs during execution. Therefore `playwright.stop()` is not required.
- Wrong selectors are used in the script.
- Assertion is missing in the script.
- Unnecessary `page.wait_for_timeout(5000)` is used in the script. Playwright has built-in wait functions.