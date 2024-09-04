from fastapi import HTTPException, Response, status

class UserAlreadyExists(HTTPException):
    detail = "User already exists"
    status_code = status.HTTP_409_CONFLICT

class IncorrectLoginOrPassword(HTTPException):
    detail = "Incorrect login or password"
    status_code = status.HTTP_401_UNAUTHORIZED

class TokenExpired(HTTPException):
    detail = "Token expired"
    status_code = status.HTTP_401_UNAUTHORIZED

class TokenAbsent(HTTPException):
    detail = "User is not authorized"
    status_code = status.HTTP_401_UNAUTHORIZED

class UserNotFound(HTTPException):
    detail = "User not found"
    status_code = status.HTTP_404_NOT_FOUND

class PostNotCreated(HTTPException):
    detail = "Post not created"
    status_code = status.HTTP_404_NOT_FOUND

class PostNotFound(HTTPException):
    detail = "Post not found"
    status_code = status.HTTP_404_NOT_FOUND
