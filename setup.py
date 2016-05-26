from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='python_vibration_motor',
    version='0.1',
    description='Library for using grove vibration motors',
    long_description=readme(),
    url='https://github.com/modular-CAT/python_vibration_motor',
    author='Daniel Smith',
    author_email='',
    license='MIT',
    packages=['python_vibration_motor'],
    install_requires=[
        'Adafruit_BBIO',
    ],
    zip_safe=False)
