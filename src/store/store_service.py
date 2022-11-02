import src.store.store_repository as store_repository

class StoreService:
    storeRepository = store_repository.StoreRepository()

    def __init__(self) -> None:
        pass

    # 시장의 모든 매장 조회
    def getStore(self, marketName):
        result = self.storeRepository.getStoreData(marketName)

        for i in result:
            storeImg = self.storeRepository.getStoreImage(i['id'])

            # result 에 'img_paths' 추가
            i['img_paths'] = []
            if len(storeImg) > 0:
                for j in storeImg:
                    i['img_paths'].append(j['img_path'])
            else:
                i['img_paths'] = None
        return result

    # 내 매장 조회
    def getMyStore(self, merchantId):
        result = self.storeRepository.getMyStoreData(merchantId)

        for i in result:
            storeImg = self.storeRepository.getStoreImage(i['id'])

            # result 에 'img_paths' 추가
            i['img_paths'] = []
            if len(storeImg) > 0:
                for j in storeImg:
                    i['img_paths'].append(j['img_path'])
            else:
                i['img_paths'] = None
        return result

    # 매장 이미지 조회
    def getStoreImg(self, storeId):
        result = self.storeRepository.getStoreImage(storeId)
        return result

    # 매장 등록
    def addStore(self, data):
        imgArr = data['images']
        result = self.storeRepository.addStore(data, imgArr)
        return result

    # 매장 수정
    def updateStore(self, data):
        imgArr = data['images']
        result = self.storeRepository.updateStore(data, imgArr)
        return result

    # 매장 삭제
    def deleteStore(self, storeId):
        result = self.storeRepository.deleteStore(storeId)
        return result
