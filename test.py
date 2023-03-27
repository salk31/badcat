#!/usr/local/bin/python3.9

import core
import pathlib

core = core.Core()

data_dir = pathlib.Path("test/data")

for path in data_dir.glob("*/*.jpg"):
  core.process(path)