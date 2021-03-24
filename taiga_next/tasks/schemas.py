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

class TaskBaseSchema(BaseModel):
    id: int
    is_blocked: bool
    is_closed: bool
    is_iocaine: bool
    ref: Optional[int]
    status_id: Optional[int]
    subject: str

    class Config:
        orm_mode = True


class TaskSchema(TaskBaseSchema):
    tags: Optional[List[str]]
    version: int
    blocked_note: str
    created_date: datetime
    modified_date: datetime
    finished_date: Optional[datetime]
    description: str
    assigned_to_id: Optional[int]
    milestone_id: Optional[int]
    owner_id: int
    project_id: int
    status_id: int
    user_story_id: int
    taskboard_order: int
    us_order: int
    external_reference: Optional[List[str]]
    due_date: Optional[datetime]
    due_date_reason: str

    class Config:
        orm_mode = True
