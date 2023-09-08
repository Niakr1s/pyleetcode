project(pyleetcode)
cmake_minimum_required(VERSION 3.10)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ../src/shared)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ../src/shared)

add_library(n1 SHARED src/pyleetcode/n1_two_sum/n1_two_sum.c)