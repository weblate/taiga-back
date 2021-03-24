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

from typing import Optional, Union

from . import repositories
from .models import Project


def get_project(identifier: Union[int, str]) -> Optional[Project]:
    if isinstance(identifier, int):
        return repositories.get_project(identifier)
    return repositories.get_project_by_slug(identifier)


def get_projects(offset: int = 0, limit: int = 100) -> list[Project]:
    return list(repositories.get_projects(offset, limit))
