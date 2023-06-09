cmake_minimum_required(VERSION 3.10.2)
project(android-jni-wrappers)

set(CMAKE_CXX_STANDARD 17)

set(JNIPP_PATH "${CMAKE_CURRENT_SOURCE_DIR}/..")
file(GLOB ANDROID_WRAPPERS *.cpp)

add_library(android-jni-wrappers STATIC
    ${ANDROID_WRAPPERS}
    ${JNIPP_PATH}/jnipp.cpp)
target_include_directories(
    android-jni-wrappers
    PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}
    PUBLIC ${JNIPP_PATH}
    PRIVATE ${JNI_INCLUDE_DIRS})