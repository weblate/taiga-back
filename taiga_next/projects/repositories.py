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

from typing import Iterable, Union

from .models import Project


def get_project(id: int) -> Union[Project, None]:
    try:
        return Project.objects.get(id=id)
    except Project.DoesNotExist:
        return None


def get_project_by_slug(slug: str) -> Project:
    try:
        return Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        return None


def get_projects(offset: int, limit: int) -> Iterable[Project]:
    return Project.objects.all()[offset:offset+limit]
