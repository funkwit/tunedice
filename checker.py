#!/usr/bin/python

from optparse import OptionParser
import walker

import sys, os, fnmatch, re, glob

def docheck():
  parser = OptionParser()
  parser.add_option("-u", "--user", default=os.getenv("USER"),
                    help="User tag to look for (default to $USER)")
  parser.add_option("-m", "--meta-file", default=".dice",
                    help="Filename to check")
  (options, args) = parser.parse_args()
  if not args:
    raise SystemExit(parser.print_help() or 1)
  walk = walker.Walker()
  for miss in walk.missing(args[0], user=options.user,
                           metafile=options.meta_file):
    print "Missing: " + miss


if __name__ == "__main__":
  docheck()
