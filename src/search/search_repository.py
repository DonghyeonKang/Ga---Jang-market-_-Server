import pymysql.cursors
import src.security.db_auth as db_auth

class SearchRepository:
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
    
    def getSearchData(self, word):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            sql = "SELECT DISTINCT s_id FROM product WHERE product_name like '%" + word + "%'"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
            return "DB Select Error"
        finally:
            self.closeConnection()