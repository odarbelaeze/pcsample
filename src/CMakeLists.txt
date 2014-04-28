include_directories(${voro++_SOURCE_DIR}/inc)

find_package(Boost 1.54)
if(Boost_FOUND)

    include_directories("${Boost_INCLUDE_DIRS}")
    set(Boost_USE_STATIC_LIBS OFF)
    set(Boost_USE_MULTITHREADED ON)
    set(Boost_USE_STATIC_RUNTIME OFF)
    find_package(Boost 1.54 COMPONENTS program_options)

    add_executable(pcsample main.cc)
    target_link_libraries(pcsample ${Boost_LIBRARIES} voro)

elseif(NOT Boost_FOUND)
    message(FATAL_ERROR "Unable to find the correct Boost version")
endif()

