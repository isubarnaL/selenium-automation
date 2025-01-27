import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service

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

driver.quit()
