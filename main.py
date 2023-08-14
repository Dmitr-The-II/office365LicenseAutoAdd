import pyautogui
import time

pyautogui.failSafe = True

file_path = "emailAddresses.txt" 
# Initialize an empty list to store the email addresses
email_array = []
# Open the file and read email addresses
with open(file_path, "r") as file:
    for line in file:
        # Remove leading and trailing whitespace characters (like newline)
        email = line.strip()
        # Append the email address to the array
        email_array.append(email)
#out loop
b=0
#lenght of an array
a=len(email_array)
#time to open required tab
time.sleep(5)
#works until last email address
while b < a:
    #inner loop
    i=0
    pyautogui.moveTo(599,801, 3)
    pyautogui.click() 
    pyautogui.moveTo(1225,473, 3)
    pyautogui.click() 
    while i <= 19 :
        pyautogui.write(email_array[b])
        time.sleep(4)
        pyautogui.press('enter')
        time.sleep(1)        
        i += 1
        b +=1
    pyautogui.moveTo(1134,1092, 5)
    pyautogui.click() 
    pyautogui.moveTo(1882,223, 5)
    pyautogui.click() 

