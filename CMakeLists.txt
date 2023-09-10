project(pyleetcode)
cmake_minimum_required(VERSION 3.10)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/src/shared/)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/src/shared/)

enable_testing()

add_subdirectory(src/pyleetcode/n1_two_sum)
add_subdirectory(src/pyleetcode/n906_super_palindromes)