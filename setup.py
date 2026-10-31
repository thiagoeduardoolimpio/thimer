from setuptools import setup

APP = ['Thimer.py']
DATA_FILES = ['assets']

OPTIONS = {
    'includes': ['_math_integer'],
    'iconfile': 'assets/icon.icns',
     'plist': {
        'CFBundleName': 'Thimer',
        'CFBundleDisplayName': 'Thimer',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)