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
from .models import Task
from .schemas import TaskSchema


metadata = {
    "name": "tasks",
    "description": "Endpoint with actions over tasks.",
}

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get(
    "/",
    name="tasks.list",
    summary="List tasks",
    response_model=List[TaskSchema]
)
def list_tasks(
    offset: int = Query(0, description="number of tasks to skip"),
    limit: int = Query(100, description="number of tasks to show")
):
    """
    Get a paginated list of visible tasks.
    """
    return services.get_tasks(offset=offset, limit=limit)

@router.get(
    "/<task_id>",
    name="tasks.get",
    summary="Get some tasks details",
    response_model=TaskSchema,
)
def get_task(
    task_id: int = Query(None, description="the task id (integer)")
):
    """
    Get task detail by id.
    """
    task = services.get_task(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="API_NOT_FOUND")
    return task
