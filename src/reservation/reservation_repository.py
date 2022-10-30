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
    def getReservation(self, user_id):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [user_id]
            cursor.execute("SELECT * FROM reservation WHERE uc_id=%s", arr)
            rows = cursor.fetchall()
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
            arr = [dataArr[0]]
            cursor.execute("SELECT id FROM users_customer WHERE user_id=%s", arr)
            rows = cursor.fetchall()
            print(rows)
            dataArr[0] = rows[0]['id']

            arr = [dataArr[1]]
            cursor.execute("SELECT id FROM users_merchant WHERE user_id=%s", arr)
            rows = cursor.fetchall()
            print(rows)
            dataArr[1] = rows[0]['id']

            cursor.execute("INSERT INTO reservation(uc_id, um_id, p_id, s_id, reservation_time, price, count, approval) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", dataArr)
            self.connection.commit()
            arr = dataArr[:4]
            cursor.execute("SELECT id FROM reservation WHERE uc_id=%s AND um_id=%s AND p_id=%s AND s_id=%s", arr)
            rows = cursor.fetchall()
            print(rows)
            return rows
        except Exception as e:
            print(e)
            return "DB Insert Error"
        finally:
            self.closeConnection()

    # 취소하기
    def deleteReservation(self, reservation_id):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [reservation_id]
            cursor.execute("DELETE FROM reservation WHERE id=%s", arr)
            self.connection.commit()
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
            self.connection.commit()
            return "success"
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
            self.connection.commit()
            return "success"
        except Exception as e:
            print(e)
            return "DB Select Error"
        finally:
            self.closeConnection()