from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def search_jobs(driver, job_keyword, location):
    """
    Searches for jobs on LinkedIn based on the provided keyword and location.

    :param driver: Selenium WebDriver instance.
    :param job_keyword: The job keyword to search for.
    :param location: The location to search in.
    """
    try:
        # Navigate to the LinkedIn jobs page
        driver.get("https://www.linkedin.com/jobs/")

        # Wait for the search input field to be present
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Search jobs')]"))
        )
        search_input.clear()
        search_input.send_keys(job_keyword)

        # Wait for the location input field to be present
        location_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Location')]"))
        )
        location_input.clear()
        location_input.send_keys(location)

        # Wait for the search button to be clickable
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'jobs-search-box__submit-button')]"))
        )
        search_button.click()

        # Wait for the results page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'jobs-search__results-list')]"))
        )

        print("Job search initiated successfully.")
    except TimeoutException:
        print("Timeout while waiting for the search button or input fields.")
    except Exception as e:
        print(f"An error occurred during job search: {e}")

def extract_job_description(driver):
    """
    Extracts the job description from the first job posting.

    :param driver: Selenium WebDriver instance.
    :return: Job description text or None if not found.
    """
    try:
        # Locate the first job in the results
        first_job = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ul[contains(@class, 'jobs-search__results-list')]/li[1]"))
        )
        first_job.click()
        print("Clicked on the first job posting.")

        # Wait for the job description to load
        job_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'jobs-description')]"))
        )
        return job_description.text
    except NoSuchElementException:
        print("Job description element not found.")
        return None
    except Exception as e:
        print(f"Error extracting job description: {e}")
        return None
