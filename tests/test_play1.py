from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.fixture(scope='function')
def browser_context():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


def test_run(browser_context):
    page = browser_context.new_page()
    page.goto('https://www.alx.pl')
    page.screenshot(path="screenshot/obraz1.png")
    assert page.title() == "ALX – szkoła programowania, szkolenia IT i kursy informatyczne"


def test_example(browser_context):
    page = browser_context.new_page()
    page.goto("https://www.alx.pl/")
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("devops")
    page.get_by_role("textbox").press("Enter")
    page.get_by_role("link", name="Devops - AWS, Terraform,").click()
    page.get_by_text("Osobom zainteresowanym").click()
    page.get_by_role("link", name="Zapisz się").click()
    page.wait_for_timeout(1000)
    page.screenshot(path="screenshot/obraz2.png")
    expect(page.get_by_label("Termin*")).to_be_visible()
    expect(page.locator("#article")).to_contain_text("Devops - AWS, Terraform, Monitoring DEVOPS-102")

