import pymysql.cursors
import src.security.db_auth as db_auth

class ReservationRepository:
    def __init__(self) -> None:
        self.login = db_auth.db_login

    def getConnection(self):
        self.connection = pymysql.connect(host=self.login['host'],
                                     user=self.login['user'],
                                     password=self.login['password'],
                                     db=self.login['db'],
                                     charset=self.login['charset'],
                                     cursorclass=pymysql.cursors.DictCursor)

    def closeConnection(self):
        self.connection.close()

    # 예약 리스트
    def getReservation(self):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = []
            cursor.execute("SELECT * FROM product WHERE s_id=(SELECT id FROM store WHERE store_name=%s)", arr)
            rows = cursor.fetchall()
            if len(rows) == 0:
                return "DB Select Error"
            else:
                return rows
        except Exception as e:
            print(e)
            return "DB Select Error"
        finally:
            self.closeConnection()

    # 예약하기
    def addReservation(self, dataArr):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO reservation(uc_id, um_id, p_id, s_id, reservation_time, price, count, approval) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", dataArr)
            self.connection.commit()
            arr = dataArr[:4]
            cursor.execute("SELECT id FROM reservation WHERE uc_id=%s AND um_id=%s AND p_id=%s AND s_id=%s", arr)
            rows = cursor.fetchall()
            return rows[0]
        except Exception as e:
            print(e)
            return "DB Select Error"
        finally:
            self.closeConnection()

    # 취소하기
    def deleteReservation(self, reservation_id):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [reservation_id]
            cursor.execute("DELETE FROM reservation WHERE id=%s", arr)
            return "success"
        except Exception as e:
            print(e)
            return "DB delete Error"
        finally:
            self.closeConnection()
    # 수락하기
    def acceptReservation(self, reservation_id):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [reservation_id]
            cursor.execute("UPDATE reservation SET approval=1 WHERE id=%s", arr)
            rows = cursor.fetchall()
            if len(rows) == 0:
                return "DB Select Error"
            else:
                return rows
        except Exception as e:
            print(e)
            return "DB Select Error"
        finally:
            self.closeConnection()

    # 거절하기
    def rejectReservation(self, reservation_id):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [reservation_id]
            cursor.execute("UPDATE reservation SET approval=0 WHERE id=%s", arr)
            rows = cursor.fetchall()
            if len(rows) == 0:
                return "DB Select Error"
            else:
                return rows
        except Exception as e:
            print(e)
            return "DB Select Error"
        finally:
            self.closeConnection()