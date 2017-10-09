#! /usr/bin/env python
# encoding: utf-8

import os

APPNAME = 'pistache'
VERSION = '0.0.0'


def build(bld):

    bld.env.append_unique(
        'DEFINES_STEINWURF_VERSION',
        'STEINWURF_PISTACHE_VERSION="{}"'.format(
            VERSION))

    pistache_path = bld.dependency_path('pistache-source')
    src_path = os.path.realpath(pistache_path)
    src_path = os.path.relpath(src_path, bld.root.abspath())
    src_path = '{}/src/**/*.cc'.format(src_path)

    include_path = '{}/include/'.format(pistache_path)

    bld.stlib(
        features='cxx',
        source=bld.root.ant_glob(src_path),
        includes=[include_path],
        target='pistache',
        use=[],
        export_includes=[include_path]
    )
