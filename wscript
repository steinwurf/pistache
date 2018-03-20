#! /usr/bin/env python
# encoding: utf-8

import os

APPNAME = 'pistache'
VERSION = '1.0.0'


def configure(conf):
    if conf.is_mkspec_platform('linux'):

        if not conf.env['LIB_PTHREAD']:
            conf.check_cxx(lib='pthread')

def build(bld):

    bld.env.append_unique(
        'DEFINES_STEINWURF_VERSION',
        'STEINWURF_PISTACHE_VERSION="{}"'.format(
            VERSION))

    use_flags = []
    if bld.is_mkspec_platform('linux'):
        use_flags += ['PTHREAD']

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
        use=use_flags,
        export_includes=[include_path]
    )
    if bld.is_toplevel():
        # Only build tests when executed from the top-level wscript,
        # i.e. not when included as a dependency
        bld.recurse('test')
        bld.recurse('examples')
