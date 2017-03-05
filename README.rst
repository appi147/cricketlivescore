.. highlight:: python
   :linenothreshold: 5
.. highlight:: rst
.. code-block:: python
   :emphasize-lines: 32,34

==============================
cricketlivescore Documentation
==============================


------------
Installation
------------

  Enter the following code in terminal::

     pip install cricketlivescore

  pip is needed to be installed. If ubuntu install it as::

     sudo apt-get install python-pip



-----------
Description
-----------

  cricketlivescore contains only one function get() which returns a list. Items of the list can be accessed as::

   scores = cricketlivescore.get()
   for score in scores:
   	print score.title
