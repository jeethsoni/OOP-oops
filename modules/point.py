class Point:
    """
    point class to store 2D points
    """

    # initializing the attribute
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """magic method to show string representation"""

        return f"String representation of points: ({self.x}, {self.y})"

    def __eq__(self, other):
        """magic method to check for equaltiy between 2 objects created"""

        return (f"Eqality of two instances: {(self.x, self.y) == (other.x, other.y)}")  # noqa
