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

    # 상시 매장 등록
    def addPermanentStore(self, data):
        result = self.storeRepository.addPermanentStore(data)
        return result

    # 상시 매장 수정
    def updatePermanentStore(self, data):
        result = self.storeRepository.updatePermanentStore(data)
        return result

    # 상시 매장 삭제
    def deletePermanentStore(self, storeID):
        result = self.storeRepository.deletePermanentStore(storeID)
        return result

    # 일일 매장 등록
    def addOneDayStore(self, data):
        result = self.storeRepository.addOneDayStore(data)
        return result

    # 상시 매장 수정
    def updateOneDayStore(self, data):
        result = self.storeRepository.updateOneDayStore(data)
        return result

    # 일일 매장 삭제
    def deleteOneDayStore(self, storeID):
        result = self.storeRepository.deleteOneDayStore(storeID)
        return result
