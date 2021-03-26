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
from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from taiga_next.auth.schemas import UserBaseSchema
from taiga_next.projects.schemas import ProjectBaseSchema
from taiga_next.tasks.schemas import TaskBaseSchema
from taiga_next.epics.schemas import EpicSchema


class UserStoryBaseSchema(BaseModel):
    id: int
    version: int
    created_date: datetime
    modified_date: datetime
    subject: str
    owner: UserBaseSchema
    project: ProjectBaseSchema

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
    assigned_to: Optional[UserBaseSchema]
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
    epics_attr: Optional[List[EpicSchema]]
    tasks_attr: Optional[List[TaskBaseSchema]]
    total_points_attr: Optional[int]
    role_points_attr: Optional[Any]
    assigned_users_attr: Optional[List[int]]
    watchers: Optional[Any]
    total_voters: Optional[int]
    total_watchers: Optional[int]
    is_voter: bool
    is_watcher: bool
    comment: Optional[str]
    total_comments: Optional[int]

    class Config:
        orm_mode = True

