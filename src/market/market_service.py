import src.market.market_repository as market_repository

class MarketService:
    marketRepository = market_repository.MarketRepository()

    def __init__(self) -> None:
        pass
    
    def getMarket(self, marketName):
        result = self.marketRepository.getMarketData(marketName)
        return result