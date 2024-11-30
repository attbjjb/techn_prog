from abc import ABC, abstractmethod

class NotificationHandler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle_notification(self, message):
        pass

class SMSHandler(NotificationHandler):
    def handle_notification(self, message):
        if self._can_send_sms():
            print(f"Отправка SMS: {message}")
        elif self._successor:
            self._successor.handle_notification(message)

    def _can_send_sms(self):
        return False

class EmailHandler(NotificationHandler):
    def handle_notification(self, message):
        if self._can_send_email():
            print(f"Отправка Email: {message}")
        elif self._successor:
            self._successor.handle_notification(message)

    def _can_send_email(self):
        return True

class MessengerHandler(NotificationHandler):
    def handle_notification(self, message):
        if self._can_send_messenger():
            print(f"Отправка через мессенджер: {message}")
        elif self._successor:
            self._successor.handle_notification(message)

    def _can_send_messenger(self):
        return False

# Пример использования
sms_handler = SMSHandler()
email_handler = EmailHandler(sms_handler)
messenger_handler = MessengerHandler(email_handler)

messenger_handler.handle_notification("Важное уведомление!")