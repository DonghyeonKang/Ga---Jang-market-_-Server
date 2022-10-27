import src.notification.notification_repository as notification_repository

class NotificationService:
    reservationRepository = notification_repository.ReservationRepository()

    def __init__(self) -> None:
        pass

    # 예약 리스트
    def getReservation(self, user_id):
        result = self.notification_repository.getReservationData(user_id)
        return result
