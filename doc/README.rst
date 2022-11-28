.. image:: https://i.imgur.com/IOdIA3y.png
      :target: https://github.com/iamd4rk/truthordare.py
      :alt: "truthordare.py"

Info
=========

An easy to use `Truth or Dare
API <https://docs.truthordarebot.xyz/api-docs>`__ wrapper written in
`Python <https://www.python.org/>`__.


Main Features
==================

-  Very easy to use
-  Covers entire API


Installation
=================

   **Python v3.8 or above is recommended**

.. code:: sh

   # Windows
   py -3 -m pip install truthordare.py


   # Linux/macOS
   python3 -m pip install truthordare.py


Import
==========

.. code:: py

   import truthordare

Commands
-------------

   You can use the following Funtions :- truth() , dare() , paranoia() , wyr() , nhie()

**Example**
~~~~~~~~~~~~~~~~

.. code:: py

   import truthordare

   print(truthordare.truth())
   print(truthordare.dare())
   print(truthordare.nhie())
   print(truthordare.wyr())
   print(truthordare.paranoia())


With rating parameter
~~~~~~~~~~~~~~~~~~~~~~~~~
..

   Valid Paramaters are: - "PG" , "PG13" , "R"

.. code:: py

   import truthordare

   print(truthordare.truth("PG"))



