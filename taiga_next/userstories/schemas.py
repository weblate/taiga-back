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

from taiga_next.auth.schemas import UserBaseSchema
from taiga_next.projects.schemas import ProjectSchema


class UserStoryBaseSchema(BaseModel):
    id: int
    version: int
    created_date: datetime
    modified_date: datetime
    subject: str
    owner_id: int
    project_id: int

    class Config:
        orm_mode = True


class UserStorySchema(UserStoryBaseSchema):
    tags: List[str]
    is_blocked: bool
    blocked_note: str
    ref: int
    is_closed: bool
    backlog_order: str
    finish_date: Optional[datetime]
    description: str
    client_requirement: bool
    team_requirement: bool
    assigned_to_id: Optional[int]
    generated_from_issue_id: Optional[int]
    milestone_id: Optional[int]
    status_id: int
    sprint_order: int
    kanban_order: int
    external_reference: Optional[str]
    tribe_gig: Optional[str]
    due_date: Optional[str]
    due_date_reason: Optional[str]
    generated_from_task_id: Optional[int]
    from_task_ref: Optional[str]
    swimlane_id: Optional[int]
    """ epics: Optional[List[EpicBase]]
    tasks: Optional[List[TaskBase]] """

    class Config:
        orm_mode = True
