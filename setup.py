import setuptools

version = "0.0.7"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TableauScraper",
    version=version,
    author="Bertrand Martel",
    author_email="bmartel.fr@gmail.com",
    description="Library to get data from Tableau Viz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bertrandmartel/tableau-scraping",
    packages=["tableauscraper"],  # setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
    python_requires=">=3.6",
    install_requires=["beautifulsoup4>=4.0.0", "pandas", "requests>=2.14.0"],
)
