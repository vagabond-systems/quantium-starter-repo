from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).resolve().parent

# long description from README
long_description = (here / "README.md").read_text(encoding="utf8") if (here / "README.md").exists() else ""

# read install requirements from requirements.txt if present
requirements_file = here / "requirements.txt"
install_requires = []
if requirements_file.exists():
    install_requires = [r.strip() for r in requirements_file.read_text(encoding="utf8").splitlines() if r.strip() and not r.strip().startswith("#")]

setup(
    name="quantium-starter-repo",
    version="0.1.0",
    description="Quantium starter repository with a Dash visualiser for Pink Morsels sales",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="",
    license="MIT",
    url="https://github.com/lfariabr/quantium-starter-repo",
    packages=find_packages(exclude=["tests", "tests.*", "*.tests", "*.tests.*"]),
    include_package_data=True,
    install_requires=install_requires,
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
