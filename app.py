from flask import Flask # Flask start 
import src.auth.auth_service as auth_service
from functools import wraps
from flask import request
from flask import jsonify
import datetime, json
import jwt
from jwt import ExpiredSignatureError
from flask_jwt_extended import *
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import decode_token
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.secret_key = 'asd1inldap123jwaw'        # 세션을 암호화하기 위해 비밀키가 서명된 쿠키 사용
app.config.update(
			DEBUG = True,
			JWT_SECRET_KEY = "adswoern!@#rwlenf@#$13rweT#^DSfsrtwer"
		)
jwt = JWTManager(app)

if not app.debug: # 디버그 모드가 아니면
    import logging  # 로깅을 하기위한 모듈
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler( # 2000바이트가 넘어가면 로테이팅 백업 진행. 최대 파일 10개
        '../log/arambyeol_error.log', maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.WARNING) # WARNING 수준의 레벨들을 로깅
    app.logger.addHandler(file_handler)
########################## member #################################################
# 토큰 유효성 검사
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs): # *args, **kwargs 정해지지 않은 인자
        token = None
        inputData = request.get_json(silent=True)

        if inputData == None: # json 데이터가 없다면
            if 'access_token' in request.form:
                token = request.form['access_token']
                authService = auth_service.AuthService()
                if authService.verifyToken(token) == False:
                    return jsonify({'result' : 'EXPIRED_TOKEN'}), 401
            else:
                return jsonify({'result' : 'Token is missing!'}), 401
        else:
            if 'access_token' in inputData: # 토큰이 존재하면,
                token = inputData['access_token']
                authService = auth_service.AuthService()
                if authService.verifyToken(token) == False:
                    return jsonify({'result' : 'EXPIRED_TOKEN'}), 401
            else:
                return jsonify({'result' : 'Token is missing!'}), 401
        return f(*args, **kwargs)
    return decorated

# 토큰 갱신
@app.route('/member/auth', methods=['PUT'])
def renewToken():
    authService = auth_service.AuthService()
    # 클라이언트로부터 요청된 값
    inputData = request.get_json()
    user_id = inputData['user_id']
    reqRefreshToken = inputData['refresh_token']

    result = authService.renewToken(user_id, reqRefreshToken)
    return result

#---------------- customer -----------------------
# 회원가입
@app.route('/member/customer', methods=['POST'])
def registerCustomer():
    authService = auth_service.AuthService()
    # 클라이언트로부터 요청된 값
    inputData = request.get_json()
    user_id = inputData['user_id']
    user_pw = inputData['user_pw']
    result = authService.addCUser(user_id, user_pw)
    return result

# 로그인
@app.route('/login/customer', methods=['POST'])
def loginCustomer():
    authService = auth_service.AuthService()
    # 클라이언트로부터 요청된 값
    inputData = request.get_json()
    user_id = inputData['user_id']
    user_pw = inputData['user_pw']

    resData = authService.CLogin(user_id, user_pw)
    return resData

# 로그아웃
@app.route('/logout/customer', methods=['POST'])
@token_required
def logoutCustomer():
    authService = auth_service.AuthService()
    # 클라이언트로부터 요청된 값
    inputData = request.get_json()
    user_id = inputData['user_id']
    result = authService.CLogout(user_id)
    return result

# 상품 좋아요 리스트
@app.route('/favorites', methods=['GET'])
@token_required
def getFavorites():
    return "1"

# 상품 좋아요
@app.route('/favorites', methods=['POST'])
@token_required
def addFavorites():
    return "1"

# 상품 좋아요 취소
@app.route('/favorites', methods=['DELETE'])
@token_required
def deleteFavorites():
    return "1"
#---------------- merchant -----------------------
# 회원가입
@app.route('/member/merchant', methods=['POST'])
def registerMerchant():
    authService = auth_service.AuthService()
    # 클라이언트로부터 요청된 값
    inputData = request.get_json()
    user_id = inputData['user_id']
    user_pw = inputData['user_pw']
    result = authService.addMUser(user_id, user_pw)
    return result

# 로그인
@app.route('/login/merchant', methods=['POST'])
def loginMerchant():
    authService = auth_service.AuthService()
    # 클라이언트로부터 요청된 값
    inputData = request.get_json()
    user_id = inputData['user_id']
    user_pw = inputData['user_pw']

    resData = authService.MLogin(user_id, user_pw)
    return resData

