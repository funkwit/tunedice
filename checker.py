#!/usr/bin/python

from optparse import OptionParser

import sys, os, fnmatch, re, glob

class Checker(object):
  def missing(self, directory, user, metafile):
    for miss in self.check_directory(directory, user, metafile):
      yield miss

  def check_directory(self, path, user, metafile):
    if not os.path.isdir(path):
      return
    meta = os.path.join(path, metafile)
    try:
      with open(meta) as f:
        for line in f.readlines():
          if line.strip() == user or line.strip() == ("!" + user):
            return
    except IOError:
      pass

    if glob.glob(os.path.join(path, "*.mp3")):
      yield path
    else:
      for dirpath in sorted(os.listdir(path)):
        for miss in self.check_directory(os.path.join(path, dirpath), user,
                                         metafile):
          yield miss


def docheck():
  parser = OptionParser()
  parser.add_option("-u", "--user", default=os.getenv("USER"),
                    help="User tag to look for (default to $USER)")
  parser.add_option("-m", "--meta-file", default=".dice",
                    help="Filename to check")
  (options, args) = parser.parse_args()
  if not args:
    raise SystemExit(parser.print_help() or 1)
  checker = Checker()
  for miss in checker.missing(args[0], user=options.user,
                              metafile=options.meta_file):
    print "Missing: " + miss


if __name__ == "__main__":
  docheck()
