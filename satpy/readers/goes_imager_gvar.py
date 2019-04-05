#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2018 PyTroll developers
#
# Author(s):
#
#   Ioan.Ferencik <ioan.ferencik@solargis.com>

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
"""
A python GOES GVAR reader


"""

import logging
from datetime import datetime, timedelta

import numpy as np
import dask.array as da
import xarray as xr

from pyresample import geometry

from satpy.readers.file_handlers import BaseFileHandler
#from satpy.readers.utils import


logger = logging.getLogger('goes_imager_gvar')