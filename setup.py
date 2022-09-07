from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vidhyapeeth/__init__.py
from vidhyapeeth import __version__ as version

setup(
	name="vidhyapeeth",
	version=version,
	description="This app is made for site:- pushtisanskarvidhyapeeth.org",
	author="SanskarTechnoab",
	author_email="nilesh.pithiya@sanskrtechnolab.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
