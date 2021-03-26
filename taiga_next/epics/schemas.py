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
from taiga_next.projects.schemas import ProjectBaseSchema


class EpicSchema(BaseModel):
    id: int
    color: str
    project: ProjectBaseSchema
    ref: Optional[int]
    subject: str

    class Config:
        orm_mode = True


class EpicsRelateduserstorySchema(BaseModel):
    id: int
    order: int
    epic_id: int
    user_story_id: int

    class Config:
        orm_mode = True
