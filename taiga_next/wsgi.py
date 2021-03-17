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
New WSGI config for taiga project.

You can run this with uvicorn or gunicorn:

    # with gunicorn
    DJANGO_SETTINGS_MODULE=settings.config gunicorn taiga_next.wsgi:app -w 4 -k uvicorn.workers.UvicornWorker

    # with uvicorn
    DJANGO_SETTINGS_MODULE=settings.config uvicorn taiga_next.wsgi:app --reload

"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from starlette.applications import Starlette
from starlette.middleware.wsgi import WSGIMiddleware
from starlette.staticfiles import StaticFiles

from taiga.wsgi import application as django_app
from taiga_next.main import api


app = Starlette(debug=True)

# Mount the new api
app.mount("/api/v2/", app=api)

# Serve old api, sitemaps, admin, static and media files urls
app.mount("/", WSGIMiddleware(django_app))
