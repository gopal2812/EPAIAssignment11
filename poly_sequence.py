from polygon import Polygon


class Polygons:
    """
    Custom polygon sequence containing polygons where maximum number of edges in a polygon is given
    by m  and circumradius (R) for all polygons is is given by circumradius and is same for all polygons"
    """
    def __init__(self, m, r):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = r
        self._polygons = [Polygon(i, r) for i in range(3, m+1)]

    def __len__(self):
        """ This function gives the length of the Polygon Sequence object """
        return self._m - 2

    def __repr__(self):
        """ This function gives the details of the Polygon Sequence object"""
        return f'Polygons(m={self._m}, R={self._R})'

    def __getitem__(self, s):
        """ This function returns the properties of the polygon whose vertices,
        circumradius are as passed in the arguments."""
        return self._polygons[s]

    def __iter__(self):
        """Iterable Function--> This function returns the iterator for the
        Polygon object"""
        print("Calling Polygon instance __iter__")
        return self.PolygonIterator(self)

    @property
    def max_efficiency_polygon(self):
        """ This function returns the maximum efficiency polygon.
        Here, a maximum efficiency polygon is one that has the highest area to
        perimeter ratio."""
        sorted_polygons = sorted(self._polygons, key=lambda p: p.area/p.perimeter, reverse=True)
        return sorted_polygons[0]

    class PolygonIterator:
        """This is an Iterator for the polygons class"""
        def __init__(self, poly_obj):
            """Function initializing the polygon Iterator and
            index. Index is used to return the next element in the polygon
            sequence when used as a iterator"""

            # poly_obj is an instance of Polygons
            print("Calling PolygonIterator __init__")
            self._poly_obj = poly_obj
            self._index = 0

        def __iter__(self):
            """ PolygonIterator instance returning self"""
            print("Calling PolygonIterator instance __iter__")
            return self

        def __next__(self):
            """PolygonIterator next function which return the next element in
            Polygons sequence if current index is less than length of Polygons obj"""
            print("Calling PolygonIterator __next__")
            if self._index >= len(self._poly_obj):
                raise StopIteration
            else:
                item = self._polyobj._polygons[self._index]
                self._index += 1
                print(f'here: {self._index}')
                return item
