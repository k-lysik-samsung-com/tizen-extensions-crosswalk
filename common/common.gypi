{
  'variables': {
    # Copy conditionally-set variables out one scope.
    'extension_host_os%': '<(extension_host_os)',
    'extension_build_type%': '<(extension_build_type)',
    'extension_host_os%': 'mobile',
    'extension_build_type%': 'Debug',
  },
  'target_defaults': {
    'conditions': [
      ['extension_host_os != "mobile"', {
        'sources/': [['exclude', '_mobile\\.cc$|mobile/']],
        'includes/': [['exclude', '_mobile\\.gypi$|mobile/']],
      }],
      ['extension_host_os != "desktop"', {
        'sources/': [['exclude', '_desktop\\.cc$|desktop/']],
        'includes/': [['exclude', '_desktop\\.gypi$|desktop/']],
      }],
      ['extension_host_os == "mobile"', { 'defines': ['TIZEN_MOBILE'] } ],
      ['extension_host_os == "desktop"', { 'defines': ['GENERIC_DESKTOP'] } ],
      ['extension_build_type== "Debug"', {
        'defines': ['_DEBUG', ],
        'cflags': [ '-O0', '-g', ],
      }],
      ['extension_build_type == "Release"', {
        'defines': ['NDEBUG', ],
        'cflags': [
          '-O2',
          # Don't emit the GCC version ident directives, they just end up
          # in the .comment section taking up binary size.
          '-fno-ident',
          # Put data and code in their own sections, so that unused symbols
          # can be removed at link time with --gc-sections.
          '-fdata-sections',
          '-ffunction-sections',
        ],
      }],
    ],
    'includes': [
      'xwalk_js2c.gypi',
    ],
    'include_dirs': [
      '../',
      '<(SHARED_INTERMEDIATE_DIR)',
    ],
    'sources': [
      'extension_adapter.h',
      'picojson.h',
      'utils.h',
    ],
    'cflags': [
      '-fPIC',
      '-fvisibility=hidden',
    ],
  },
}