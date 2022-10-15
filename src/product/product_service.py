import src.product.product_repository as product_repository

class ProductService:
    productRepository = product_repository.ProductRepository()

    def __init__(self) -> None:
        pass
    
    def getProduct(self, storeName):
        result = self.productRepository.getProductData(storeName)
        return result