#!/usr/bin/python

from optparse import OptionParser
import os
import re
import walker


def docheck():
  parser = OptionParser()
  parser.add_option("-u", "--user", default=os.getenv("USER"),
                    help="User tag to look for (default to $USER)")
  parser.add_option("-m", "--meta-file", default=".dice",
                    help="Filename to check")
  parser.add_option("-H", "--hard-links", action="store_true",
                    default=False, help="Whether to use hardlinks (careful!)")
  (options, args) = parser.parse_args()
  if not args:
    raise SystemExit(parser.print_help() or 1)
  walk = walker.Walker()
  for target in walk.wanted(args[0], user=options.user,
                            metafile=options.meta_file):
    local = re.sub("^" + re.escape(args[0]) + "/?", "", target)
    print "User wants: %s %s to %s" % (target, "hardlinked" if
                                       options.hard_links else "symlinked", local) 

    (head, tail) = os.path.split(local)
    if options.hard_links:
      print "Can't do hard-links yet, sorry"
      return

    if head:
      print "Deep, deal with later"
    else:
      if os.path.lexists(local):
        if os.path.islink(local):
          if os.path.samefile(local, target):
            print "  OK: existing, nothing to do"
          else:
            print "  ERROR: already symlinked elsewhere!"
        else:
          print "  ERROR: desired link already exists as a file/directory"
      else:
        os.symlink(target, local)
        print "  OK: done!"


if __name__ == "__main__":
  docheck()
