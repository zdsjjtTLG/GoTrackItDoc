Welcome to GoTrackIt's documentation!
=========================================


.. note::

    The English document has not yet been fully translated...


Read UserManual in ：`Chinese <https://gotrackit.readthedocs.io/en/latest/index.html>`_

Author: Tang Kai

Email：tangkai@zhechengdata.com、794568794@qq.com

Project source code：`GitHub <https://github.com/zdsjjtTLG/TrackIt>`_ --- Current version v0.3.10

GoTrackIt is a Map-Matching python package based on the Hidden Markov Model.

It matches the vehicle's GPS trajectory data to the road network through probabilistic graph modeling, and obtains the standardized spatiotemporal trajectory of the vehicle.It can effectively support travel navigation, traffic monitoring, traffic management, carbon emission accounting, traffic modeling and other directions.

.. image:: _static/images/MapMatch-en.PNG
    :align: center

-----------------------------------------------------


The application areas of Map-Matching are as follows：

* Travel navigation
    General Navigation、Lane Level Navigation、Traffic behavior warning

* Traffic monitoring
    Real-time traffic calculation、Intersection delay calculation、Real-time public transportation、Traffic monitoring

* Traffic management
    Traffic tracing analysis、Travel behavior analysis、Traffic congestion analysis

* Carbon emission accounting
    Emissions accounting、Road network emission characteristics

* Traffic modeling and other directions
    Road network integration、Bus/road network matching


.. note::

   This project is in a period of frequent upgrades and iterations. The current version is v0.3.10. Please update in time.

.. note::
    Due to the differences in computers of different users, it is difficult to unify the CRS output format in Geopandas. Starting from v0.3.5, the CRS check for geographic vector files has been completely removed. Users need to ensure that the CRS of the input geometry vector layer is EPSG:4326.


Document Content
--------------------------

.. toctree::

    Introduction
    HowToUse
    QuickStart
    ClassMethod
    IterationRecords
