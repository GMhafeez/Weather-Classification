import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    # metadata
    name="Weather-App",
    version="0.0.1",
    author="Ghulam Mustafa",
    author_email="gmhafee17@gmail.com",
    description="A small python package for Weather App ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gmhafee17/py_test",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'seaborn',
        'scikit-learn',
        'scipy',
        'statsmodels',
        'pyarrow',
        'pyyaml',
        'tqdm',
        'joblib',
        'torch'
    ],
)
