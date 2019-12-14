# -*- mode: python -*-

block_cipher = None


a = Analysis(['..\\src\\main.py',
              '..\\src\\win\\flashWin.py',
              '..\\src\\ui\\uicore.py',
              '..\\src\\run\\runcore.py',
              '..\\src\\ui\\uidef.py',
              '..\\src\\boot\\bltest.py',
              '..\\src\\boot\\commands.py',
              '..\\src\\boot\\memoryrange.py',
              '..\\src\\boot\\peripherals.py',
              '..\\src\\boot\\peripheralspeed.py',
              '..\\src\\boot\\properties.py',
              '..\\src\\boot\\status.py',
              '..\\src\\boot\\target.py',
              '..\\src\\targets\\MIMXRT1011\\bltargetconfig.py',
              '..\\src\\targets\\MIMXRT1015\\bltargetconfig.py',
              '..\\src\\targets\\MIMXRT1021\\bltargetconfig.py',
              '..\\src\\targets\\MIMXRT1052\\bltargetconfig.py',
              '..\\src\\targets\\MIMXRT1062\\bltargetconfig.py',
              '..\\src\\targets\\MIMXRT1064\\bltargetconfig.py',
              '..\\src\\run\\rundef.py',
              '..\\src\\utils\\filetools.py',
              '..\\src\\utils\\misc.py'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='NXP-MCUBootFlasher',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True,
          icon='..\\img\\NXP-MCUBootFlasher.ico')
