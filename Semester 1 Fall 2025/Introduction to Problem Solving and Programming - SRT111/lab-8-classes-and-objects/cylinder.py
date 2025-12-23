# Define the Cylinder class
class Cylinder:
    
    def __init__(self, height=1, radius=1):
      """
        Constructor that initializes the height and radius of the cylinder.
        Default values are 1 if no arguments are provided.
        """
        self._height = height
        self._radius = radius

    def volume(self):
        """
        Calculates and returns the volume of the cylinder.
        Formula: π * r^2 * h
        """
        # TODO: Complete this method by calculating and returning the volume
        pass

    def surface_area(self):
        """
        Calculates and returns the surface area of the cylinder.
        Formula: 2πr^2 + 2πrh
        """
        top = 3.14 * (self._radius ** 2)
        return (2 * top) + (2 * 3.14 * self._radius * self._height)
