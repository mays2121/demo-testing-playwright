from playwright.sync_api import expect

def test_demoqa_home(page):
    page.goto("https://demoqa.com")    
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)

    # Verify page title
    expect(page).to_have_title("DEMOQA")

    # Click Elements card
    page.locator("text=Elements").click()

    expect(page).to_have_url("https://demoqa.com/elements")