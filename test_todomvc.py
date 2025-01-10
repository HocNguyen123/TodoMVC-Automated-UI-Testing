from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configure Chrome options for headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize the Chrome driver with options
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

# Open the TodoMVC React demo
driver.get("https://demo.playwright.dev/todomvc/#/active")

def human_typing(element, text, delay=0.0):
    """Simulates human typing by sending each character with a delay."""
    for char in text:
        element.send_keys(char)
        time.sleep(delay)  # Wait for the specified delay between keystrokes

# Test 1: Add four todos
def test_add_four_todos():
    todo_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "new-todo")))
    todos = ["Task 1", "Task 2", "Task 3", "Task 4"]
    for todo in todos:
        human_typing(todo_input, todo)  # Use human_typing for each task
        todo_input.send_keys(Keys.RETURN)
        time.sleep(1)  # Allow time for the task to be added
    # Wait for all tasks to appear in the DOM
    wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".todo-list li")) == 4)
    print("Test 1 Passed: Added four todos.")

# Test 2: Edit the second task
def test_edit_second_task():
    # Locate the second task label
    todo_item = wait.until(EC.presence_of_element_located((By.XPATH, "(//ul[@class='todo-list']//li//label)[2]")))
    
    # Scroll the item into view
    driver.execute_script("arguments[0].scrollIntoView();", todo_item)
    
    # Double-click on the task to enter edit mode
    actions = ActionChains(driver)
    actions.double_click(todo_item).perform()
    
    # Add a short wait for the input field to become editable
    time.sleep(1)  # Sometimes required due to animation or rendering delays
    
    # Locate the input field for the editing mode
    edit_input = wait.until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'editing')]//input[@class='edit']")))
    
    # Simulate manual backspacing to clear the original text
    current_text = edit_input.get_attribute("value")
    for _ in range(len(current_text)):
        edit_input.send_keys(Keys.BACKSPACE)
    
    # Type the new text
    human_typing(edit_input, "Edited Task 2")  # Use human_typing for realistic input
    edit_input.send_keys(Keys.RETURN)
    
    # Verify the updated text
    updated_task = wait.until(EC.text_to_be_present_in_element((By.XPATH, "(//ul[@class='todo-list']//li//label)[2]"), "Edited Task 2"))
    print("Test 2 Passed: Edited the second task.")

# Test 3: Delete the third task
def test_delete_third_task():
    # Locate all tasks in the todo list
    todo_list = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, ".todo-list li"))
    
    # Hover over the third task to reveal the delete button
    third_task = todo_list[2]  # Third task (index 2)
    actions = ActionChains(driver)
    actions.move_to_element(third_task).perform()
    
    # Locate and click the delete button for the third task
    delete_button = third_task.find_element(By.CLASS_NAME, "destroy")
    driver.execute_script("arguments[0].click();", delete_button)  # Use JavaScript click to avoid hover issues
    
    # Wait for the third task to be removed
    time.sleep(1)
    wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".todo-list li")) == 3)
    print("Test 3 Passed: Deleted the third task.")

# Test 4: Complete the fourth task
def test_complete_fourth_task():
    try:
        # Wait for all tasks to load
        todo_list = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, ".todo-list li"))
        
        # Ensure there are at least 3 tasks (since Task 3 was deleted)
        if len(todo_list) < 3:
            raise Exception("Not enough tasks to complete the last task. Found only {} tasks.".format(len(todo_list)))
        
        # Locate the last task's checkbox (index 2 after Task 3 deletion)
        last_task_checkbox = todo_list[2].find_element(By.CSS_SELECTOR, "input.toggle")
        
        # Click the checkbox to mark the task as completed
        last_task_checkbox.click()
        
        # Wait for the "Clear completed" button to become visible and clickable
        clear_completed_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Clear completed']")))
        
        # Click the "Clear completed" button
        clear_completed_button.click()
        
        # Verify that the completed task is no longer in the list
        remaining_tasks = wait.until(lambda driver: driver.find_elements(By.CSS_SELECTOR, ".todo-list li"))
        assert len(remaining_tasks) == 2, f"Expected 2 tasks remaining, but found {len(remaining_tasks)}."
        print("Test 4 Passed: Completed and cleared the last task.")
        
    except Exception as e:
        print(f"Test 4 Failed: {e}")
        raise


# Run all tests
try:
    test_add_four_todos()
    test_edit_second_task()
    test_delete_third_task()
    test_complete_fourth_task()
    print("All tests passed successfully!")
except Exception as e:
    print(f"Test failed: {e}")
finally:
    driver.quit()
