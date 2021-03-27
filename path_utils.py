import numpy as np
import math

def of_multiples(across, down):
    direction = 0
    x = 0
    while True:
        x1 = x
        x2 = x1 + across
        yield ()

def of_order():
    pass

# https://gist.github.com/kylemcdonald/6132fc1c29fd3767691442ba4bc84018
# intersection between line(p1, p2) and line(p3, p4)
def intersect(line1, line2):
    x1,y1,x2,y2 = line1
    x3,y3,x4,y4 = line2
    denom = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
    if denom == 0: # parallel
        return None
    ua = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / denom
    if ua < 0 or ua > 1: # out of range
        return None
    ub = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / denom
    if ub < 0 or ub > 1: # out of range
        return None
    x = x1 + ua * (x2-x1)
    y = y1 + ua * (y2-y1)
    return (x,y)

def any_intersect(line, lines):
    for other_line in lines:
        if intersect(line, other_line):
            return True
    return False

def lines_parallel(line1, line2):
    x1,y1,x2,y2 = line1
    x3,y3,x4,y4 = line2
    denom = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
    if denom == 0: # parallel
        return True
    return False

def line_projection(line1, line2):
    return np.dot(line1, line2) / np.linalg.norm(line2)

def dist(x1, y1, x2, y2):
    return math.sqrt((y2 - y1) ** 2) + math.sqrt((x2 - x1) ** 2)

# https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line#Line_defined_by_two_points
def point_line_dist(x0, y0, line):
    x1, y1, x2, y2 = line
    numerator = abs((x2 - x1) * (y1 - y0) - (x1 - x0) * (y2 - y1))
    denom = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return numerator / denom

def line_to_vector(line):
    return np.array([line[2] - line[0], line[3] - line[1]])

def unit_vector(v):
    return v / abs(np.array(v)).max()

# https://stackoverflow.com/questions/1243614/
def normals(line):
    x1, y1, x2, y2 = line
    dx = x2 - x1 
    dy = y2 - y1
    return unit_vector(
        np.array([[-dy, dx],
                  [dy, -dx]]))

def vector_normals(x, y):
    return unit_vector(
        np.array([[-y, x],
                  [y, -x]]))

def point_adjacent(pt, normals, line, max_d):
    for n in normals:
        normal_ray = (*pt, *(pt + n * max_d))
        i_point = intersect(normal_ray, line)
        if i_point is not None:
            final_dist = dist(*pt, *i_point)
            return (tuple(i_point), final_dist, n)
    return None

def get_min_max_walls(walls):
    xs = np.concatenate([
        np.array(walls)[:,0],
        np.array(walls)[:,2]
    ])
    ys = np.concatenate([
        np.array(walls)[:,1],
        np.array(walls)[:,3]
    ])
    return [xs.min(), xs.max(), ys.min(), ys.max()]

def simple_wall(p_, vec, len):
    p = np.array(p_)
    return np.array([*p, *(p + np.array(vec) * len )])
