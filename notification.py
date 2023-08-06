from plyer import notification

def display_notification(message):
    notification.notify(
        title="POPUP Notification",
        message=message,
        app_name="APP NOTIFICATION",
        timeout=10
    )


