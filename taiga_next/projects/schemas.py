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

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class ProjectBaseSchema(BaseModel):
    name: str
    description: str
    tags: List[str]
    is_private: bool
    public_permissions: List[str]
    anon_permissions: List[str]
    is_epics_activated: bool
    is_backlog_activated: bool
    is_kanban_activated: bool
    is_issues_activated: bool
    is_wiki_activated: bool


class ProjectSchema(ProjectBaseSchema):
    id: int
    slug: str
    owner_id: int
    created_date: datetime
    modified_date: datetime

    class Config:
        orm_mode = True
