💡Introduction
===================================

1. About Gotrackit
--------------------------

This map matching package implements probabilistic modeling of continuous GPS points based on Hidden Markov Model (HMM). This package can be used to easily perform map matching on GPS data. The main features of this open source package are：

* Comprehensive data preprocessing tools😻
    Provide road network processing optimization tools；
    Provide GPS sample data production module to solve the problem of no GPS data;
    Provides GPS data cleaning interface, including itinerary segmentation, sliding window noise reduction, data frequency reduction, stop point identification, and point density enhancement.


* Complete documentation☑️
    Chinese and English documents with detailed operation instructions;
    The explanation of the algorithm principle does not involve complex formula derivation, and uses animation to analyze the algorithm principle, which is concise and clear.


* Matching algorithm optimization🚀
    Support FastMapMatching based on path pre-calculation, support multi-core parallel matching, and support grid parameter search;
    The preliminary path based on HMM matching is optimized, and the disconnected locations will be automatically searched and completed. For the locations that are disconnected in the actual road network, warning messages will be output to facilitate users to trace back the problems.


* Matching results support animation visualization🌈
    The matching results are output in three forms: GPS point matching result table (csv), matching result vectorized layer, and vector layer matching animation (HTML file). HTML animation allows users to intuitively experience the matching results and improves the efficiency of troubleshooting.


.. image:: _static/images/极稀疏轨迹匹配.gif
    :align: center

-------------------------------------


.. image:: _static/images/匹配动画样例1.gif
    :align: center

-------------------------------------


.. image:: _static/images/匹配动画样例2.gif
    :align: center

-------------------------------------


.. image:: _static/images/匹配动画样例3.gif
    :align: center

-------------------------------------


.. image:: _static/images/匹配动画样例4.gif
    :align: center

-------------------------------------

.. image:: _static/images/geojson_res.jpg
    :align: center

-------------------------------------


**WeChat Chat Group**

.. image:: _static/images/wxq.jpg
    :align: center



2. MapMatch Problem
------------------------------

.. image:: _static/images/MapMatch.PNG
    :align: center

-----------------------------------------------------


3. Related video tutorials
------------------------------

 `Animated version of map matching algorithm based on Hidden Markov Model (HMM)! <https://www.bilibili.com/video/BV1gQ4y1w7dC>`_

 `A python package handles road network acquisition + map matching! <https://www.bilibili.com/video/BV1nC411z7Vg>`_

 `Detailed explanation and troubleshooting of map matching package parameters <https://www.bilibili.com/video/BV1qK421Y7hV>`_

 `QGIS road network topology display, base map loading, style reuse, and map saving <https://www.bilibili.com/video/BV1Sq421F7QX>`_


.. [Ref] 《Hidden Markov map matching through noise and sparseness》,Paul Newson & John Krumm