# 로그아웃
@app.route('/logout/merchant', methods=['POST'])
@token_required
def logoutMerchant():
    authService = auth_service.AuthService()
    # 클라이언트로부터 요청된 값
    inputData = request.get_json()
    user_id = inputData['user_id']

    result = authService.MLogout(user_id)
    return result

########################## market #################################################
import src.market.market_service as market_service
# market
@app.route('/market', methods=['GET'])
def getMarket():
    marketService = market_service.MarketService()
    marketName = request.args.get('market_name')
    result = marketService.getMarket(marketName)
    return {"result" : result}

########################## store #################################################
import src.store.store_service as store_service
storeService = store_service.StoreService()
# 매장 리스트
@app.route('/store', methods=['GET'])
def getStore():
    marketName = request.args.get('market_name')
    result = storeService.getStore(marketName)
    json_string = json.dumps(result, default=str, ensure_ascii=False)
    return json.loads(json_string)

# 상시 매장 등록
@app.route('/store/permanent', methods=['POST'])
def addPermanentStore():
    marketName = request.args.get('market_name')
    result = storeService.getStore(marketName)
    return {"result" : result}

# 상시 매장 수정
@app.route('/store/permanent', methods=['PUT'])
def updatePermanentStore():
    marketName = request.args.get('market_name')
    result = storeService.updatePermanentStore(marketName)
    return {"result" : result}

# 상시 매장 삭제
@app.route('/store/permanent', methods=['DELETE'])
def deletePermanentStore():
    marketName = request.args.get('market_name')
    result = storeService.deletePermanentStore(marketName)
    return {"result" : result}

# 일일 매장 등록
@app.route('/store/oneday', methods=['POST'])
def addOneDayStore():
    marketName = request.args.get('market_name')
    result = storeService.addOneDayStore(marketName)
    return {"result" : result}

# 상시 매장 수정
@app.route('/store/oneday', methods=['PUT'])
def updateOneDayStore():
    marketName = request.args.get('market_name')
    result = storeService.updateOneDayStore(marketName)
    return {"result" : result}

# 일일 매장 삭제
@app.route('/store/oneday', methods=['DELETE'])
def deleteOneDayStore():
    marketName = request.args.get('market_name')
    result = storeService.deleteOneDayStore(marketName)
    return {"result" : result}

########################## product #################################################
import src.product.product_service as product_service
productService = product_service.ProductService()
# 상품 리스트
@app.route('/product', methods=['GET'])
def getProduct():
    storeName = request.args.get('store_name')
    result = productService.getProduct(storeName)
    return {"result" : result}

# 상품 등록
@app.route('/product', methods=['POST'])
def addProduct():
    inputData = request.get_json()
    result = productService.addProduct(inputData)
    return {"result" : result}

# 상품 수정
@app.route('/product', methods=['PUT'])
def updateProduct():
    inputData = request.get_json()
    result = productService.updateProduct(inputData)
    return {"result" : result}

# 상품 삭제
@app.route('/product', methods=['DELETE'])
def deleteProduct():
    productId = request.args.get('product_id')
    storeId = request.args.get('store_id')
    result = productService.deleteProduct(productId, storeId)
    return {"result" : result}

########################## reservation #################################################
import src.reservation.reservation_service as reservation_service
reservationService = reservation_service.ReservationService()
# 예약 리스트
@app.route('/reservation', methods=['GET'])
def getReservation():
    user_id = request.args.get('user_id')
    result = reservationService.getReservation(user_id)
    return {"result" : result}

# 예약하기
@app.route('/reservation', methods=['POST'])
def addReservation():
    # notification 으로 상인에게 알림을 넘겨줘야함
    inputData = request.get_json()
    result = reservationService.addReservation(inputData)
    return {"reservation_id" : result}

# 취소하기
@app.route('/reservation', methods=['DELETE'])
def deleteReservation():
    reservation_id = request.args.get('reservation_id')
    result = reservationService.deleteReservation(reservation_id)
    return {"result" : result}

# 수락하기
@app.route('/reservation/accept', methods=['POST'])
def acceptReservation():
    inputData = request.get_json()
    result = reservationService.acceptReservation(inputData['reservation_id'])
    return {"result" : result}

# 거절하기
@app.route('/reservation/reject', methods=['POST'])
def rejectReservation():
    inputData = request.get_json()
    result = reservationService.rejectReservation(inputData['reservation_id'])
    return {"result" : result}

########################## search #################################################
import src.search.search_service as search_service
searchService = search_service.SearchService()

# 검색하기
@app.route('/search', methods=['GET'])
def search():
    word = request.args.get('word')
    result = searchService.getSearchData(word)
    return {"result" : result}


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True, threaded=True)