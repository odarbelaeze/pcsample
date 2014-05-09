include_directories(${voro++_SOURCE_DIR}/inc)

set(voro_SOURCES
   cell.cc
   common.cc
   container.cc
   unitcell.cc
   v_compute.cc
   c_loops.cc
   v_base.cc
   wall.cc
   pre_container.cc
   container_prd.cc
)

add_library(voro STATIC ${voro_SOURCES})
add_library(voroshared SHARED ${voro_SOURCES})

add_executable(voro++ cmd_line.cc)
target_link_libraries(voro++ voro)
