from setuptools import setup, find_packages

"""
--> python setup.py sdist bdist_wheel // python setup.py sdist // python -m build // 
--> after that u need to install twine for it.
---> pip install -e . => this will install the package but not in the site-packages dir but it just take the refrence from
        the existing running package. which you can modify on the go and check the effects of changes directly.
--> pip install -e .[dev] => this is to install the lib with the developers depedencies module.
"""

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="unittestmanual",  # Replace with your own username
    version="1.0.0",
    author="sahilSingh",
    author_email="sahils@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "blessings ~= 1.7"
    ],
    extra_requires={
        "dev": [
            "pytest>=3.7",
        ]
    },
    package_dir={"": "src"},
    packages=find_packages(where="src", include="src.unitTest"),
    python_requires=">=3.6",
)