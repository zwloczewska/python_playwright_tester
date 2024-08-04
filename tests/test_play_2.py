import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.alx.pl/")
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("devops")
    page.get_by_role("textbox").press("Enter")
    page.get_by_role("link", name="Devops - AWS, Terraform,").click()
    page.get_by_text("Osobom zainteresowanym").click()
    page.get_by_role("link", name="Zapisz się").click()
    expect(page.get_by_label("Termin*")).to_be_visible()
    expect(page.locator("#article")).to_contain_text("Devops - AWS, Terraform, Monitoring DEVOPS-102")
