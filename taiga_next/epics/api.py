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
from typing import Iterable, List

from fastapi import APIRouter, HTTPException, Query

from . import services
from .models import Epic
from .schemas import EpicSchema


metadata = {
    "name": "epics",
    "description": "Endpoint with actions over epics.",
}

router = APIRouter(prefix="/epics", tags=["epics"])

@router.get(
    "/",
    name="epics.list",
    summary="List epics",
    response_model=List[EpicSchema]
)
def list_epics(
    offset: int = Query(0, description="number of epics to skip"),
    limit: int = Query(100, description="number of epics to show")
):
    """
    Get a paginated list of visible epics.
    """
    return services.get_epics(offset=offset, limit=limit)

@router.get(
    "/<epic_id>",
    name="epics.get",
    summary="Get some epics details",
    response_model=EpicSchema,
)
def get_epic(
    epic_id: int = Query(None, description="the epic id (integer)")
):
    """
    Get epic detail by id.
    """
    epic = services.get_epic(epic_id)

    if epic is None:
        raise HTTPException(status_code=404, detail="API_NOT_FOUND")
    return epic
