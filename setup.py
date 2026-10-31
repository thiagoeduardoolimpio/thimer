from setuptools import setup

APP = ['thimer.py']
DATA_FILES = ['assets']

OPTIONS = {
    'includes': ['_math_integer'],
    'iconfile': 'assets/icon.icns',
    'plist': {
    'CFBundleName': 'Thimer',
    'CFBundleDisplayName': 'Thimer',
    'CFBundleShortVersionString': '1.0.0-beta 1',
    'NSHumanReadableCopyright': 'Copyright © 2026 Thiago Olímpio',
},
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)