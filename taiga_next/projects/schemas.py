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
    id: int
    name: str
    slug: str

    class Config:
        orm_mode = True


class ProjectSchema(ProjectBaseSchema):
    tags: List[str]
    description: str
    created_date: datetime
    modified_date: datetime
    total_milestones: Optional[int]
    total_story_points: Optional[float]
    is_backlog_activated: bool
    is_kanban_activated: bool
    is_wiki_activated: bool
    is_issues_activated: bool
    videoconferences: Optional[str]
    videoconferences_extra_data: Optional[str]
    anon_permissions: List[str]
    public_permissions: List[str]
    is_private: bool
    owner_id: int
    creation_template_id: Optional[int]
    default_issue_status_id: Optional[int]
    default_issue_type_id: Optional[int]
    default_points_id: Optional[int]
    default_priority_id: Optional[int]
    default_severity_id: Optional[int]
    default_task_status_id: Optional[int]
    default_us_status_id: Optional[int]
    issues_csv_uuid: Optional[str]
    tasks_csv_uuid: Optional[str]
    userstories_csv_uuid: Optional[str]
    is_featured: bool
    is_looking_for_people: bool
    total_activity: int
    total_activity_last_month: int
    total_activity_last_week: int
    total_activity_last_year: int
    total_fans: int
    total_fans_last_month: int
    total_fans_last_week: int
    total_fans_last_year: int
    totals_updated_datetime: datetime
    logo: Optional[str]
    looking_for_people_note: str
    blocked_code: Optional[str]
    transfer_token: Optional[str]
    is_epics_activated: bool
    default_epic_status_id: Optional[int]
    epics_csv_uuid: Optional[str]
    is_contact_activated: bool
    default_swimlane_id: Optional[int]

    class Config:
        orm_mode = True