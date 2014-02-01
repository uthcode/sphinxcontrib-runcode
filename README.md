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
       :language: C
       :codesite: codepad

Or

    .. runcode:: path/to/your/file
       :language: C
       :codesite: ideone

Ideone
======

When using ideone for for runcode, you need to create an account with
http://ideone.com/account and provide your **APIUSER** and **APIPASSWORD**
in the file: sphinxcontrib/runcode.py

* Create the tar.gz packager **after*your set your APIUSER and APIPASSWORD and
  then do the pip install.

* Dont expose your APIUSER and APIPASSWORD. Since ideone does not oauth, others
  can use yours if you use.



This will get replaced by

    Run This.

Which the use can click and visit codepad.org to run directly.

Supported Values
================

* Language: C, Python
* codesite: codepad, ideone


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


