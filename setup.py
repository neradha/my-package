from setuptools import find_packages
from setuptools import setup


setup(
    name="my-package",
    packages=find_packages(),
    version='1.0.1',
    description="Test",
    install_requires=["my-other-package @ git+https://github.com/neradha/my-other-package.git"],
    author="",
    license="",
)
