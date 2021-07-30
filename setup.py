from setuptools import setup

setup(
    name='mntport',
    version='0.1',
    py_modules= ['mntport'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        mntport=mntport:cli
    ''',  

)