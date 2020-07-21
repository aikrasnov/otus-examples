import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


# https://stackoverflow.com/questions/58533084/what-keyword-arguments-does-setuptools-setup-accept
setuptools.setup(
    name="example-pkg-akrasnov-test", # Replace with your own username
    platforms="linux",
    version="0.0.4",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aikrasnov",
    # packages=setuptools.find_packages(),
    packages=["foo"],
    keywords='sample setuptools development',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    # A boolean (True or False) flag specifying whether the project can be safely installed and run from a zip file. If this argument is not supplied, the bdist_egg command will have to analyze all of your project’s contents for possible problems each time it builds an egg.
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=["requests==2.23.0"]
)

# sdist -- source distribution
# python -m pip install --upgrade setuptools wheel
# Не забыть показать help
# python setup.py sdist bdist_wheel
# python setup.py build
# https://test.pypi.org/account/register/
# https://test.pypi.org/manage/account/#api-tokens
# python -m pip install --user --upgrade twine
# python -m twine upload --repository testpypi dist/*
# https://test.pypi.org/project/example-pkg-YOUR-USERNAME-HERE/
# pip --help
#  -i,--index-url <url>
#           Base URL of Python Package Index (default https://pypi.python.org/simple/).
#
#    --extra-index-url <url>
#           Extra URLs of package indexes to use in addition to --index-url.