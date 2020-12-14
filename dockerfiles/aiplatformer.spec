# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import os
here = os.path.abspath('.')

a = Analysis([os.path.join(here, 'src', 'Game.py')],
             pathex=[os.path.join(here, 'src')],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

a.datas.extend(Tree(os.path.join(here, 'assets'), prefix='assets', typecode='DATA'))


exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='aiplatformer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
