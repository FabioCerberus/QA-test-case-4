import time
from playwright.sync_api import sync_playwright, expect


def test_register_user_successfully():
    username = "Fabio Test"
    email = f"fabio_test_2{int(time.time())}@example.com"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Launch browser
        # Browser is launched above.

        # 2. Navigate to url 'http://automationexercise.com'
        page.goto("https://automationexercise.com/")

        # 3. Verify that home page is visible successfully
        expect(page).to_have_title("Automation Exercise")

        # 4. Click on 'Signup / Login' button
        page.get_by_role("link", name="Signup / Login").click()

        # 5. Verify 'New User Signup!' is visible
        expect(page.get_by_text("New User Signup!")).to_be_visible()

        # 6. Enter name and email address
        page.locator('[data-qa="signup-name"]').fill(username)
        page.locator('[data-qa="signup-email"]').fill(email)

        # 7. Click 'Signup' button
        page.locator('[data-qa="signup-button"]').click()

        # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
        expect(page.get_by_text("Enter Account Information")).to_be_visible()

        # 9. Fill details: Title, Name, Email, Password, Date of birth
        page.locator("#id_gender1").check()
        page.locator('[data-qa="password"]').fill("Password123!")

        page.locator('[data-qa="days"]').select_option("10")
        page.locator('[data-qa="months"]').select_option("5")
        page.locator('[data-qa="years"]').select_option("1995")

        # 10. Select checkbox 'Sign up for our newsletter!'
        page.locator("#newsletter").check()

        # 11. Select checkbox 'Receive special offers from our partners!'
        page.locator("#optin").check()

        # 12. Fill details: First name, Last name, Company, Address, Address2,
        # Country, State, City, Zipcode, Mobile Number
        page.locator('[data-qa="first_name"]').fill("Fabio")
        page.locator('[data-qa="last_name"]').fill("Lacerda")
        page.locator('[data-qa="company"]').fill("QA Study")
        page.locator('[data-qa="address"]').fill("123 Test Street")
        page.locator('[data-qa="address2"]').fill("Apartment 45")
        page.locator('[data-qa="country"]').select_option("United States")
        page.locator('[data-qa="state"]').fill("California")
        page.locator('[data-qa="city"]').fill("Los Angeles")
        page.locator('[data-qa="zipcode"]').fill("90001")
        page.locator('[data-qa="mobile_number"]').fill("1234567890")

        # 13. Click 'Create Account button'
        page.locator('[data-qa="create-account"]').click()

        # 14. Verify that 'ACCOUNT CREATED!' is visible
        expect(page.get_by_text("Account Created!")).to_be_visible()

        # 15. Click 'Continue' button
        page.locator('[data-qa="continue-button"]').click()

        # 16. Verify that 'Logged in as username' is visible
        expect(page.get_by_text(f"Logged in as {username}")).to_be_visible()

        # 17. Click 'Delete Account' button
        page.get_by_role("link", name="Delete Account").click()

        # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
        expect(page.get_by_text("Account Deleted!")).to_be_visible()
        page.locator('[data-qa="continue-button"]').click()

        browser.close()