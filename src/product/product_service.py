import src.product.product_repository as product_repository

class ProductService:
    productRepository = product_repository.ProductRepository()

    def __init__(self) -> None:
        pass
    
    def getProduct(self, storeName):
        result = self.productRepository.getProductData(storeName)
        for i in result:
            productImg = self.productRepository.getProductImage(i['id'])
            i['img_path'] = productImg
        return result

    # 상품 등록
    def addProduct(self, inputData):
        # 상품 등록
        productArr = [inputData['store_id'], inputData['product_name'], inputData['content'], inputData['origin']] # s_id, product_name, img_path
        sellingOptionArr = inputData['selling_option']
        imgArr = [inputData['images']]
        result = self.productRepository.addProduct(productArr, sellingOptionArr, imgArr)
        return result

    # 상품 이미지 
    def getProductImg(self, productId):
        result = self.productRepository.getProductImage(productId)
        return result

    # 상품 수정
    def updateProduct(self, inputData):
        try:
            product_id = inputData['product_id']
            store_id = inputData['store_id']
            imgArr = [inputData['images']]
            # 상품 수정
            productArr = [inputData['product_name'], inputData['content'], inputData['origin'], product_id] # product_name, s_id
            sellingOptionArr = inputData['selling_option']
            result = self.productRepository.updateProduct(store_id, product_id, productArr, sellingOptionArr, imgArr)
        except KeyError:
            product_id = inputData['product_id']
            store_id = inputData['store_id']
            # 이미지가 없는 상품 수정
            productArr = [inputData['product_name'], product_id] # product_name, s_id
            sellingOptionArr = inputData['selling_option']
            result = self.productRepository.updateProductNoImg(store_id, product_id, productArr, sellingOptionArr)
        return result

    # 상품 삭제
    def deleteProduct(self, productId, storeId):
        result = self.productRepository.deleteProduct(str(productId), str(storeId))
        return result
