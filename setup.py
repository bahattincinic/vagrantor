from setuptools import setup

setup(
    name='vagrantor',
    version='0.1',
    packages=['vagrantor'],
    url='https://github.com/bahattincinic/vagrantor',
    license='MIT',
    author='Bahattin Cinic',
    author_email='bahattincinic@gmail.com',
    description='Vagrant configuration file generator',
    entry_points={
        'console_scripts': [
            'vagrantor = vagrantor.__main__:main',
        ],
    },
    dependency_links=[
        'http://github.com/kennethreitz/clint/tarball/master#egg=clint'
    ],
    install_requires=[
        'jinja2',
        'clint'
    ],
)
