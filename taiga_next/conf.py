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
from typing import Tuple

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_secret: str = "app_secret"
    admins: Tuple[Tuple[str, str], ...]

    #class Config:
    #    env_file = ".env"


@property
@lru_cache()
def settings():
    from django.conf import settings as django_settings

    return Settings(
        app_secret=django_settings.SECRET_KEY,
        admins=django_settings.ADMINS,
    )
