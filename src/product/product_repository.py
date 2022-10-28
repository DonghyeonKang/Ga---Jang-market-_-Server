import pymysql.cursors
import src.security.db_auth as db_auth

class ProductRepository:
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
    
    # 상품 조회
    def getProductData(self, storeName):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [storeName]
            cursor.execute("SELECT * FROM product WHERE s_id=(SELECT id FROM store WHERE store_name=%s)", arr)
            rows = cursor.fetchall()

            for i in rows:
                arr = i['id']
                cursor.execute("SELECT selling_option, price FROM product_selling_option WHERE p_id=%s", arr)
                rows2 = cursor.fetchall()
                if len(rows2) == 0:
                    i['selling_option'] = None
                else:
                    for j in rows2:
                        j['label'] = j['selling_option']
                        del j['selling_option']
                    i['selling_option'] = rows2
                    
                print(rows)
            
            if len(rows) == 0:
                return "DB Select Error"
            else:
                return rows
        except Exception as e:
            print(e)
            return "DB Select Error"
        finally:
            self.closeConnection()

    # 상품 등록
    def addProduct(self, productArr, sellingOptionArr, imgArr):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO product(s_id, product_name) VALUES(%s, %s)", productArr)
            self.connection.commit()
            
            cursor.execute("SELECT id FROM product WHERE s_id=%s AND product_name=%s", productArr)
            product_id = cursor.fetchall()
            
            # selling option 등록
            for i in sellingOptionArr:
                arr = [product_id[0]['id'], i['price'], i['label']]

                cursor.execute("INSERT INTO product_selling_option(p_id, price, selling_option) VALUES(%s, %s, %s)", arr)
                self.connection.commit()

            # 이미지 등록
            for i in imgArr:
                arr = [product_id[0]['id'], productArr[0], i] # p_id, s_id, i
                cursor.execute("INSERT INTO product_img(p_id, s_id, img_path) VALUES(%s, %s, %s)", arr)
                self.connection.commit()
                
            return "success"
        except Exception as e:
            print(e)
            return "DB Insert Error"
        finally:
            self.closeConnection()

    # 상품 이미지 조회
    def getStoreImage(self, storeId):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [storeId]
            cursor.execute("SELECT img_path FROM product_img WHERE s_id=%s", arr)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
            return "DB Select Error"
        finally:
            self.closeConnection()

    # 상품 수정
    def updateProduct(self, store_id, product_id, productArr, sellingOptionArr, imgArr):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE product SET product_name=%s WHERE id=%s", productArr)
            self.connection.commit()
            
            # selling option 등록
            for i in sellingOptionArr:
                arr = [i['price'], i['label'], product_id]
                cursor.execute("UPDATE product_selling_option SET price=%s, selling_option=%s WHERE p_id=%s", arr)
                self.connection.commit()

            # 이미지 등록
            for i in imgArr:
                arr = [i, product_id, store_id]
                cursor.execute("UPDATE product_img SET img_path=%s WHERE p_id=%s AND s_id=%s", arr)
                self.connection.commit()
                
            return "success"
        except Exception as e:
            print(e)
            return "DB Insert Error"
        finally:
            self.closeConnection()

    # 상품 수정 이미지 없는 것
    def updateProductNoImg(self, store_id, product_id, productArr, sellingOptionArr):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE product SET product_name=%s WHERE id=%s", productArr)
            self.connection.commit()
                        
            # selling option 등록
            for i in sellingOptionArr:
                arr = [i['price'], i['label'], product_id]
                cursor.execute("UPDATE product_selling_option SET price=%s, selling_option=%s WHERE p_id=%s", arr)
                self.connection.commit()
            return "success"
        except Exception as e:
            print(e)
            return "DB Insert Error"
        finally:
            self.closeConnection()

    # 상품 삭제
    def deleteProduct(self, productId, storeId):
        self.getConnection()
        try:
            cursor = self.connection.cursor()
            arr = [productId]
            cursor.execute("DELETE FROM product WHERE id=%s", arr)
            self.connection.commit()

            arr = [productId, storeId]
            cursor.execute("DELETE FROM product_img WHERE p_id=%s and s_id=%s", arr)
            self.connection.commit()
            return "success"
        except Exception as e:
            print(e)
            return "DB Delete Error"
        finally:
            self.closeConnection()
