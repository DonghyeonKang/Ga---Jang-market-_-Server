import src.reservation.reservation_repository as reservation_repository

class ReservationService:
    reservationRepository = reservation_repository.ReservationRepository()

    def __init__(self) -> None:
        pass

    # 예약 리스트
    def getReservation(self, customerId):
        result = self.reservationRepository.getReservation(customerId)
        return result

    # 예약하기
    def addReservation(self, inputData, ):
        dataArr = [inputData['user_id'], inputData['merchant_id'], inputData['product_id'], inputData['store_id'],
                 inputData['reservation_time'], inputData['price'], inputData['count'], 0] # user_id, merchant_id, product_id, store_id, reservation_time, price, count, approval순으로
        result = self.reservationRepository.addReservation(dataArr)
        return result

    # 취소하기(고객)
    def deleteReservation(self, reservation_id):
        result = self.reservationRepository.deleteReservation(reservation_id)
        # 리턴 값에 따라 알림 전송
        return result

    # 수락하기
    def acceptReservation(self, reservation_id):
        result = self.reservationRepository.acceptReservation(reservation_id)
        # 리턴 값에 따라 알림 전송
        return result

    # 거절하기(상인)
    def rejectReservation(self, reservation_id):
        result = self.reservationRepository.rejectReservation(reservation_id)
        # return 값에 따라 알림 전송
        return result