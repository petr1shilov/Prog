block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Progi\\narutoo'],
             binaries=[],
             datas=[
                    ('car_down.png', '.'),
                    ('car_up.png', '.'),
                    ('hit_sound.mp3', '.'),
                    ('hp.png', '.'),
                    ('HP_car.png', '.'),
                    ('lose.mp3', '.'),
                    ('naruto.png', '.'),
                    ('road.png', '.')
             ],
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
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
