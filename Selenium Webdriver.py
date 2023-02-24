from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to a web page
driver.get("https://www.amazon.com/")

# Get the page title
title = driver.title

# Print the page title
print(title)


def test_register_new_user():
    # Navigate to registration page
    driver.get(
        "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3F_encoding%3DUTF8%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

    # Enter valid user details
    driver.find_element("Your Name").send_keys("Vignesh")
    driver.find_element("email").send_keys("vignesh.navaladi@gmail.@gmail.com")
    driver.find_element("password").send_keys("new123")
    driver.find_element("confirm_password").send_keys("new123")
    driver.find_element("submit").click()

    # Verify successful registration message
    success_message = driver.find_element("success-message").text
    assert "Registration successful" in success_message
    print("Registration successful")


def test_login():
    # Navigate to login page
    driver.get(
        "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

    # Enter valid credentials
    driver.find_element("Email or mobile phone number ").send_keys("vignesh.navaladi@gmail.@gmail.com")
    driver.find_element("Password").send_keys("new123")
    driver.find_element("Sign In").click()

    # Verify successful login message and user is redirected to the home page
    success_message = driver.find_element("success-message").text
    assert "Login successful" in success_message
    assert "https://www.amazon.com/" in driver.current_url
    print("Login successful")


def test_add_to_cart():
    # Navigate to product page
    driver.get("https://www.amazon.in/NECA-Homelander-Ultimate-Action-Figure/dp/B098MRLRTG/ref=sr_1_4?crid=2DIZUR1M3TX0S&keywords=Homelander&qid=1677227973&sprefix=homelande%2Caps%2C845&sr=8-4")

    # Add item to cart
    driver.find_element("add-to-cart").click()

    # Verify item is added to cart and cart count increases
    cart_count = driver.find_element("cart-count").text
    assert cart_count == "1"

    # Navigate to cart page
    driver.get("https://www.amazon.in/cart/smart-wagon?newItems=f8e07d98-7276-48bc-b79a-83f51b01c392,1")

    # Verify item is in cart
    item_name = driver.find_element("item-name").text
    assert item_name == "Product Name"
    print("Added to cart")


def test_checkout():
    # Navigate to cart page
    driver.get("https://www.amazon.in/cart/smart-wagon?newItems=f8e07d98-7276-48bc-b79a-83f51b01c392,1")

    # Click checkout button
    driver.find_element("checkout").click()

    # Enter valid shipping and payment details
    driver.find_element("name").send_keys("Vignesh Navaladi")
    driver.find_element("address").send_keys("123 Main St.")
    driver.find_element("city").send_keys("Anytown")
    driver.find_element("state").send_keys("CA")
    driver.find_element("zip").send_keys("12345")
    driver.find_element("card-number").send_keys("1234567890123456")
    driver.find_element("card-expiry").send_keys("12/24")
    driver.find_element("card-cvc").send_keys("123")
    driver.find_element("place-order").click()

    # Choose a payment method and enter payment information
    payment_method_radio = driver.find_element("//input[@id='credit-card']")
    payment_method_radio.click()
    card_number_input = driver.find_element("//input[@name='card-number']")
    card_number_input.send_keys("1234 5678 9012 3456")
    expiration_month_select = driver.find_element("//select[@name='expiration-month']")
    expiration_month_select.send_keys("01")
    expiration_year_select = driver.find_element("//select[@name='expiration-year']")
    expiration_year_select.send_keys("2025")
    cvv_input = driver.find_element("//input[@name='cvv']")
    cvv_input.send_keys("123")

    # Verify that the payment information is correct
    assert card_number_input.get_attribute("value") == "1234 5678 9012 3456"
    assert expiration_month_select.get_attribute("value") == "01"
    assert expiration_year_select.get_attribute("value") == "2025"
    assert cvv_input.get_attribute("value") == "123"

    # Verify successful order message and user is redirected to the order confirmation page
    success_message = driver.find_element("success-message").text
    assert "Order placed successfully" in success_message
    assert "https://www.amazon.in/NECA-Homelander-Ultimate-Action-Figure/dp/B098MRLRTG/ref=sr_1_4?crid=2DIZUR1M3TX0S&keywords=Homelander&qid=1677227973&sprefix=homelande%2Caps%2C845&sr=8-4" in driver.current_url
    print("Order placed Successfully")


# Close the browser
driver.quit()