import src.store.store_repository as store_repository

class StoreService:
    storeRepository = store_repository.StoreRepository()

    def __init__(self) -> None:
        pass
    
    def getStore(self, marketName):
        result = self.storeRepository.getStoreData(marketName)
        return result