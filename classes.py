class Vertex:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        return (self.x, self.y, self.z)

    def set_coordinates(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def difference_vector(self, other):
        if not isinstance(other, Vertex):
            raise ValueError("Argument must be a Vertex")
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return (dx, dy, dz)
    
    # instance method for a calculation (e.g., distance to another vert)
    def distance_to(self, other):
        dx, dy, dz = self.difference_vector(other)
        return (dx**2 + dy**2 + dz**2)**0.5 # Euclidean distance

v1 = Vertex(1,2,3)
v2 = Vertex(4,5,6)
print(v1.get_coordinates())
v1.set_coordinates(10,20,30)
print(v1.distance_to(v2))

class Cube:
    def __init__(self, origin, size):
        if not isinstance(origin, Vertex):
            raise ValueError("Origin must be a vertex")
        # Define 8 vertices based on origin (bottom-front-left) and size
        size *= 0.5
        self.vertices = [
            Vertex(origin.x - size, origin.y - size, origin.z - size), # Vertex 0
            Vertex(origin.x + size, origin.y - size, origin.z - size), # Vertex 1
            Vertex(origin.x + size, origin.y + size, origin.z - size), # Vertex 2
            Vertex(origin.x - size, origin.y + size, origin.z - size), # Vertex 3
            Vertex(origin.x - size, origin.y - size, origin.z + size), # Vertex 4
            Vertex(origin.x + size, origin.y - size, origin.z + size), # Vertex 5
            Vertex(origin.x + size, origin.y + size, origin.z + size), # Vertex 6
            Vertex(origin.x - size, origin.y + size, origin.z + size) # Vertex 7
        ]   
        
    # Instance method to get all vertices
    def get_vertices(self):
        return [v.get_coordinates() for v in self.vertices]
    
    # Instance method to calculate volume (using side length from vertices)
    def volume(self):
        side_length = self.vertices[1].x - self.vertices[0].x # Assuming uniform size
        return side_length ** 3

    # Instance method to translate the entire cube
    def translate(self, dx, dy, dz):
        for v in self.vertices:
            v.set_coordinates(v.x + dx, v.y + dy, v.z + dz)

origin_vertex = Vertex(0,0,0)
my_cube = Cube(origin_vertex, 1)
verts = my_cube.get_vertices()
for v in verts:
    print(v)
print(my_cube.volume())
my_cube.translate(10,10,10)
print(my_cube.get_vertices())


