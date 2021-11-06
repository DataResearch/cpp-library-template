cmake_minimum_required(VERSION 3.16)

set(PROJECT_NAME cpp_library_template)

project(${PROJECT_NAME})
add_library(${PROJECT_NAME} SHARED)
target_compile_definitions(${PROJECT_NAME} PRIVATE _USE_MATH_DEFINES=1)
set_target_properties(${PROJECT_NAME} PROPERTIES CXX_STANDARD 17)
set_target_properties(${PROJECT_NAME} PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build/lib"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build/lib"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build/bin"
)

target_include_directories(${PROJECT_NAME} PUBLIC src/include)

target_sources(${PROJECT_NAME} PRIVATE src/library.cpp)
target_sources(${PROJECT_NAME} PUBLIC src/include/project/library.h)

#libraries import
find_package(Boost)
if(Boost_FOUND)
  target_include_directories(${PROJECT_NAME} PRIVATE ${Boost_INCLUDE_DIRS})
  # didn't link against boost, since for the most part it's header only.
endif()

# build tests
option(BUILD_TESTING "providing the option BUILD_TESTING will buld the tests as well as the library" OFF)
if (BUILD_TESTING)

  enable_testing()

  add_executable(${PROJECT_NAME}_tests)
  
  target_compile_definitions(${PROJECT_NAME}_tests PRIVATE _USE_MATH_DEFINES=1)
  target_sources(${PROJECT_NAME}_tests PRIVATE tests/test.cpp)
  target_include_directories(${PROJECT_NAME}_tests PRIVATE src/include)
  target_link_libraries(${PROJECT_NAME}_tests ${PROJECT_NAME})

  set_target_properties(${PROJECT_NAME}_tests PROPERTIES CXX_STANDARD 17)
  set_target_properties(${PROJECT_NAME}_tests PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build/tests"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build/tests"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build/tests"
  )

  find_package(GTest REQUIRED)
  if(GTest_FOUND)

    target_include_directories(${PROJECT_NAME}_tests PRIVATE ${GTEST_INCLUDE_DIRS})
    target_link_libraries(${PROJECT_NAME}_tests ${GTEST_LIBRARIES} pthread)

  endif()

endif()