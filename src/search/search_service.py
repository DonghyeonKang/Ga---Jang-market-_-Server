import src.search.search_repository as search_repository

class SearchService:
    searchRepository = search_repository.SearchRepository()

    def __init__(self) -> None:
        pass
    
    # word 가 포함된 상품을 판매하는 가게의 id 리스트를 줌
    def getSearchData(self, word):
        result = self.searchRepository.getSearchData(word)
        return result