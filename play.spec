# -*- mode: python -*-

block_cipher = None

added_files = [
("resources", "resources")
]

a = Analysis(['play.py'],
             pathex=['C:\\Users\\Ari.DESKTOP-REV5O0M\\Google Drive\\University Stuff\\Year 3 NSC\\Group Project\\python-lander'],
             binaries=None,
             datas=added_files,
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
          name='Lander',
          debug=False,
          strip=False,
          upx=True,
          console=False )