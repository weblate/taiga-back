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

from taiga_next.auth.services import is_auth_required

from taiga_next.auth import api as auth_api
from taiga_next.projects import api as projects_api
from taiga_next.userstories import api as userstories_api
from taiga_next.tasks import api as tasks_api
from taiga_next.epics import api as epics_api



router = APIRouter()
router.include_router(auth_api.router)
router.include_router(projects_api.router, dependencies=[is_auth_required])
router.include_router(userstories_api.router)
router.include_router(tasks_api.router)
router.include_router(epics_api.router)

tags_metadata = [
    auth_api.metadata,
    projects_api.metadata,
    userstories_api.metadata,
    tasks_api.metadata,
    epics_api.metadata,
]
