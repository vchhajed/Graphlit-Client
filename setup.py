from setuptools import setup, find_packages

setup(
    name='graphlit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyJWT',
    ],
    author='Vaibhav Chhajed',
    author_email='vaibhav787845@gmail.com',
    description='A package for creating tokens for Graphlit services',
    url='https://github.com/vchhajed/graphlit-client',
)
