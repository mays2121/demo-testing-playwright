import re
from playwright.sync_api import Page, expect


def test_check_box(page: Page):
    page.goto("https://demoqa.com")
    page.wait_for_timeout(2000)
    page.locator("div").filter(has_text=re.compile(r"^Elements$")).nth(1).click()
    page.get_by_text("Check Box").click()
    page.get_by_role("button", name="Expand all").click()
    page.get_by_text("React").click()
    expect(page.locator("#result")).to_contain_text("You have selected :react")
    page.get_by_text("Home").click()
    result = "You have selected :homedesktopnotescommandsdocumentsworkspacereact"
    expect(page.locator("#result")).to_contain_text(
        f"{result}angularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile"
    )
