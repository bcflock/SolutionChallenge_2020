from setuptools import setup

setup(
    name='app',
    packages=['project'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)