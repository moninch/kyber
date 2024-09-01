from fastapi import HTTPException, Response, status

UserAlreadyExistsException = HTTPException(
    status_code= status.HTTP_409_CONFLICT,
    detail= 'Пользователь уже зарегистрирован'
)

IncorrectloginOrPasswordException = HTTPException(
    status_code= status.HTTP_401_UNAUTHORIZED,
    detail="Неправильная логин или пароль"
                                                  )

TokenExpireException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Срок действия токена истек'
    )

TokenAbsentException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED
                                     ,detail='Токена истек')

UserIsNotPresentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    )

PostNotCreatedException = HTTPException(status_code=status.HTTP_404_NOT_FOUND
                                     ,detail='Пост не был создан')

