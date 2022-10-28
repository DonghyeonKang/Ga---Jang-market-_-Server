import src.auth.auth_repository as auth_repository
# 앱 로그인
from flask import make_response
from flask_jwt_extended import *
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import decode_token
from flask_jwt_extended import JWTManager
from jwt import ExpiredSignatureError
import json
from datetime import datetime, timedelta # Time generator
from flask import jsonify # Return json form to client
import bcrypt
import base64
import hashlib
import hmac
import src.security.keys as keys
import time
import requests
import random

class AuthService:
    authRepository = auth_repository.AuthRepository()

    def __init__(self) -> None:
        pass

    #--------- /auth
    def createAccessToken(self, user_id): # 로그인 시 토큰 생성, access token 재생성. 
        token = create_access_token(identity = user_id, expires_delta = timedelta(minutes=1440))
        return token

    def createRefreshToken(self, user_id): # 로그인 시 토큰 생성
        authRepository = auth_repository.AuthRepository()
        
        token = create_refresh_token(identity = user_id, expires_delta = timedelta(minutes=1440))
        # TODO 아래 insert의 결과를 어떻게 처리해야할까, 이미 있는 refresh token 에 대해서는 어떻게 처리할까. 
        authRepository.insertRefreshToken(user_id, token)
        return token

    def renewToken(self, user_id, refreshToken):
        authRepository = auth_repository.AuthRepository()
        # DB 에 없는 refresh token 이면 False
        if authRepository.checkRefreshToken(refreshToken) == False:
            return {"message": "Unauthorized"}, 401

        result = self.verifyToken(refreshToken)
        if  result is not False:    # refresh 토큰이 만료되지 않았다면 access token 생성 후 리턴 
            resAccessToken = self.createAccessToken(user_id)
            resRefreshToken = self.createRefreshToken(user_id)
            return jsonify({"access_token" : resAccessToken, "refresh_token" : resRefreshToken}) # 재생성된 accessToken
        else:   # 리프레시 토큰도 만료되었을 때  {"message": "EXPIRED_TOKEN"}, 401 return -> 프론트에서 재로그인 처리
            return {"message": "EXPIRED_TOKEN"}, 401

    def verifyToken(self, token): # token 이 유효한 지 검증
        try:
            payload = decode_token(token)
            return payload
        except ExpiredSignatureError as e:
            print(e)
            return False

    def make_signature(self, string):
        secret_key = bytes(keys.secret_key, 'UTF-8')
        string = bytes(string, 'UTF-8')
        string_hmac = hmac.new(secret_key, string, digestmod=hashlib.sha256).digest()
        string_base64 = base64.b64encode(string_hmac).decode('UTF-8')
        return string_base64

    def send_massage(self, phoneNumber):
        url = "https://sens.apigw.ntruss.com"
        uri = "/sms/v2/services/" + keys.service_id + "/messages"
        api_url = url + uri
        timestamp = str(int(time.time() * 1000))
        access_key = keys.access_key
        string_to_sign = "POST " + uri + "\n" + timestamp + "\n" + access_key
        signature = self.make_signature(string_to_sign)

        headers = {
            'Content-Type': "application/json; charset=UTF-8",
            'x-ncp-apigw-timestamp': timestamp,
            'x-ncp-iam-access-key': access_key,
            'x-ncp-apigw-signature-v2': signature
        }

        verificationNum = random.randrange(100000,999999)
        message = "가는날이 장날이다 인증번호 [" + str(verificationNum) + "] 를 입력해주세요"

        body = {
            "type": "SMS",
            "contentType": "COMM",
            "from": "01041669516",
            "content": message,
            "messages": [{"to": phoneNumber}]
        }

        body = json.dumps(body)

        response = requests.post(api_url, headers=headers, data=body)
        response.raise_for_status()
        return {"result": str(verificationNum)}

    #--------- /auth/member/customer --------------------------------------
    def addCUser(self, user_id, user_pw): # 회원 가입
        authRepository = auth_repository.AuthRepository()
        if(authRepository.checkCUserId(user_id) == "Available"):
            pw = (bcrypt.hashpw(user_pw.encode('UTF-8'), bcrypt.gensalt())).decode('utf-8')  # 해싱 처리
            result = authRepository.insertCUser(user_id, pw)
            return jsonify({"result" : result})
        else:
            return jsonify({"result" : "Id is already exists"})

    def CLogin(self, user_id, user_pw): # 앱 로그인
        authRepository = auth_repository.AuthRepository()
        if(authRepository.checkCUserId(user_id) == "Already exists" and self.checkCUserPassword(user_id, user_pw)):
            return jsonify(result = "success",
                           access_token = self.createAccessToken(user_id),
                           refresh_token = self.createRefreshToken(user_id))
        else:
            return jsonify(result = "Invalid Params!")

    def CLogout(self, user_id):
        authRepository = auth_repository.AuthRepository()
        result = authRepository.deleteRefreshToken(user_id)
        return jsonify({"result" : result})

    # 아이디가 존재하는 지 체크함
    def checkCUserId(self, userid):
        authRepository = auth_repository.AuthRepository()
        result = authRepository.checkUserId(userid)
        return jsonify({"result": result})

    # 비밀 번호를 비교함
    def checkCUserPassword(self, input_username, input_password):
        authRepository = auth_repository.AuthRepository()
        result = authRepository.checkCUserPw(input_username)
        input_password = input_password.encode('utf-8') # bcrypt hash transfer

        if result == None: # DB에 계정 정보가 없으면 account == None
            return False
        else:
            check_password = bcrypt.checkpw(input_password, result['user_pw'].encode('utf-8')) # 해싱된 비밀번호 비교
            return check_password   # 일치하면 true, 틀리면 false
    
    #--------- /auth/member/merchant --------------------------------------
    def addMUser(self, user_id, user_pw): # 회원 가입
        authRepository = auth_repository.AuthRepository()
        if(authRepository.checkMUserId(user_id) == "Available"):
            pw = (bcrypt.hashpw(user_pw.encode('UTF-8'), bcrypt.gensalt())).decode('utf-8')  # 해싱 처리
            result = authRepository.insertMUser(user_id, pw)
            return jsonify({"result" : result})
        else:
            return jsonify({"result" : "Id is already exists"})

    def MLogin(self, user_id, user_pw): # 앱 로그인
        authRepository = auth_repository.AuthRepository()
        if(authRepository.checkMUserId(user_id) == "Already exists" and self.checkMUserPassword(user_id, user_pw)):
            return jsonify(result = "success",
                           access_token = self.createAccessToken(user_id),
                           refresh_token = self.createRefreshToken(user_id))
        else:
            return jsonify(result = "Invalid Params!")

    def MLogout(self, user_id):
        authRepository = auth_repository.AuthRepository()
        result = authRepository.deleteRefreshToken(user_id)
        return jsonify({"result" : result})

    # 아이디가 존재하는 지 체크함
    def checkMUserId(self, userid):
        authRepository = auth_repository.AuthRepository()
        result = authRepository.checkMUserId(userid)
        return jsonify({"result": result})

    # 비밀 번호를 비교함
    def checkMUserPassword(self, input_username, input_password):
        authRepository = auth_repository.AuthRepository()
        result = authRepository.checkMUserPw(input_username)
        input_password = input_password.encode('utf-8') # bcrypt hash transfer

        if result == None: # DB에 계정 정보가 없으면 account == None
            return False
        else:
            check_password = bcrypt.checkpw(input_password, result['user_pw'].encode('utf-8')) # 해싱된 비밀번호 비교
            return check_password   # 일치하면 true, 틀리면 false