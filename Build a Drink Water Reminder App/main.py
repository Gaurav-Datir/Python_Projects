import time   
from plyer import notification

while True:
    print("Please sip some water!")  
    notification.notify(title="Please drink some water", 
                        message = "You need to drink some water",)
    time.sleep(3600)  # Wait for 1 hour (3600 seconds) before reminding again