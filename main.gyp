{
  'target_defaults': {
    'conditions': [
      [ 'OS=="win"', {
        'sources': [
          'src/explorer_command.cc',
          'src/explorer_command.def',
        ],
        'include_dirs': [
          'deps/wil/include',
        ],
        'defines': [
          '_WINDLL',
          'WIN32_LEAN_AND_MEAN',
          '_UNICODE',
          'UNICODE',
          '_CRT_SECURE_NO_DEPRECATE',
          '_CRT_NONSTDC_NO_DEPRECATE',
        ],
        'msvs_settings': {
          'VCLinkerTool': {
            'AdditionalOptions': [
              '/guard:cf',
            ],
            'OptimizeReferences': 2,             # /OPT:REF
            'EnableCOMDATFolding': 2,            # /OPT:ICF
          },
          'VCCLCompilerTool': {
            'AdditionalOptions': [
              '/Zc:__cplusplus',
              '-std:c++17',
              '/Qspectre',
              '/guard:cf',
            ],
            'BufferSecurityCheck': 'true',
            'ExceptionHandling': 1,               # /EHsc
            'EnableFunctionLevelLinking': 'true',
            'Optimization': 3,              # /Ox, full optimization
          },
        },
        'libraries': [
          '-ladvapi32.lib',
          '-lruntimeobject.lib',
          '-lshlwapi.lib',
          '-lonecore.lib',
        ]
      }],
    ],
  },
  'targets': [{
    'target_name': 'codium_explorer_command',
    'type': 'shared_library',
    'defines': [
      'EXE_NAME="VSCodium.exe"',
    ],
    'conditions': [
      [ 'OS=="win"', {
        'conditions': [
          ['target_arch=="x86"', {
            'TargetMachine' : 1,              # /MACHINE:X86
            'defines': [ 
              'DLL_UUID="18877606-DAD0-495D-BC63-1AFE7AE1421E"',
            ],
          }],
          ['target_arch=="x64"', {
            'TargetMachine' : 17,             # /MACHINE:X64
            'defines': [ 
              'DLL_UUID="738B8814-DF7F-4E12-9408-A406928BA4A5"',
            ],
          }],
          ['target_arch=="arm64"', {
            'TargetMachine' : 18,             # /MACHINE:ARM64 https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.vcprojectengine.machinetypeoption?view=visualstudiosdk-2022
            'defines': [ 
              'DLL_UUID="EAB622C6-23B0-461A-9D93-F033C101C00D"',
            ],
          }],
        ],
      }],
    ],
  }, {
    'target_name': 'codium_insiders_explorer_command',
    'type': 'shared_library',
    'defines': [
      'EXE_NAME="VSCodium - Insiders.exe"',
      'INSIDER=1',
    ],
    'conditions': [
      [ 'OS=="win"', {
        'conditions': [
          ['target_arch=="x86"', {
            'TargetMachine' : 1,              # /MACHINE:X86
            'defines': [ 
              'DLL_UUID="E4020A7F-81EF-4D44-A39E-F1B5939CBE3D"',
            ],
          }],
          ['target_arch=="x64"', {
            'TargetMachine' : 17,             # /MACHINE:X64
            'defines': [ 
              'DLL_UUID="24EA9688-2FCD-49FC-9B8F-25283351AD01"',
            ],
          }],
          ['target_arch=="arm64"', {
            'TargetMachine' : 18,             # /MACHINE:ARM64
            'defines': [ 
              'DLL_UUID="D255504C-24B7-456B-9A81-80BF73A5762C"',
            ],
          }],
        ],
      }],
    ],
  }],
}