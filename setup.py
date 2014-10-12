from setuptools import setup, find_packages

setup(
    name='vagrantor',
    version='0.3',
    packages=find_packages(),
    package_data={'vagrantor': ['templates/*.html']},
    include_package_data=True,
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
