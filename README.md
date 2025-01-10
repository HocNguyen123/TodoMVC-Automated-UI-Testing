# TodoMVC-Automated-UI-Testing

Welcome to the **Automated Testing for TodoMVC** project! This repository features a suite of automated tests designed to ensure the functionality and reliability of the TodoMVC application, specifically its React implementation. Below, you'll find details about the project, how to run the tests, and insights into its design and objectives.

---

## Project Overview

The **TodoMVC React demo** is a widely recognized application used to demonstrate the architecture and design patterns of various front-end frameworks. This project automates the end-to-end testing of core functionalities, including:

- Adding tasks
- Editing tasks
- Deleting tasks
- Completing tasks

These tests simulate real-world user interactions, ensuring the TodoMVC app performs as expected in various scenarios.

---

## Key Features

- **Human-like Typing Simulation**: Tests use a custom `human_typing` function to replicate realistic typing speeds.
- **Comprehensive Coverage**: Covers adding, editing, deleting, and completing tasks to test the app's critical features.
- **Efficient Element Handling**: Utilizes Selenium's robust waiting and element handling mechanisms to ensure stable and reliable test execution.
- **Clear and Actionable Feedback**: Test results provide straightforward pass/fail status with detailed descriptions for easy debugging.

---

## Installation and Setup

### Prerequisites

1. Python 3.x
2. Selenium WebDriver
3. Google Chrome and ChromeDriver

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/todomvc-automation.git
   cd todomvc-automation
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure ChromeDriver is in your system's PATH.

---

## Running the Tests

Execute the test suite with the following command:
```bash
python test_todomvc.py
```
The script will:
- Open the TodoMVC React demo in Chrome.
- Execute four tests sequentially, providing real-time feedback on the results.

---

## Test Descriptions

1. **Add Four Todos**
   - Adds four tasks to the list and verifies their presence.
   - Output: "Test 1 Passed: Added four todos."

2. **Edit the Second Task**
   - Modifies the second task and ensures the change is saved.
   - Output: "Test 2 Passed: Edited the second task."

3. **Delete the Third Task**
   - Removes the third task from the list and verifies its deletion.
   - Output: "Test 3 Passed: Deleted the third task."

4. **Complete and Clear the Last Task**
   - Marks the last task as complete, clears it, and verifies the remaining tasks.
   - Output: "Test 4 Passed: Completed and cleared the last task."

