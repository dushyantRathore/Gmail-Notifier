from plyer import notification

notification.notify(
    title = "Notification Test",
    message = "Test message",
    app_icon = None,  # e.g. 'C:\\icon_32x32.ico'
    timeout = 5,  # seconds
)