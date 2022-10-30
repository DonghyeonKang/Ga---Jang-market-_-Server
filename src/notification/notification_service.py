import src.notification.notification_repository as notification_repository
from pyfcm import FCMNotification

push_tokens = ""
message_title = ""
message_body = ""

push_service = FCMNotification(api_key=conf["fcm"]["key"])
result = push_service.notify_multiple_devices(registration_ids=push_tokens, message_title=message_title, message_body=message_body)
result = push_service.notify_single_device(registration_id=push_tokens, message_title=message_title, message_body=message_body)
result = push_service.notify_single_device(registration_id=push_tokens, message_title=message_title, message_body=message_body,data_message=data)

class NotificationService:
    reservationRepository = notification_repository.ReservationRepository()

    def __init__(self) -> None:
        pass

    # 예약 리스트
    def getReservation(self, user_id):
        result = self.notification_repository.getReservationData(user_id)
        return result
