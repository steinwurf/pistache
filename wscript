#! /usr/bin/env python
# encoding: utf-8

import os

APPNAME = 'pistache'
VERSION = '1.0.1'


def configure(conf):
    if conf.is_mkspec_platform('linux') and not conf.env['LIB_PTHREAD']:
        conf.check_cxx(lib='pthread')

def build(bld):

    bld.env.append_unique(
        'DEFINES_STEINWURF_VERSION',
        'STEINWURF_PISTACHE_VERSION="{}"'.format(
            VERSION))

    use_flags = []
    if bld.is_mkspec_platform('linux'):
        use_flags += ['PTHREAD']

    pistache_path = bld.root.find_dir(bld.dependency_path('pistache-source'))
    src_path = pistache_path.ant_glob('src/**/*.cc')
    include_path = pistache_path.find_dir('include/')

    bld.stlib(
        features='cxx',
        source=src_path,
        includes=[include_path],
        target='pistache',
        use=use_flags,
        defines=['ONLY_C_LOCALE=1'],
        export_includes=[include_path]
    )
    if bld.is_toplevel():
        # Only build tests when executed from the top-level wscript,
        # i.e. not when included as a dependency
        bld.recurse('test')
        bld.recurse('examples')
