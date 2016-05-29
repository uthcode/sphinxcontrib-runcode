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

When using ideone for for runcode, you need to create an account with http://ideone.com/account and provide your
**APIUSER** and **APIPASSWORD** in the file: `sphinxcontrib/runcode.py`

Use this option only when you build this extension locally, **do not bundle the APIUSER and APIPASSWORD and upload
the .tar.gz file to be pip-installable from any location.

* Create the tar.gz packager your set your APIUSER and APIPASSWORD and then do the pip install on your local system.

::

    pip install sphinxcontrib-runcode-0.2.0.tar.gz

This extension will take the runcode rules in the sphinx files and replace it with a big green button, pointing to
running this in the IDEONE ide.

This will create a file `codemap.json` which is a mapping of the particular source file and the IDEONE location.

Supported Values
================

* Language: C, Python
* codesite: codepad, ideone


Runbook
=======
To create a tar.gz

    python setup.py sdist
    
Install it locally

    pip install dist/sphinxcontrib-runcode-0.0.2.tar.gz


Create build and codemap.json

::

    make html


Commit codemap.json

::

    git add codemap.json
    git commit -am "Updated Code Mappings."


Using it with readthedocs.org
=============================

If you are using it readthedocs.org, do not provide **APIUSER** and **APIPASSWORD**, instead build it locally and
update the `codemap.json` and publish your updated `codemap.json` everytime the your repository code changes.
