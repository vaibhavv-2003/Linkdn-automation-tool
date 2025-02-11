from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from witai import get_witai_message  # Import your Wit.ai integration

def send_message(driver, job_title, company_name, resume_path):
    try:
        # Generate a personalized cold message using Wit.ai
        cold_message = get_witai_message(f"Write a personalized cold message for a {job_title} position at {company_name}")

        # Locate and click the message button
        message_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Message")]'))
        )
        message_button.click()

        # Locate the message input box and send the Wit.ai-generated message
        message_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@role="textbox"]'))
        )
        message_input.send_keys(cold_message)

        # Optionally, attach the resume
        attach_button = driver.find_element(By.XPATH, '//button[contains(@aria-label, "Attach")]')
        attach_button.click()
        driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(resume_path)

        print(f"Message sent successfully to {company_name} for {job_title} position.")

    except Exception as e:
        print(f"Error during sending message: {e}")
