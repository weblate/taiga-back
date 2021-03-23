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
from .models import UserStory
from .schemas import UserStorySchema


metadata = {
    "name": "userstories",
    "description": "Endpoint with actions over userstories.",
}

router = APIRouter(prefix="/userstories", tags=["userstories"])

@router.get(
    "/",
    name="userstories.list",
    summary="List userstories",
    response_model=List[UserStorySchema]
)
def list_userstories(
    offset: int = Query(0, description="number of userstories to skip"),
    limit: int = Query(100, description="number of userstories to show")
):
    """
    Get a paginated list of visible userstories.
    """
    return services.get_userstories(offset=offset, limit=limit)

@router.get(
    "/<userstory_id>",
    name="userstories.get",
    summary="Get some userstorie details",
    response_model=UserStorySchema,
)
def get_userstory(
    userstory_id: int = Query(None, description="the userstory id (integer)")
):
    """
    Get userstory detail by id.
    """
    userstory = services.get_userstory(userstory_id)

    if userstory is None:
        raise HTTPException(status_code=404, detail="API_NOT_FOUND")
    return userstory
