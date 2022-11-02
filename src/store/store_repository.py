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
    
    # 매장 조회
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
    
    # 내 매장 조회
    def getMyStoreData(self, merchantId):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [merchantId]
            cursor.execute("SELECT * FROM store WHERE id IN (SELECT s_id FROM management WHERE um_id=(SELECT id FROM users_merchant WHERE user_id=%s))", arr)
            rows = cursor.fetchall()
            print(rows)
            return rows
        except Exception as e:
            print(e)
            return "DB Select Error"
        finally:
            self.closeConnection()

    # 매장 이미지 조회
    def getStoreImage(self, storeId):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [storeId]
            cursor.execute("SELECT img_path FROM store_img WHERE s_id=%s", arr)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
            return "DB Select Error"
        finally:
            self.closeConnection()

    # 매장 등록
    def addStore(self, data, imgArr):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [data['market_id'], data['store_name'], data['info'], data['store_type'], data['open_time'], data['close_time'], data['latitude'], data['longitude'], data['category'], data['phone']]
            cursor.execute("INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time, latitude, longitude, category, phone) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", arr)
            self.connection.commit()

            # 등록한 매장의 store_id를 가져옵니다. 
            arr = [data['market_id'], data['store_name']]
            cursor.execute("SELECT id FROM store WHERE m_id=%s AND store_name=%s", arr)
            storeId = cursor.fetchall()

            # 이미지 등록
            for i in imgArr:
                arr = [storeId[0]['id'], i['image']] # s_id, i
                cursor.execute("INSERT INTO store_img(s_id, img_path) VALUES(%s, %s)", arr)
                self.connection.commit()
            
            # 관계 등록
            arr = [data['merchant_id'], storeId[0]['id']]
            print(arr)
            cursor.execute("INSERT INTO management(um_id, s_id) VALUES((SELECT id FROM users_merchant WHERE user_id=%s), %s)", arr)
            self.connection.commit()

            return "success"
        except Exception as e:
            print(e)
            return "DB INSERT Error"
        finally:
            self.closeConnection()

    # 매장 수정
    def updateStore(self, data, imgArr):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            # 텍스트 데이터 업데이트
            arr = [data['store_name'], data['info'], data['store_type'], data['open_time'], data['close_time'], data['latitude'], data['longitude'], data['phone'], data['store_id']]
            cursor.execute("UPDATE store SET store_name=%s, info=%s, store_type=%s, open_time=%s, close_time=%s, latitude=%s, longitude=%s, phone=%s WHERE id=%s", arr)
            self.connection.commit()
            storeId = data['store_id']

            # 기존 사진 삭제
            arr = [storeId]
            cursor.execute("DELETE FROM store_img WHERE s_id=%s", arr)
            self.connection.commit()

            # 이미지 등록
            for i in imgArr:
                arr = [str(storeId), i['image']] # s_id, i
                cursor.execute("INSERT INTO store_img(s_id, img_path) VALUES(%s, %s)", arr)
                self.connection.commit()
            return "success"
        except Exception as e:
            print(e)
            return "DB INSERT Error"
        finally:
            self.closeConnection()

    # 매장 삭제
    def deleteStore(self, storeId):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [storeId]
            # 텍스트 데이터 삭제
            cursor.execute("DELETE FROM store WHERE id=%s", arr)
            self.connection.commit()
            
            # 이미지 데이터 삭제
            cursor.execute("DELETE FROM store_img WHERE s_id=%s", arr)
            self.connection.commit()

            # management 삭제
            cursor.execute("DELETE FROM management WHERE s_id=%s", arr)
            self.connection.commit()

            return "success"
        except Exception as e:
            print(e)
            return "DB delete Error"
        finally:
            self.closeConnection()