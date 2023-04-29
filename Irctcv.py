from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import base64
import os
from google.cloud import vision_v1

print("Welcome to Vaibhav's train booking system....")
username = ("")
password = ("")

print("You will be redirected to the site for searching trains....")

driver = webdriver.Chrome()
driver.get('https://www.irctc.co.in/nget/train-search')
time.sleep(1)
driver.maximize_window()

time.sleep(1)

driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[1]/a[1]').click()
time.sleep(1)

# Find the username input field by searching for its placeholder text
username_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="User Name"]')

# Enter the username
username_input.send_keys(username)

# Find the password input field by searching for its placeholder text
password_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]')

# Enter the password
password_input.send_keys(password)



# Set up authentication with Google Cloud using API key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/vaibhav/Desktop/python/advance-wavelet-385212-6e0fa109b948.json'

# Instantiates a client
client = vision_v1.ImageAnnotatorClient()

# Find the image element and extract the base64 encoded image string
img_element = driver.find_element(By.CSS_SELECTOR, '.captcha-img')
img_base64 = img_element.get_attribute('src')

# Decode base64 string and read as bytes
img_bytes = base64.b64decode(img_base64.split(',')[1])

# Construct an image instance
image = vision_v1.types.Image(content=img_bytes)

# Perform text detection on the image
response = client.text_detection(image=image)

# Print the detected text
if response.text_annotations and response.text_annotations[0].description:
    captcha_text = response.text_annotations[0].description
else:
    captcha_text = ''

# Assuming you have already found the captcha input field
captcha_input = driver.find_element(By.ID, 'captcha')

# Send the text to the captcha input field
captcha_input.send_keys(captcha_text)
time.sleep(3)
print(captcha_text)


# Wait for the button to be clickable
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='SIGN IN']")))

# Click the button
button.click()
time.sleep(10)



# Find the first input field
input_field1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-controls="pr_id_1_list"]'))
)

# Type in the value
input_field1.send_keys("GHAZIABAD - GZB")


# Find the second input field
input_field2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-controls="pr_id_2_list"]'))
)

# Type in the value
input_field2.send_keys("LUCKNOW NR - LKO")
time.sleep(1)



# Click on the calendar input field to open the calendar
calendar_input = driver.find_element(By.CSS_SELECTOR, 'span.ng-tns-c58-10 input[type="text"]')
calendar_input.click()

# Delete existing date in the input box
existing_date = calendar_input.get_attribute("value")
for i in range(len(existing_date)):
    calendar_input.send_keys(Keys.BACKSPACE)


# Fill the new date in the calendar
calendar_input.send_keys("04/05/202")


# wait for the dropdown Quota to be clickable
dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "journeyQuota")))

# click the dropdown to open it
dropdown.click()

# wait for the desired option to be clickable and click it
option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[@aria-label='GENERAL']")))
option.click()



# click on the search button
search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[5]/div/button')))
search_button.click()




time.sleep(1)
print("Currently above trains are available")
choice = ("15")
passenger_name = ("Nisha Srivastava")
age = ("43")
gender = ("F")
print("Now you will be again redirected to the IRCTC website for booking.......")
time.sleep(1)
driver.maximize_window()

# class selection
class_xpath = '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[{}]/div[1]/app-train-avl-enq/div[1]/div[5]/div/table/tr/td[1]/div'.format(choice)
driver.find_element(By.XPATH, class_xpath).click()

# Wait for the element to be clickable
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'td.link.ng-star-inserted'))
)

# Click on the element
element.click()

# book now
book_xpath = '//*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[{}]/div[1]/app-train-avl-enq/div[2]/div/span/span/button[1]'.format(choice)
driver.find_element(By.XPATH, book_xpath).click()
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input').send_keys(passenger_name) #passenger name
driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input').send_keys(age)  #age
element1 = Select(driver.find_element(By.XPATH, '//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select'))  #gender dropdown

if gender=='M':
    element1.select_by_index(1)
elif gender=='F':
    element1.select_by_index(2)
else:
    print("invalid input for gender")

# Wait for the radio button to be clickable
radiobutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "2")))

# Click the radio button
radiobutton.click()


# Wait for the button to be clickable to captcha
continue_button = WebDriverWait(driver, 100).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.train_Search.btnDefault"))
)

# Click the button
continue_button.click()
time.sleep(30)



# Set up authentication with Google Cloud using API key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/vaibhav/Desktop/python/advance-wavelet-385212-6e0fa109b948.json'

# Instantiates a client
client = vision_v1.ImageAnnotatorClient()

# Find the image element and extract the base64 encoded image string
img_element = driver.find_element(By.CSS_SELECTOR, '.captcha-img')
img_base64 = img_element.get_attribute('src')

# Decode base64 string and read as bytes
img_bytes = base64.b64decode(img_base64.split(',')[1])

# Construct an image instance
image = vision_v1.types.Image(content=img_bytes)

# Perform text detection on the image
response = client.text_detection(image=image)

# Print the detected text
if response.text_annotations and response.text_annotations[0].description:
    captcha_text = response.text_annotations[0].description
else:
    captcha_text = ''

# Assuming you have already found the captcha input field
captcha_input = driver.find_element(By.ID, 'captcha')

# Send the text to the captcha input field
captcha_input.send_keys(captcha_text)
print(captcha_text)
time.sleep(3)



# Wait for the button to be clickable to payment selection
continue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.train_Search.btnDefault"))
)

# Click the button
continue_button.click()
time.sleep(1000)


driver.quit() # add parentheses after quit() function call

