from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope='function')
def browser_context():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


def test_run(browser_context):
    page = browser_context.new_page()
    page.goto('https://www.alx.pl')
    page.screenshot(path="screenshot/obraz1.png")
    assert page.title() == "ALX – szkoła programowania, szkolenia IT i kursy informatyczne"

