from plyer import notification

def display_notification(message):
    notification.notify(
        title="POPUP Notification",
        message=message,
        app_name="APP NOTIFICATION",
        timeout=10
    )

if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    display_notification(user_input)
