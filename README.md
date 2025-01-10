# TodoMVC Automation Project

Welcome to the **TodoMVC Automation Project** repository! This project demonstrates a robust approach to automated testing using Selenium, GitHub, and GitHub Actions. It includes a fully functional CI/CD pipeline to ensure the quality and reliability of the TodoMVC React application.

---

## Project Overview

The TodoMVC application is a classic example used to showcase front-end frameworks. This project builds on that by automating its UI testing, ensuring critical features like adding, editing, deleting, and completing tasks work seamlessly.

**Key Objectives:**

- Automate UI tests for the TodoMVC React app.
- Implement CI/CD using GitHub Actions.
- Provide clear and actionable test reports.

---

## Features

- **Realistic User Simulation:** Custom `human_typing` function mimics real-world typing behavior.
- **Comprehensive Test Coverage:** Covers all major interactions, including adding, editing, deleting, and completing tasks.
- **CI/CD Integration:** Automated workflows using GitHub Actions ensure consistent test execution.
- **Beginner-Friendly Setup:** Step-by-step instructions for newcomers to Selenium and GitHub.

---

## Getting Started

### Prerequisites

1. **Python** (Version 3.8 or higher)
2. **Selenium WebDriver**
3. **Google Chrome** and **ChromeDriver**

---

### Step 1: Set Up Your Environment

1. **Install Python:**

   - [Download Python](https://www.python.org/downloads/) and ensure you check "Add Python to PATH" during installation.

2. **Install Selenium:**

   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver:**

   - Use the following ChromeDriver compatible with your version of Google Chrome:
     - ChromeDriver: [Download Here](https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.264/win64/chromedriver-win64.zip) (Version 131.0.6778.264)
   - Unzip and place it in a folder accessible via PATH.

---

### Step 2: Write Your Test Script

1. **Create a Project Folder:**

   ```bash
   mkdir todo_automation
   cd todo_automation
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```

3. **Install Selenium in the Virtual Environment:**

   ```bash
   pip install selenium
   ```

4. **Create the Test Script:**

   - Inside `todo_automation`, create `test_todo.py` with the following content:
     ```python
     from selenium import webdriver
     from selenium.webdriver.common.keys import Keys
     import time

     driver = webdriver.Chrome()
     driver.get("https://todomvc.com/examples/react/")

     input_box = driver.find_element_by_class_name("new-todo")
     input_box.send_keys("Learn Selenium")
     input_box.send_keys(Keys.RETURN)
     time.sleep(2)

     todo_list = driver.find_elements_by_css_selector(".todo-list li")
     assert len(todo_list) > 0, "Todo item was not added."

     driver.quit()
     ```

---

### Step 3: Set Up GitHub

1. **Create a GitHub Account:**

   - Sign up at [GitHub](https://github.com).

2. **Create a New Repository:**

   - Name it `todo_automation` and select Public.
   - Clone it locally:
     ```bash
     git clone https://github.com/your_username/todo_automation.git
     cd todo_automation
     ```

3. **Add and Commit Your Test Script:**

   ```bash
   git add test_todo.py
   git commit -m "Add Selenium test script"
   git push origin main
   ```

---

### Step 4: Configure GitHub Actions

1. **Set Up a Workflow File:**

   - Inside your project folder, create `.github/workflows/test.yml` with the following content:
     ```yaml
     name: Run Selenium Tests

     on:
       push:
         branches:
           - main
       pull_request:
         branches:
           - main

     jobs:
       selenium-tests:
         runs-on: ubuntu-latest

         steps:
         - name: Checkout repository
           uses: actions/checkout@v3

         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.10'

         - name: Install dependencies
           run: |
             python -m pip install --upgrade pip
             pip install selenium

         - name: Download ChromeDriver
           run: |
             sudo apt-get update
             sudo apt-get install -y wget unzip
             wget -N https://chromedriver.storage.googleapis.com/$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
             unzip chromedriver_linux64.zip -d /usr/local/bin

         - name: Install Google Chrome
           run: |
             wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
             sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
             sudo apt-get update
             sudo apt-get install -y google-chrome-stable

         - name: Run Selenium tests
           run: |
             python test_todomvc.py
     ```

2. **Commit and Push the Workflow File:**

   ```bash
   git add .github/workflows/test.yml
   git commit -m "Add GitHub Actions workflow"
   git push origin main
   ```

---

### Step 5: Run the Workflow

1. **Navigate to the Actions Tab:**

   - In your GitHub repository, go to the Actions tab.
   - Observe the workflow running upon the latest push.

2. **Review the Test Results:**

   - Check the logs to verify the tests' success or failure.

---

### Step 6: Document and Deliver

1. **Code Repository:**

   - Ensure the repository contains `test_todomvc.py` and `.github/workflows/test.yml`.

2. **Test Results:**

   - Summarize:
     - What the test does.
     - Results (pass/fail).
     - CI/CD pipeline setup.

3. **Enhancements:**

   - Highlight how CI/CD strengthens test reliability and expedites the development cycle.

---

## Additional Resources

- [**Intro to GitHub Actions**](https://docs.github.com/en/actions)
- [**Selenium Documentation**](https://www.selenium.dev/documentation/)
- [**GitHub Actions Tutorial for Beginners**](https://www.youtube.com/watch?v=R8_veQiYBjI)

