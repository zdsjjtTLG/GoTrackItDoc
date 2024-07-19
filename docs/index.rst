Welcome to GoTrackIt's documentation!
=========================================

Read UserManual in ：`Chinese <https://gotrackit.readthedocs.io/en/latest/index.html>`_

Author: Tang Kai

Email：tangkai@zhechengdata.com、794568794@qq.com

Project source code：`项目GitHub主页 <https://github.com/zdsjjtTLG/TrackIt>`_ --- Current version v0.3.7

GoTrackIt is a map matching package based on the Hidden Markov Model. It matches the vehicle's GPS trajectory data to the road network through probabilistic graph modeling, and obtains the standardized spatiotemporal trajectory of the vehicle. It can effectively support travel navigation, traffic monitoring, traffic management, carbon emission accounting, traffic modeling and other directions.

.. image:: _static/images/MapMatch.PNG
    :align: center

-----------------------------------------------------


.. image:: _static/images/application.PNG
    :align: center

-----------------------------------------------------------------------------

.. note::

   This project is in a period of frequent upgrades and iterations. The current version is v0.3.7. Please update in time.

.. note::
    Due to the differences in computers of different users, it is difficult to unify the CRS output format in Geopandas. Starting from v0.3.5, the CRS check for geographic vector files has been completely removed. Users need to ensure that the CRS of the input geometry vector layer is EPSG:4326.


文档内容
--------

.. toctree::

    Introduction
    HowToUse
    ClassMethod
    IterationRecords
