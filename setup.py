from setuptools import setup

setup(
    name='delete_dirs',
    version='0.1',
    packages=[''],
    url='https://github.com/korhun/delete_dirs',
    license='',
    author='Koray',
    author_email='korhun@gmail.com',
    description='',
    install_requires= [
        "PyYAML==6.0",
        "matplotlib<3.3",  # for PyInstaller
    ]
)