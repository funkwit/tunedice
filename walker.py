#!/usr/bin/python

import os, glob

class Walker(object):
  def missing(self, directory, user, metafile):
    for miss in self.check_directory(directory, user, metafile, missing=True):
      yield miss

  def wanted(self, directory, user, metafile):
    for hit in self.check_directory(directory, user, metafile, missing=False):
      yield hit

  def check_directory(self, path, user, metafile, missing):
    if not os.path.isdir(path):
      return
    meta = os.path.join(path, metafile)
    try:
      f = open(meta)
      for line in f.readlines():
        if line.strip() == ("!" + user):
          return
        if line.strip() == user:
          if missing:
            return
          else:
            yield path
    except IOError:
      pass

    if glob.glob(os.path.join(path, "*.mp3")):
      if missing:
        yield path
    else:
      for dirpath in sorted(os.listdir(path)):
        for miss in self.check_directory(os.path.join(path, dirpath), user,
                                         metafile, missing):
          yield miss
