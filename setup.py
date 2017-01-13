import setuptools

setuptools.setup(
    name="nbserverproxy",
    version='0.1.0',
    url="https://github.com/ryanlovett/nbserverproxy",
    author="Ryan Lovett",
    description="Jupyter server extension to proxy web services",
    packages=setuptools.find_packages(),
    install_requires=[ 'tornado', 'notebook' ],
)
