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

from typing import Iterable, List, Union

from fastapi import APIRouter, Depends

from . import exceptions as exp
from .schemas import OAuth2PasswordRequestForm, LoginSchema
from .services import authenticate_user, create_access_token

metadata = {
    "name": "auth",
    "description": "Endpoint with actions related to authentication process.",
}

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post(
    "/login",
    name="auth.login",
    summary="User sign in",
    response_model=LoginSchema
)
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form.username, form.password)
    if not user:
        raise exp.invalid_credentials

    user.token_type = "bearer"
    user.access_token = create_access_token(data={"sub": user.username})
    return user
