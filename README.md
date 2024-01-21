Test Scenario

The provided Python script, test_states_list_websocket_api.py, performs the following steps:

1. Launches a Chromium browser using Playwright.
2. Navigates to the Deriv API Explorer page.
3. Waits for the element with the ID 'swagger-request-websocket-url' to be present on the page.
4. Retrieves the WebSocket URL from the page.
5. Launches a Selenium WebDriver (Chrome) and connects to the obtained WebSocket URL.
6. Sends a WebSocket request to the API endpoint /states_list.
7. Verifies the received response, checking if the status is 200 and if the 'states' data is not empty.
