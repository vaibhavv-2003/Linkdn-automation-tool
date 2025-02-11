from utils import load_config, is_test_mode
from Linkdn_login import linkedin_login
from search_jobstool import search_jobs, extract_job_description
from send import send_message
from witai import get_witai_message
from gemini_integration import generate_cold_message_gemini

# Load the configuration
config = load_config()

# Check if in test mode
if is_test_mode(config):
    print("Running in test mode. No messages or resumes will be sent.")
else:
    # Log into LinkedIn
    driver = linkedin_login(config['linkedin_email'], config['linkedin_password'])

    # Search for jobs using the keyword and location from config
    search_jobs(driver, config['job_keyword'], config['location'])

    # Extract the job description of the first job posting
    job_description = extract_job_description(driver)
    if job_description:
        print(f"Extracted Job Description:\n{job_description}")

        # Generate a personalized message using the preferred API
        if config.get("use_witai"):
            cold_message = get_witai_message(job_description)
        elif config.get("use_gemini"):
            cold_message = generate_cold_message_gemini(config['google_gemini_api_key'], job_description)
        else:
            cold_message = config["cold_message"]  # Default message

        # Send the personalized cold message
        send_message(driver, cold_message, config['resume_path'])

    else:
        print("No job description found. Please check the job search process.")

    # Close the browser
    driver.quit()
