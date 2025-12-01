from playwright.sync_api import Page, expect

def test_demoqa_home(page: Page):
    page.goto("https://demoqa.com")

    # Verify page title
    expect(page).to_have_title("DEMOQA")

    # Click Elements card
    page.locator("text=Elements").click()

    expect(page).to_have_url("https://demoqa.com/elements")