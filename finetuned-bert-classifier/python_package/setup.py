from __future__ import absolute_import
from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = ("transformers", "datasets", "tqdm", "cloudml-hypertune")

setup(
    name="trainer",
    version="0.1",
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description="Vertex AI | Training | PyTorch | Text Classification | Python Package",
)
