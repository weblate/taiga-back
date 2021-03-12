#!/usr/bin/env python
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

import os

import typer

import uvicorn
from uvicorn.config import Config
from uvicorn.server import Server, ServerState  # noqa: F401  # Used to be defined here.
from uvicorn.supervisors import ChangeReload, Multiprocess

from taiga_next.wsgi import app as wsgi_app

wsgi_app_name = "taiga_next.wsgi:app"

cmd = typer.Typer()


@cmd.command()
def runserve(
    host: str = typer.Option("0.0.0.0", help="Host to serve the app."),
    port: int = typer.Option(8000, help="Port to serve the app."),
    reload: bool = typer.Option(True, help="Reload after some change in the source code happens."),
):
    if reload:
        app = wsgi_app_name
    else:
        app = wsgi_app
        app.debug = debug

    kwargs = {
        "host": host,
        "port": port,
        "reload": reload,
        "debug": True,
        "log_level": "debug",
    }

    config = Config(app, **kwargs)
    server = Server(config=config)


    typer.secho(f">> Running on {host}:{port}", bold=True)
    if config.should_reload:
        typer.secho(f">> Reload mode is ON", bold=True)
        sock = config.bind_socket()
        supervisor = ChangeReload(config, target=server.run, sockets=[sock])
        supervisor.run()
    else:
        server.run()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.common")

    cmd()
