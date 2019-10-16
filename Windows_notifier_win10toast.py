from win10toast import ToastNotifier
import time

# One-time initialization
toaster = ToastNotifier()

# Show notification whenever 
notification_heading = "Notification Test"
notification_body = "Test message"

# Show the notification
toaster.show_toast(notification_heading, notification_body, threaded=True,
                   icon_path=None, duration=3)  # Duration is 3 seconds here

# To check if any notifications are active,
# use `toaster.notification_active()`
# while toaster.notification_active():
#     time.sleep(0.1)