import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# --------------- INITALIZE SELENIUM & WEBPAGE REQUEST ----------------- #
chrome_driver_path = os.environ.["CHROMEPATHDRIVER"]
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/feed/")
driver.maximize_window()


# ------------------ LOGIN TO LINKEDIN -------------------- #
driver.find_element(By.CLASS_NAME, "main__sign-in-link").click()

time.sleep(2)

username = driver.find_element(By.ID, "username")
username.send_keys(os.environ["USERNAME"])
password = driver.find_element(By.ID, "password")
password.send_keys(os.environ["PASSWORD"])

time.sleep(2)

driver.find_element(By.CLASS_NAME, "btn__primary--large").click()

time.sleep(3)


# ---------------- CLOSE MESSAGE BOX-------------- #
message_box_button = driver.find_elements(By.CLASS_NAME, "msg-overlay-bubble-header__control")
message_box_button[1].click()

time.sleep(2)


# ---------------- SEARCH FOR PYTHON DEVELOPER JOBS  -------------- #
jobs_filter = driver.find_element(By.LINK_TEXT, "Jobs")
jobs_filter.click()

time.sleep(5)

search_bar = driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__inner .relative input")
search_bar.send_keys("python developer")

time.sleep(2)

submit_button = driver.find_element(By.CLASS_NAME, "jobs-search-box__submit-button")
submit_button.click()

time.sleep(2)


# ---------------- EASY APPLY FILTER  -------------- #
easy_apply_filter = driver.find_element(By.XPATH, "//button[@aria-label='Easy Apply filter.']").click()

time.sleep(5)


# # ------------------ APPLY FOR POSITIONS ---------------- #
job_postings = driver.find_elements(By.CLASS_NAME, "job-card-container")

for job in job_postings:

    # CLICK ON JOB POSTING
    job.click()
    time.sleep(3)

    # CLICK ON EASY APPLY BUTTON
    try:
        easy_apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        easy_apply_button.click()
        time.sleep(3)

        # SUBMIT APPLICATION PROCESS
        try:
            # CLICK SUBMIT APPLICATION BUTTON
            submit_application_button = driver.find_element(By.XPATH, "//button[@aria-label='Submit application']")
            submit_application_button.click()
            time.sleep(5)

            # ONCE JOB APPLICATION IS SUCCESSFUL, IF THERE ARE ANY POP-UP WINDOWS, CLOSE THEM!
            try:
                driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
            except NoSuchElementException:
                pass

        # EXIT APPLICATION PROCESS IF THERE IS A "NEXT" BUTTON
        except NoSuchElementException:
            # CLICK ON "X" TO DISCARD APPLICATION
            driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']").click()
            time.sleep(1)

            # CONFIRM DISCARDING THE APPLICATION
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
            discard_button[1].click()
            time.sleep(2)

    # IF NO EASY APPLY BUTTON, CONTINUE
    except NoSuchElementException:
        continue

time.sleep(5)
driver.quit()
