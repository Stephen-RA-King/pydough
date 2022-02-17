#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pathlib
import sys

BASE_DIR = pathlib.Path(__file__).resolve().parents[1]
SRC = BASE_DIR / "src"
sys.path.insert(0, str(SRC))
