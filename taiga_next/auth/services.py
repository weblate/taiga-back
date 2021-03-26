# -*- coding: utf-8 -*-
# Copyright (C) 2014-present Taiga Agile LLC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime, timedelta
from typing import Any, Optional, Union

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from taiga_next.conf import settings

from .models import User
from . import exceptions as exp
from . import repositories


# Auth

pwd_context = CryptContext(schemes=settings.CRYPT_SCHEMES, deprecated="auto")


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.JWT_TOKEN_EXPIRED_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

# User

def authenticate_user(username_or_email: str, password: str) -> Union[User, bool]:
    user = repositories.get_user_by_username_or_email(username_or_email, extra_filters={"is_active": True})
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user_by_token(token: str = Depends(oauth2_scheme)) -> Optional[User]:
    # Get payload
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
    except JWTError:
        raise exp.invalid_credentials

    # Get user
    username: str = payload.get("sub")
    if username is None:
        raise exp.invalid_credentials
    user = repositories.get_user_by_username_or_email(username)
    if user is None:
        raise exp.invalid_credentials

    return user


async def get_current_user(user: User = Depends(get_user_by_token)) -> Optional[User]:
    # Check if is active
    if not user.is_active:
        raise exp.inactive_user

    return user


is_auth_required = Depends(get_current_user)
