# Assignment11
EPAi Assignment11
##Description
The starting point for this project is the Polygon class and the Polygons sequence type we created in the previous project or mentioed in deepNote

###Goal
Refactor the Polygons (sequence) type, into an iterable. You'll need to implement both an iterable, and an iterator.

![image](https://user-images.githubusercontent.com/39087216/126877754-95428ec4-10be-4bdd-8f47-5d51b9f5e9b1.png)

### Polygon Class
1. A regular strictly convex polygon is a polygon that has the following characteristics:
    * All interior angles are less than 180
    * All sides have equal length

2. For a regular strictly convex polygon with vertices n and circumradius r:
    * interiorAngle = (n−2) * (180/n)
    * edgeLength, s = 2 * R * sin(π/n) 
    * apothem, a = R * cos(π/n)
    * area = (1/2) * n * a
    * perimeter = n * s
3. Create a Polygon Class:
     
     1. Where initializer takes in:
        * number of edges/vertices
        * circumradius
      2. That can provide these properties:
          * edges
          * vertices
          * interior angle
          * edge length
          * apothem
          * area
          * perimeter
      3. That has these functionalities:
          * a proper __repr__ function
          * implements equality (==) based on # vertices and circumradius (__eq__)
          * implements > based on number of vertices only (__gt__)

4.  Implement a Custom Polygon sequence type:
    
    1. Where initializer takes in:
        * number of vertices for largest polygon in the sequence
        * common circumradius for all polygons
        * that can provide these properties:
        * max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
     2. that has these functionalities:
        * functions as a sequence type (__getitem__)
        * supports the len() function (__len__)
        * has a proper representation (__repr__)

5.  Refactor the Polygons (sequence) type, into an iterable. You'll need to implement both an iterable, and an iterator.

```
class Polygon(builtins.object)
 |  Polygon(n, r)
 |  
 |  Polygon class to create polygons which are regular strictly convex.
 |  Regular strict polygons have two properties:
 |  1- All interior angles are less than 180.
 |  2- All sides have equal length
 |  
 |  Methods defined here:
 |  
 |  __eq__(self, other)
 |      Provides ability to compare two objects for euality (==).
 |  
 |  __gt__(self, other)
 |      Provide ability to compare two objects for greater than '>' test.
 |  
 |  __init__(self, n, r)
 |      Initialize the edges, circumradius, interiorAngle, edgeLength ,
 |      apothem, area, perimeter.
 |  
 |  __repr__(self)
 |      This function gives the details of the Polygon Sequence object
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  apothem
 |      apothem of the polygon
 |  
 |  area
 |      area of the polygon
 |  
 |  circumradius
 |      Circumradius of the polygon
 |  
 |  count_edges
 |      Number of edges in the polygon
 |  
 |  count_vertices
 |      Number of vertices in the polygon
 |  
 |  interior_angle
 |      Interior angle of the polygon
 |  
 |  perimeter
 |      perimeter of the polygon
 |  
 |  side_length
 |      side length of the polygon
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

class Polygons(builtins.object)
 |  Polygons(m, r)
 |  
 |  Custom polygon sequence containing polygons where maximum number of edges in a polygon is given
 |  by m  and circumradius (R) for all polygons is is given by circumradius and is same for all polygons"
 |  
 |  Methods defined here:
 |  
 |  __getitem__(self, s)
 |      This function returns the properties of the polygon whose vertices, 
 |      circumradius are as passed in the arguments.
 |  
 |  __init__(self, m, r)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self)
 |      Iterable Function--> This function returns the iterator for the 
 |      Polygon object
 |  
 |  __len__(self)
 |      This function gives the length of the Polygon Sequence object
 |  
 |  __repr__(self)
 |      This function gives the details of the Polygon Sequence object
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  max_efficiency_polygon
 |      This function returns the maximum efficiency polygon.
 |      Here, a maximum efficiency polygon is one that has the highest area to
 |      perimeter ratio.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  PolygonIterator = <class '__main__.Polygons.PolygonIterator'>
 |      This is an Iterator for the polygons class

class PolygonIterator(builtins.object)
 |  PolygonIterator(poly_obj)
 |  
 |  This is an Iterator for the polygons class
 |  
 |  Methods defined here:
 |  
 |  __init__(self, poly_obj)
 |      Function initializing the polygon Iterator and
 |      index. Index is used to return the next element in the polygon
 |      sequence when used as a iterator
 |  
 |  __iter__(self)
 |      PolygonIterator instance returning self
 |  
 |  __next__(self)
 |      PolygonIterator next function which return the next element in 
 |      Polygons sequence if current index is less than length of Polygons obj
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 ```
