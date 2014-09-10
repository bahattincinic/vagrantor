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
    install_requires=[
        'jinja2',
        'clint'
    ],
)
