import setuptools

version = "0.1.23"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TableauScraper",
    version=version,
    author="Bertrand Martel",
    author_email="bmartel.fr@gmail.com",
    description="Python library to scrape data from Tableau viz",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/bertrandmartel/tableau-scraping",
    packages=["tableauscraper"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
    python_requires=">=3.6",
    install_requires=["beautifulsoup4>=4.0.0", "pandas", "requests>=2.14.0"],
)
