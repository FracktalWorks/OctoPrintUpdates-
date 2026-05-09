from setuptools import setup, find_packages

setup(
    name="octoprint_ControlCenter",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "octoprint",
    ],
    entry_points={
        "octoprint.plugin": [
            "ControlCenter = octoprint_ControlCenter"
        ]
    },
)
