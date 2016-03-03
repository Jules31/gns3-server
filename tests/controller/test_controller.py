#!/usr/bin/env python
#
# Copyright (C) 2016 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pytest

from gns3server.controller import Controller
from gns3server.controller.server import Server
from gns3server.config import Config


def test_isEnabled(controller):
    Config.instance().set("Server", "controller", False)
    assert not controller.isEnabled()
    Config.instance().set("Server", "controller", True)
    assert controller.isEnabled()


def test_addServer(controller):
    server1 = Server("test1")

    controller.addServer(server1)
    assert len(controller.servers) == 1
    controller.addServer(Server("test1"))
    assert len(controller.servers) == 1
    controller.addServer(Server("test2"))
    assert len(controller.servers) == 2
