import setuptools

with open("README.md", "r", encoding = "utf-8") as ld:
    long_description = ld.read()

setuptools.setup(
    name = "spoke2writ",
    version = 1.0,
    author = "Samarth Khanna",
    author_email = "samarthkhanna0@gmail.com",
    description = "Package for spoken to written English conversion",
    long_description = long_description,
    url = "https://github.com/SamarthKhanna/SpokenToWrittenEnglish",
    license = 'MIT',
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where = "src/s2w_pkg"),
    python_requires=">=3",
)

