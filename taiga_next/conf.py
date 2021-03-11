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

from functools import lru_cache
from typing import Tuple, List

from pydantic import BaseSettings, EmailStr

class Settings(BaseSettings):
    SECRET_KEY: str = "app_secret"
    ADMINS: Tuple[Tuple[str, EmailStr], ...]
    CORS_ORIGINS: List[str] = ["*"]

    #class Config:
    #    env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    from django.conf import settings as django_settings

    return Settings(
        SECRET_KEY=django_settings.SECRET_KEY,
        ADMINS=django_settings.ADMINS,
    )


settings = get_settings()
