#!/usr/bin/env python3
from __future__ import print_function
from shutil import copy
import os
import sys

codium_clsid_map = {
  'x86': '18877606-DAD0-495D-BC63-1AFE7AE1421E',
  'x64': '738B8814-DF7F-4E12-9408-A406928BA4A5',
  'arm64': 'EAB622C6-23B0-461A-9D93-F033C101C00D'
}

codium_insiders_clsid_map = {
  'x86': 'E4020A7F-81EF-4D44-A39E-F1B5939CBE3D',
  'x64': '24EA9688-2FCD-49FC-9B8F-25283351AD01',
  'arm64': 'D255504C-24B7-456B-9A81-80BF73A5762C'
}

root = os.path.dirname(os.path.dirname(__file__))
out_dir = os.path.join(root, 'out')
pkg_type = sys.argv[1]
arch = sys.argv[2]
pkg_dir = os.path.join(out_dir, pkg_type + '_explorer_pkg_' + arch)

# Create output directory.
os.mkdir(pkg_dir)

# Update AppxManifest.
manifest = os.path.join(root, 'template', 'AppxManifest.xml')
with open(manifest, 'r') as f:
  content = f.read()
  content = content.replace('@@PackageDLL@@', pkg_type + '_explorer_command.dll')
  content = content.replace('@@PackageDescription@@', pkg_type + ' context menu handler')
  if pkg_type == 'codium':
    content = content.replace('@@PackageName@@', 'VSCodium.VSCodium')
    content = content.replace('@@PackageDisplayName@@', 'VSCodium')
    content = content.replace('@@Application@@', 'VSCodium.exe')
    content = content.replace('@@ApplicationIdShort@@', 'VSCodium')
    content = content.replace('@@MenuID@@', 'OpenWithVSCodium')
    content = content.replace('@@CLSID@@', codium_clsid_map[arch])
  if pkg_type == 'codium_insiders':
    content = content.replace('@@PackageName@@', 'VSCodium.VSCodiumInsiders')
    content = content.replace('@@PackageDisplayName@@', 'VSCodium - Insiders')
    content = content.replace('@@Application@@', 'VSCodium - Insiders.exe')
    content = content.replace('@@ApplicationIdShort@@', 'VSCodiumInsiders')
    content = content.replace('@@MenuID@@', 'OpenWithVSCodiumInsiders')
    content = content.replace('@@CLSID@@', codium_insiders_clsid_map[arch])

# Copy AppxManifest file to the package directory.
manifest_output = os.path.join(pkg_dir, 'AppxManifest.xml')
with open(manifest_output, 'w+') as f:
  f.write(content)