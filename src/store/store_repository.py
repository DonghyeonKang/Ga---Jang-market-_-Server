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