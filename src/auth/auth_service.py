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

    #--------- /auth/member/customer --------------------------------------
    def addCUser(self, user_id, user_pw): # 회원 가입
        authRepository = auth_repository.AuthRepository()
        # 학교 메일 검증
        id = user_id.split("@")
        if len(id) < 2 or id[len(id) - 1] != 'gnu.ac.kr': # split 이 되지 않으면
                return jsonify({"result":"Id is not gnuEmail"})
        else:
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
        # 학교 메일 검증
        id = user_id.split("@")
        if len(id) < 2 or id[len(id) - 1] != 'gnu.ac.kr': # split 이 되지 않으면
                return jsonify({"result":"Id is not gnuEmail"})
        else:
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