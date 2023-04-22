#!/usr/local/bin/python3.9

import core
import pathlib

core = core.Core()

data_dir = pathlib.Path("test/data")

for path in data_dir.glob("*/*.jpg"):
  print(path)
  res = core.process(path)
  print(f'{path} -> {res.detections(0.8)}')