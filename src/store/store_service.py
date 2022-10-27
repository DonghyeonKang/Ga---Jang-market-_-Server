import src.store.store_repository as store_repository

class StoreService:
    storeRepository = store_repository.StoreRepository()

    def __init__(self) -> None:
        pass

    # 매장 조회
    def getStore(self, marketName):
        result = self.storeRepository.getStoreData(marketName)
        return result

    # 매장 이미지 조회
    def getStoreImg(self, marketID):
        result = self.storeRepository.getStoreImage(marketID)
        return result

    # 매장 등록
    def addStore(self, data):
        imgArr = [data['image']]
        print(imgArr)
        result = self.storeRepository.addStore(data, imgArr)
        return result

    # 매장 수정
    def updateStore(self, data):
        imgArr = [data['image']]
        result = self.storeRepository.updateStore(data, imgArr)
        return result

    # 매장 삭제
    def deleteStore(self, storeId):
        result = self.storeRepository.deleteStore(storeId)
        return result
