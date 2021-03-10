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

from fastapi import APIRouter

from . import views
#from .schemas import Project

metadata = {
    "name": "projects",
    "description": "Endpoint with actions over projects.",
}

router = APIRouter()

router.get(
    "/",
    name="projects.list",
    tags=["projects"],
    summary="List projects",
    #response_model=List[Project],
)(views.list_projects)

router.get(
    "/<project_id>",
    name="projects.get",
    tags=["projects"],
    summary="Get some project datails",
    #response_model=Project,
)(views.get_project)
