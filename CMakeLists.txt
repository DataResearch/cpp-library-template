cmake_minimum_required(VERSION 3.16)

set(PROJECT_NAME cpp_library_template)
set(CMAKE_CXX_STANDARD 17)

project(${PROJECT_NAME})
add_library(${PROJECT_NAME} SHARED)

target_compile_definitions(${PROJECT_NAME} PRIVATE _USE_MATH_DEFINES=1)

target_sources(${PROJECT_NAME} PRIVATE src/library.cpp)
target_sources(${PROJECT_NAME} PUBLIC src/include/library.h)

set_target_properties(${PROJECT_NAME} PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build/lib"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build/lib"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build/bin"
)

find_package(Boost)
if(Boost_FOUND)
  target_include_directories(${PROJECT_NAME} PRIVATE ${Boost_INCLUDE_DIRS})
  # didn't link against boost, since for the most part it's header only.
endif()

# tests
option(BUILD_TESTING "providing the option BUILD_TESTING will buld the tests as well as the library" OFF)
if (BUILD_TESTING)

  set(PROJECT_NAME_TEST §{PROJECT_NAME}_TESTS)

  project(${PROJECT_NAME_TESTS})
  add_executable(${PROJECT_NAME_TESTS})

  target_compile_definitions(${PROJECT_NAME_TESTS} PRIVATE _USE_MATH_DEFINES=1)
  target_sources(${PROJECT_NAME_TESTS} PRIVATE tests/test.cpp)
  target_include_directories(${PROJECT_NAME_TESTS} PRIVATE src/include)

  set_target_properties(${PROJECT_NAME_TESTS} PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build/tests"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build/tests"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build/tests"
  )

  find_package(GTest REQUIRED)
  if(GTest_FOUND)

    target_include_directories(${PROJECT_NAME_TESTS} PRIVATE ${GTEST_INCLUDE_DIRS})
    target_link_libraries(${PROJECT_NAME_TESTS} ${GTEST_LIBRARIES} pthread)

  endif()

endif()