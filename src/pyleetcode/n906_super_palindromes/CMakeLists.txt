add_library(n906 SHARED n906_super_palindromes.c)

enable_testing()

add_executable(n906_test n906_super_palindromes_test.c)
target_link_libraries(n906_test n906)
add_test(NAME n906_test COMMAND n906_test)