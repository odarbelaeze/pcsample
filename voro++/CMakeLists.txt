cmake_minimum_required(VERSION 2.8)
project(voro++)
subdirs(src)

configure_file(vorop.sh vorop.sh
  COPYONLY ESCAPE_QUOTES @ONLY)
