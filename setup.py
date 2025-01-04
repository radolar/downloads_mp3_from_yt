from setuptools import setup

APP = ['mp3.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': [],  # Add any necessary packages here
    'bdist_base': 'custom_build_dir'  # Custom build directory to avoid conflicts
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)