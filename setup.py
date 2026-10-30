from setuptools import setup # type: ignore

APP = ['main.py']
DATA_FILES = ['assets']
OPTIONS = {
    'argv_emulation': True,
    'includes': ['_math_integer'], 
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)