import json
import pytest
from playwright.async_api import async_playwright
from selenium import webdriver

@pytest.mark.asyncio
async def test_states_list_websocket_api():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        try:
            await page.goto('https://api.deriv.com/api-explorer#states_list')

            # Wait for the element with ID 'swagger-request-websocket-url'
            await page.wait_for_selector("#swagger-request-websocket-url")

            # Get the WebSocket URL from the page
            websocket_url = await page.evaluate('() => document.querySelector("#swagger-request-websocket-url").textContent')

            # Open a WebSocket connection using Selenium (placeholder, adjust as needed)
            driver = webdriver.Chrome()
            driver.get(websocket_url)

            # Send the request (placeholder, adjust as needed)
            request = {
                "method": "GET",
                "uri": "/states_list",
                "headers": {
                    "Content-Type": "application/json"
                }
            }
            driver.send_keys(json.dumps(request))

            # Verify the received response (placeholder, adjust as needed)
            response = json.loads(driver.page_source)
            assert response["status"] == 200
            assert response["data"]["states"] is not None

        except Exception as e:
            print(f"Error: {e}")

        finally:
            if 'driver' in locals() and driver is not None:
                driver.quit()

