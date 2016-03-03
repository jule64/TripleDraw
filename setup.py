from setuptools import setup

setup(
        name='tripledraw',
        version='0.1',
        py_module=['tripledraw'],
        install_requires=[
            'click>=4.0',
            'ansicolors'
        ],
        author='julien monnier',
        author_email='jule64@gmail.com',
        entry_points='''
        [console_scripts]
        tripledraw=tripledraw:main
        ''',
)
