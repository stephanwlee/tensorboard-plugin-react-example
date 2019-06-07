import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRED_PACKAGES = [
    'werkzeug >= 0.11.15',
    'tensorboard >= 1.13.0',
]

setuptools.setup(
    name="tensorboard_plugin_react",
    version="0.0.1",
    author="React-based plugin Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github./pypa/sampleproject",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "tensorboard_plugins": [
            "tensorboard_plugin_react=tensorboard_plugin_react.react_plugin:ReactPlugin",
        ],
    },
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
