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
from typing import Iterable, List, Union

from fastapi import APIRouter, HTTPException

from . import services
from .models import Project
from .schemas import ProjectSchema


metadata = {
    "name": "projects",
    "description": "Endpoint with actions over projects.",
}

router = APIRouter()

@router.get(
    "/",
    name="projects.list",
    summary="List projects",
    response_model=List[ProjectSchema]
)
def list_projects(offset: int = 0, limit: int = 100) -> Iterable[Project]:
    return services.get_projects(offset=offset, limit=limit)

@router.get(
    "/<project_id>",
    name="projects.get",
    summary="Get some project datails",
    response_model=ProjectSchema,
)
def get_project(project_id: int) -> Union[Project, HTTPException]:
    project = services.get_project(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="API_NOT_FOUND")
    return project
