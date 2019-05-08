Oro Sphinxdoc Integrity Check extension
=======================================

This extension allows to control content of rst document.
It can be useful to verify that examples in documentation with `literalinclude` of the files from code are still valid.

How to install
--------------
* Clone repository to any directory
* Edit your sphinx `conf.py` file to add extension: `extensions = ['oro.integrity_check']` 

Example of usage
----------------
index.rst
```
.. oro_integrity_check:: 207bafe71c5c3bf6530c9cf98d4f654126bdcaac

  My content

  .. literalinclude:: included_file.php
     :language: php
```

included_file.php
```
foo
===

Some intro text here...
```

In case of changing content of `included_file.php` this extension generates warning during documentation build process
to notify that content of file was changed without reviewing documentation where this file is used.
