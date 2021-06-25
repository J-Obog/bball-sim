from setuptools import setup, find_packages

pkgs = find_packages()
print(pkgs)

setup(
    name='bball',
    version='1.0',
    description='Basketball Simulation',
    url='https://github.com/J-Obog/bball-sim',
    author='JObog',
    author_email='jobogbaimhe@gmail.com',
    license='MIT',
    packages=pkgs,
    zip_safe=False
)