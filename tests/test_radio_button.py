import re
from playwright.sync_api import expect


def test_demoqa_home(page):
    page.goto("https://demoqa.com")
    page.wait_for_timeout(2000)
    page.locator("div").filter(has_text=re.compile(r"^Elements$")).nth(1).click()
    page.get_by_role("listitem").filter(has_text="Radio Button").click()
    expect(page.locator("#app")).to_contain_text("Do you like the site?")
    expect(page.get_by_text("Yes")).to_be_visible()
    expect(page.get_by_text("Impressive")).to_be_visible()
    expect(page.get_by_text("No")).to_be_visible()
    page.get_by_text("Yes").click()
    expect(page.get_by_role("paragraph")).to_contain_text("You have selected Yes")
    page.get_by_text("Impressive").click()
    expect(page.get_by_role("paragraph")).to_contain_text(
        "You have selected Impressive"
    )
