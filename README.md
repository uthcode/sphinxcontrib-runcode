=====================
sphinxcontrib-runcode
=====================

Run the included code in pastebin like codepad.org or ideone.

Usage
=====

To enable this extension, add the following line to ``conf.py``::

    extensions.append('sphinxcontrib.runcode')

Now you can include a runnable link to your literalinclude file.

    .. runcode:: path/to/your/file
       :language: c
       :codesite: codepad


This will get replaced by

    Run This.

Which the use can click and visit codepad.org to run directly.

Supported Values
================

* Language: c, python
* codesite: codepad

Runbook
=======
To create a tar.gz

    python setup.py sdist

Download 
========

https://dl.dropbox.com/s/2y5eomikg8gqg9g/sphinxcontrib-runcode-0.0.1.tar.gz

pip install
===========

    pip install https://dl.dropbox.com/s/2y5eomikg8gqg9g/sphinxcontrib-runcode-0.0.1.tar.gz


