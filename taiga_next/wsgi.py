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

"""
WSGI config for taiga project.

You can run this with uvicorn or gunicorn:

    # with gunicorn
    DJANGO_SETTINGS_MODULE=settings.config gunicorn wsgi:app -w 4 -k uvicorn.workers.UvicornWorker

    # with uvicorn
    DJANGO_SETTINGS_MODULE=settings.config uvicorn wsgi:app --reload

"""
import os, sys, inspect

from starlette.applications import Starlette
from starlette.middleware.wsgi import WSGIMiddleware
from starlette.staticfiles import StaticFiles


current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from taiga.wsgi import application as django_api
from taiga_next.main import app as api


app = Starlette()

# Mount the new api
app.mount("/api/v2/", app=api)

# Serve old api, admin, static and media files urls
app.mount("/", WSGIMiddleware(django_api))
