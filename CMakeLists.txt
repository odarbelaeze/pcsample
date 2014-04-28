cmake_minimum_required(VERSION 2.8)
project(pcsample CXX)
subdirs(voro++)

include_directories(${pcsample_SOURCE_DIR}/inc)
include_directories(${pcsample_SOURCE_DIR}/voro++/inc)

find_package(Boost 1.54)

if(Boost_FOUND)

    include_directories("${Boost_INCLUDE_DIRS}")
    find_package(Boost 1.54 COMPONENTS program_options)
    add_executable(pcsample "src/SampleBase.cc" "src/main.cc")
    target_link_libraries(pcsample ${Boost_LIBRARIES} voro)

elseif(NOT Boost_FOUND)

    message(FATAL_ERROR "Unable to find the correct Boost version")

endif()

