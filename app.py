from flask import Flask # Flask start 
import src.auth.auth_service as auth_service
from functools import wraps
from flask import request
from flask import jsonify
import datetime, json

app = Flask(__name__)

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
# 앱 회원가입
@app.route('/member/customer', methods=['POST'])
def registerCustomer():
    authService = auth_service.AuthService()
    # 클라이언트로부터 요청된 값
    inputData = request.get_json()
    user_id = inputData['user_id']
    user_pw = inputData['user_pw']
    nickname = inputData['nickname']
    result = authService.addUser(user_id, user_pw, nickname)
    return result

# 앱 비밀번호 변경
@app.route('/member/customer/password', methods=['POST'])
@token_required
def changePasswordCustomer():
    authService = auth_service.AuthService()
    # 클라이언트로부터 요청된 값
    inputData = request.get_json()
    user_id = inputData['user_id']
    user_pw = inputData['user_pw']
    result = authService.changePassword(user_id, user_pw)
    return result

# 앱 로그인
@app.route('/login/customer', methods=['POST'])
def loginCustomer():
    authService = auth_service.AuthService()
    # 클라이언트로부터 요청된 값
    inputData = request.get_json()
    user_id = inputData['user_id']
    user_pw = inputData['user_pw']

    resData = authService.appLogin(user_id, user_pw)
    return resData

# 앱 로그아웃
@app.route('/logout/customer', methods=['POST'])
@token_required
def logoutCustomer():
    authService = auth_service.AuthService()
    # 클라이언트로부터 요청된 값
    inputData = request.get_json()
    user_id = inputData['user_id']

    result = authService.appLogout(user_id)
    return result

# 상품 좋아요 리스트
@app.route('/Favorites', methods=['GET'])
@token_required
def getFavorites():
    return "1"

# 상품 좋아요
@app.route('/Favorites', methods=['POST'])
@token_required
def addFavorites():
    return "1"

# 상품 좋아요 취소
@app.route('/Favorites', methods=['DELETE'])
@token_required
def deleteFavorites():
    return "1"
#---------------- merchant -----------------------
# 앱 회원가입
@app.route('/member/merchant', methods=['POST'])
def registerMerchant():
    authService = auth_service.AuthService()
    # 클라이언트로부터 요청된 값
    inputData = request.get_json()
    user_id = inputData['user_id']
    user_pw = inputData['user_pw']
    nickname = inputData['nickname']
    result = authService.addUser(user_id, user_pw, nickname)
    return result

# 앱 비밀번호 변경
@app.route('/member/merchant/password', methods=['POST'])
@token_required
def changePasswordMerchant():
    authService = auth_service.AuthService()
    # 클라이언트로부터 요청된 값
    inputData = request.get_json()
    user_id = inputData['user_id']
    user_pw = inputData['user_pw']
    result = authService.changePassword(user_id, user_pw)
    return result

# 앱 로그인
@app.route('/login/merchant', methods=['POST'])
def loginMerchant():
    authService = auth_service.AuthService()
    # 클라이언트로부터 요청된 값
    inputData = request.get_json()
    user_id = inputData['user_id']
    user_pw = inputData['user_pw']

    resData = authService.appLogin(user_id, user_pw)
    return resData

# 앱 로그아웃
@app.route('/logout/merchant', methods=['POST'])
@token_required
def logoutMerchant():
    authService = auth_service.AuthService()
    # 클라이언트로부터 요청된 값
    inputData = request.get_json()
    user_id = inputData['user_id']

    result = authService.appLogout(user_id)
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
# 매장 리스트
@app.route('/store', methods=['GET'])
def getStore():
    storeService = store_service.StoreService()
    marketName = request.args.get('market_name')
    result = storeService.getStore(marketName)
    json_string = json.dumps(result, default=str, ensure_ascii=False)
    return json.loads(json_string)

# 상시 매장 등록
@app.route('/store/permanent', methods=['POST'])
@token_required
def addPermanentStore():
    return "1"

# 상시 매장 수정
@app.route('/store/permanent', methods=['PUT'])
@token_required
def updatePermanentStore():
    return "1"

# 상시 매장 삭제
@app.route('/store/permanent', methods=['DELETE'])
@token_required
def deletePermanentStore():
    return "1"

# 일일 매장 등록
@app.route('/store/oneDay', methods=['POST'])
@token_required
def addOneDayStore():
    return "1"

# 상시 매장 수정
@app.route('/store/oneDay', methods=['PUT'])
@token_required
def updateOneDayStore():
    return "1"

# 일일 매장 삭제
@app.route('/store/oneDay', methods=['DELETE'])
@token_required
def deleteOneDayStore():
    return "1"

########################## product #################################################
import src.product.product_service as product_service
# 상품 리스트
@app.route('/product', methods=['GET'])
def getProduct():
    productService = product_service.ProductService()
    storeName = request.args.get('store_name')
    result = productService.getProduct(storeName)
    return {"result" : result}

# 상품 등록
@app.route('/product', methods=['POST'])
def addProduct():
    return "1"

# 상품 수정
@app.route('/product', methods=['PUT'])
def updateProduct():
    return "1"

# 상품 삭제
@app.route('/product', methods=['DELETE'])
def deleteProduct():
    return "1"

########################## notification #################################################
# 매장 알림 목록
@app.route('/product', methods=['GET'])
@token_required
def getNotification():
    return "1"

# 매장 알림 등록
@app.route('/product', methods=['POST'])
@token_required
def addNotification():
    return "1"

# 매장 알림 취소
@app.route('/product', methods=['DELETE'])
@token_required
def deleteNotification():
    return "1"

########################## reservation #################################################
# 예약 리스트
@app.route('/reservation', methods=['GET'])
@token_required
def getReservation():
    return "1"

# 예약하기
@app.route('/reservation', methods=['POST'])
@token_required
def addReservation():
    return "1"

# 취소하기
@app.route('/reservation', methods=['DELETE'])
@token_required
def deleteReservation():
    return "1"

# 수락하기
@app.route('/reservation/accept', methods=['POST'])
@token_required
def acceptReservation():
    return "1"

# 거절하기
@app.route('/reservation/reject', methods=['POST'])
@token_required
def rejectReservation():
    return "1"

########################## search #################################################
# 검색하기
@app.route('/search', methods=['GET'])
def search():
    return "1"


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True, threaded=True)