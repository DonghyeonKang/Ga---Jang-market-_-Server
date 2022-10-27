from multiprocessing import connection
import pymysql.cursors
import src.security.db_auth as db_auth

class StoreRepository:
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
    
    def getStoreData(self, marketName):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [marketName]
            cursor.execute("SELECT * FROM store WHERE m_id=(SELECT id FROM market WHERE market_name=%s)", arr)
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
    
    def getStoreImage(self, marketID):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [marketID]
            cursor.execute("SELECT * FROM store_img WHERE s_id IN (SELECT id FROM store WHERE m_id=%s)", arr)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
            return "DB Select Error"
        finally:
            self.closeConnection()

    # 상시 매장 등록
    def addPermanentStore(self, data):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = data
            cursor.execute("INSERT INTO store() VALUES()", arr)
            self.connection.commit()
            return "success"
        except Exception as e:
            print(e)
            return "DB INSERT Error"
        finally:
            self.closeConnection()

    # 상시 매장 수정
    def updatePermanentStore(self, data):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = data
            cursor.execute("", arr)
            self.connection.commit()
            return "success"
        except Exception as e:
            print(e)
            return "DB Update Error"
        finally:
            self.closeConnection()

    # 상시 매장 삭제
    def deletePermanentStore(self, storeID):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [storeID]
            cursor.execute("", arr)
            self.connection.commit()
            return "success"
        except Exception as e:
            print(e)
            return "DB delete Error"
        finally:
            self.closeConnection()

    # 일일 매장 등록
    def addOneDayStore(self, data):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = data
            cursor.execute("INSERT INTO store() VALUES()", arr)
            self.connection.commit()
            return "success"
        except Exception as e:
            print(e)
            return "DB INSERT Error"
        finally:
            self.closeConnection()

    # 상시 매장 수정
    def updateOneDayStore(self, data):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = data
            cursor.execute("", arr)
            self.connection.commit()
            return "success"
        except Exception as e:
            print(e)
            return "DB Update Error"
        finally:
            self.closeConnection()

    # 일일 매장 삭제
    def deleteOneDayStore(self, storeID):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [storeID]
            cursor.execute("", arr)
            self.connection.commit()
            return "success"
        except Exception as e:
            print(e)
            return "DB delete Error"
        finally:
            self.closeConnection()
