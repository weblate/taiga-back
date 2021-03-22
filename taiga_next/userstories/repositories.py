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

from .models import UserStory

from taiga.projects.userstories.utils import attach_extra_info


def get_userstory(id: int) -> Union[UserStory, None]:
    try:
        return UserStory.objects.get(id=id)
    except UserStory.DoesNotExist:
        return None


def get_userstories(offset: int, limit: int) -> Iterable[UserStory]:
        qs = UserStory.objects.all()[offset:offset+limit]
        qs = qs.select_related("project",
                               "status",
                               "assigned_to",
                               "owner")

        qs = attach_extra_info(qs, include_tasks=True)

        return qs