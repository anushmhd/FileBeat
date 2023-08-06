from plyer import notification

def display_notification(message):
    notification.notify(
        title="FileBeat",
        message=message,
        app_name="FileBeat",
        timeout=10
    )


