from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksBlueprintsGenerator',
    version='0.1.0',
    author='Guido Barbaglia',
    author_email='guido.barbaglia@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    description='Geobricks Blueprints Generator.',
    install_requires=[
        'watchdog', 'flask', 'flask-cors'
    ],
    url='http://pypi.python.org/pypi/GeobricksBlueprintsGenerator/'
)
