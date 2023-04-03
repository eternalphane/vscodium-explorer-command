#!/usr/bin/env python3
from __future__ import print_function
from shutil import copy
import os
import sys

codium_clsid_map = {
  'x86': '0632BBFB-D195-4972-B458-53ADEB984588',
  'x64': '1C6DF0C0-192A-4451-BE36-6A59A86A692E',
  'arm64': 'F5EA5883-1DA8-4A05-864A-D5DE2D2B2854'
}

codium_insiders_clsid_map = {
  'x86': 'B9949795-B37D-457F-ADDE-6A950EF85CA7',
  'x64': '799F4F7E-5934-4001-A74C-E207F44F05B8',
  'arm64': '7D34756D-32DD-4EE6-B99F-2691C0DAD875'
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