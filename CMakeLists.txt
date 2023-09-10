project(pyleetcode)
cmake_minimum_required(VERSION 3.10)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ../src/shared)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ../src/shared)

add_library(n1 SHARED src/pyleetcode/n1_two_sum/n1_two_sum.c)

add_library(n906 SHARED src/pyleetcode/n906_super_palindromes/n906_super_palindromes.c)
add_executable(n906_test src/pyleetcode/n906_super_palindromes/n906_super_palindromes_test.c)
target_link_libraries(n906_test n906)

enable_testing()
add_test(NAME n906_test COMMAND n906_test)