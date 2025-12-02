import re
from playwright.sync_api import Page, expect


def test_text_box(page: Page):
    page.goto("https://demoqa.com")
    page.wait_for_timeout(2000)

    # Checking visibility of Text Box elements
    page.locator("div").filter(has_text=re.compile(r"^Elements$")).nth(1).click()
    page.get_by_role("listitem").filter(has_text="Text Box").click()
    expect(page.locator("#userName-label")).to_contain_text("Full Name")
    expect(page.locator("#userEmail-label")).to_contain_text("Email")
    expect(page.locator("#currentAddress-label")).to_contain_text("Current Address")
    expect(page.locator("#permanentAddress-label")).to_contain_text("Permanent Address")
    expect(page.get_by_role("textbox", name="Full Name")).to_be_visible()
    expect(page.get_by_role("textbox", name="name@example.com")).to_be_visible()
    expect(page.get_by_role("textbox", name="Current Address")).to_be_visible()
    expect(page.locator("#permanentAddress")).to_be_visible()
    expect(page.get_by_role("button", name="Submit")).to_be_visible()

    # Filling the Text Box form and submitting
    page.get_by_role("textbox", name="Full Name").fill("Tester")
    page.get_by_role("textbox", name="name@example.com").fill("end_2_end@dummy.com")
    page.get_by_role("textbox", name="Current Address").fill("Munich, Germany")
    page.locator("#permanentAddress").fill("Munich, Germany")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("#name")).to_contain_text("Name:Tester")
    expect(page.locator("#email")).to_contain_text("Email:end_2_end@dummy.com")
    expect(page.locator("#output")).to_contain_text("Current Address :Munich, Germany")
    expect(page.locator("#output")).to_contain_text(
        "Permananet Address :Munich, Germany"
    )
