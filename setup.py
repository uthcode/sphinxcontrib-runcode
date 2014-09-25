from setuptools import setup


NAME = "sphinxcontrib-runcode"
VERSION = "0.0.7"
DESCRIPTION = "Post included code in an executable pastebin like codepad / ideone."
LONG_DESCRIPTION = open('README.md').read()
AUTHOR = "Senthil Kumaran (Uthcode)"
AUTHOR_EMAIL = "senthil@uthcode.com"
LICENSE = "BSD"
URL = "http://github.com/uthcode/sphinxcontrib-runcode"
DOWNLOAD_URL = "https://github.com/uthcode/sphinxcontrib-runcode/tree/downloads/packages"
CLASSIFIERS = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Text Processing',
]
PLATFORMS = 'any'
REQUIRES = ['Sphinx']
# Dependency https://pypi.python.org/pypi/ideone/0.2.0
INSTALL_REQUIRES = ['ideone']
PACKAGES = ['sphinxcontrib']
ZIP_SAFE = False
INCLUDE_PACKAGE_DATA = True
NAMESPACE_PACKAGES = ['sphinxcontrib']


setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      url=URL,
      download_url=DOWNLOAD_URL,
      classifiers=CLASSIFIERS,
      platforms=PLATFORMS,
      requires=REQUIRES,
      install_requires=INSTALL_REQUIRES,
      packages=PACKAGES,
      zip_safe=ZIP_SAFE,
      include_package_data=INCLUDE_PACKAGE_DATA,
      namespace_packages=NAMESPACE_PACKAGES)


