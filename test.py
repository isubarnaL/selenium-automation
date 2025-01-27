import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

edge_driver_path = os.path.join("venv", "edgedriver_win32", "msedgedriver.exe")
service = Service(edge_driver_path)

driver = webdriver.Edge(service=service)
driver.get("https://www.linkedin.com")

expected_title = "LinkedIn: Log In or Sign Up"
actual_title = driver.title

if actual_title == expected_title:
    print("Title verification passed.")
else:
    print(f"Title verification failed! Expected: '{expected_title}', but got: '{actual_title}'")

try:
    h1_element = driver.find_element(By.CSS_SELECTOR, "h1[data-test-id='hero__headline']")
    expected_h1_text = "Welcome to your professional community"
    actual_h1_text = h1_element.text

    if actual_h1_text.strip() == expected_h1_text:
        print("<h1> text verification passed!")
    else:
        print(f"<h1> text verification failed! Expected: '{expected_h1_text}', but got: '{actual_h1_text}'")

except NoSuchElementException:
    print("<h1> element not found!")

driver.quit()
