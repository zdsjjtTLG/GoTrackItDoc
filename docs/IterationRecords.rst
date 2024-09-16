🖥️Iteration record
==================================

1. v0.1.1
--------------------

* Update date
    2023.12.15

* Update description
    - Launched HMM matching core function

    - Launched kepler visualization result module

2. v0.1.3
--------------------

* Update date
    2023.12.29

* Update description
    - Added sample GPS data production function

3. v0.1.5
--------------------

* Update date
    2024.01.25

* Update description
    - Added path-based reverse production road network function module

4. v0.1.6
--------------------

* Update date
    2024.02.11

* Update description
    - Fixed GPS interpolation BUG

    - Added projection point information and path distance between adjacent observations to the matching results

    - Optimized the road network reverse module

5. v0.1.7
--------------------

* Update date
    2024.03.06

* Update description
    - Improved map matching efficiency

    - Fixed the BUG that caused floating point underflow due to probability multiplication

    - Added road network connectivity repair function

    - Optimized the road network reverse module

    - Added GPS point actual section information to the GPS generation module

    - Added data check interface to the matching results

6. v0.1.8
--------------------

* Update date
    2024.03.17

* Update description
    - Fixed the connectivity check BUG in road network generation

    - In the map matching process, an error message is given for "GPS data is not associated with any road network"

7. v0.1.9
--------------------

* Update date
    2024.03.29

* Update Notes
    - Added GPS densification function

    - Introduced GPS point differential direction vector to correct emission probability

    - Upgraded map matching interface, easier to use, and exposed more adjustable parameters

    - Construction of Net object is limited to: the input link and node data must be WGS-84 EPSG:4326 geographic coordinates, the plane projection coordinate system no longer needs to be manually specified, and the 6-degree zone can be automatically determined

    - Added road network processing function: section division function

    - Added road network processing function: section-link_id field, from_node field, to_node field, node-node_id field remapping function

    - Fixed the bug of negative speed in GPS generation interface

    - Fixed the problem of memory overflow caused by too large node ID during Net initialization

    - Added path cache switch and ID cache switch parameters

8. v0.2.0
--------------------

* Update Date
    2024.04.12

* Update Notes
    - Added multi-process parameters in the matching process and multi-process parameters in the topology optimization process

    - Selection of GPS candidate sections: In addition to buffer selection, the top_k parameter is introduced to specify the nearest top_k sections in the buffer as candidate sections

    - Added GPS point stop point recognition function

    - Fixed the BUG of inconsistent coordinates in the matching results, now unified as EPSG:4326

    - Added the function of extracting OD with waypoints based on GPS data

    - Added road network processing functions: road section and node reshaping

    - Fixed some bugs

9. v0.2.1
--------------------

* Update date
    2024.04.18

* Update description
    - Removed geo_res_fldr from the map matching interface, geojson files and html are stored in the same directory, specify html_fldr, and add other storage parameters (see document)

    - Added warning section information in the HTML file. If a warning appears in this match, Then there will be an extra layer in the HTML file, which records the road sections where the GPS state transfer is wrong

    - Improved the stop point identification function

    - Bug fixes

10. v0.2.2
--------------------

* Update date
    2024.04.27

* Update notes
    - Vectorization transformation, while introducing the path pre-calculation mechanism, greatly improving the matching efficiency

    - Remove the multi-core matching interface on a single track, and add a parallel matching interface on multiple tracks

    - Optimize the error reporting mechanism, add output warning information and error information, and facilitate user backtracking

    - Bug fixes

11. v0.2.3
--------------------

* Update date
    2024.05.07

* Update notes

    - Optimize the efficiency of the map matching interface, a slight improvement compared to v0.2.2

    - Optimize the error reporting mechanism of the map matching interface

    - Remove the html_fldr parameter from the map matching interface, and use out_fldr instead

    - The map matching interface adds an instant output switch instant_output. When turned on, the result is stored immediately after each matched track

    - Road network construction: crs judgment BUG fixed, overseas road network construction failure BUG fixed

    - Add loop processing function

12. v0.2.4
--------------------

* Update date
    2024.05.08

* Update description

    - Map matching interface efficiency optimization, slightly improved compared to v0.2.3

13. v0.2.7
--------------------

* Update date
    2024.05.19

* Update description

    - Map matching interface efficiency optimization, slightly improved compared to v0.2.4

    - Added grid parameter search to help users determine reasonable matching parameters

    - BUG fixed

14. v0.2.9
--------------------

* Update date
    2024.06.03

* Update description

    - Sample GPS generation module: interface simplification, bug fixes

    - Road network reverse module-request function optimization

    - GPS-based OD production interface: efficiency optimization

    - Online GPS trip segmentation interface

    - Connectivity repair module BUG (extremely low probability, but very harmful) fixed

    - Map matching BUG (extremely low probability, but very harmful) fixed

15. v0.3.0
--------------------

* Update date
    2024.06.10

* Update description

    - Road network reverse module: add multi-core parallel reverse parameters to improve the efficiency of large-scale road network acquisition

    - Road network reverse module: launch multi-region road network merging interface

    - Map matching: introduce spatial hierarchical indexing mechanism to improve the spatial correlation efficiency of large-scale road networks and long trajectories

    - Map matching: minor BUG fixes, partial code writing optimization

    - Map matching: remove two parameters: max_increment_times, increment_buffer

16. v0.3.1
--------------------

* Updated on
    2024.06.16

* Updated instructions

    - Improved robustness of the program

    - Map matching interface: Optimized duplicate points in the geometry column of the road network layer

17. v0.3.3
--------------------

* Updated on
    2024.06.24

* Updated instructions
    - Map matching interface: Optimized the penalty logic for disconnected paths.

    - Map matching interface: Added the user_field_list parameter to allow users to specify the relevant fields of the GPS table to be output together with the matching results, to avoid users from making secondary associations after the matching is completed.

    - Map matching interface: Optimized the output of the matching result fields, and added loc_type to identify: source GPS data points, densified points, and supplementary points.

    - Map matching interface: Optimized the output of the matching result fields, and added the route_dis field to identify the path distance between the matching point on the matching section and the starting point of the section.

    - Map matching interface: Matching results - Added matching point heading angle and heading vector data.

18. v0.3.5
--------------------

* Updated on
    2024.06.29

* Updated instructions
    - Completely removed crs check for geographic vector files. Users need to ensure that the crs of the input geometry vector layer is EPSG:4326.

    - Map matching interface: redundant calculation code removed.

    - Plane projection coordinate system parameters: some interface parameter names in the old version are plain_prj, now unified as plain_crs.

19. v0.3.6
--------------------

* Updated on
    2024.07.02

* Updated instructions
    - Compatible with geopandas-v1.0.0

19. v0.3.7
--------------------

* Updated on
    2024.07.11

* Updated instructions
    - Fixed the BUG that caused some VsCode users to fail to visualize output.

20. v0.3.8
--------------------

* Update date
    2024.08.31

* Update description
    - Road network optimization module: node/section reshaping BUG fixed
    - Road network optimization module: point layer creation BUG fixed
    - Road network generation module: added high-precision map analysis
    - Road network reverse module: added planning strategy
    - Trajectory preprocessing module: integrated preprocessing interface, added Kalman filter preprocessing, line type simplification preprocessing
    - Map matching module: added real-time continuous matching interface
    - Map matching interface: optimize HTML storage time, improve efficiency by 40%
    - Other BUG fixed

21. v0.3.10
--------------------

* Update date
    2024.09.04

* Update description
    - Fixed time series calculation BUG