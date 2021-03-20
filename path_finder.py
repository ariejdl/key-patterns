import numpy as np
from path_utils import *

def path_find(position, direction, walls, size):
    '''
    args: take position and direction
    return: list of new positions and directions

    rough algorithm
    - Find all adjacent parallel walls within 1/2 square
    - Continue in current direction until intersect with wall or come to end of adjacent wall
    - if intersection
    -    then backtrack 1/2 square from nearest intersection point
    -    Bifurcate in two directions parallel to wall
    -    Find any intersections, if intersection <= 1/2 square distant it is invalid
    -    otherwise recurse for each valid bifurcation
    - elif have adjacent
    -    find end adjacent point
    -    test if double back is out of bounds
    -    if in bounds then double back along the adjacent wall and recurse
    '''
    min_x, max_x, min_y, max_y = get_min_max_walls(walls)
    max_d = max(max_x - min_x, max_y - min_y)

    ray = np.array([
        position[0],
        position[1],
        position[0] + direction[0] * max_d * size,
        position[1] + direction[1] * max_d * size
    ])
    
    adjacent = []
    intersecting = []
    for wall in walls:
        # may want to change this so its from 'position' not 'ray'
        if lines_parallel(tuple(ray), tuple(wall)):

            vns = vector_normals(*direction)

            # could check wall start and end against ray here instead
            # then pick further end
            end1, end2 = np.array(wall).reshape(2,2)
            i_point1 = point_adjacent(end1, vns, ray, 0.25 * size)
            i_point2 = point_adjacent(end2, vns, ray, 0.25 * size)
            if i_point1 is not None and i_point2 is None:
                adjacent.append((np.array(wall), *i_point1))
            elif i_point2 is not None and i_point1 is None:
                adjacent.append((np.array(wall), *i_point2))
            elif i_point1 is not None and i_point2 is not None:
                # find point that is further away
                if dist(*end1, *position) > dist(*end2, *position):
                    adjacent.append((np.array(wall), *i_point1))
                else:
                    adjacent.append((np.array(wall), *i_point2))

        point = intersect(ray, wall)
        if point is not None:
            intersecting.append((point, wall, dist(*point, *position)))

    use_intersect = False
    use_adjacent = False
    if len(intersecting):
        pt, wall, _ = sorted(intersecting, key=lambda v: v[2])[0]
        d = np.array(direction)
        norm_scaled = 1 / abs(d).sum()
        stop_pt = np.array(pt) + np.array(direction) * -0.5 * size * norm_scaled

    if len(adjacent):
        # find furthest end of nearest adjacent that is still past position
        nearest_adj_wall, adj_end, _, n = sorted(
            adjacent, key=lambda v: dist(*v[1], *position))[0]
        n *= -1
        
    if len(intersecting) and not len(adjacent):
        use_intersect = True
    elif len(adjacent) and not len(intersecting):
        use_adjacent = True
    elif len(intersecting) and len(adjacent):
        if dist(*position, *stop_pt) < dist(*position, *adj_end):
            use_intersect = True
        else:
            use_adjacent = True

    if use_intersect:
        print(d, norm_scaled, stop_pt)
    #print(tuple(ray))
    print(len(intersecting), len(adjacent), use_intersect, use_adjacent)

    if use_intersect:
        segment = np.array([
            position[0],
            position[1],
            stop_pt[0],
            stop_pt[1]
        ])

        direction1 = unit_vector(line_to_vector(wall))
        direction2 = direction1 * -1
        ray1 = np.array([
            stop_pt[0],
            stop_pt[1],
            stop_pt[0] + direction1[0] * 0.5 * size,
            stop_pt[1] + direction1[1] * 0.5 * size
        ])
        ray2 = np.array([
            stop_pt[0],
            stop_pt[1],
            stop_pt[0] + direction2[0] * 0.5 * size,
            stop_pt[1] + direction2[1] * 0.5 * size
        ])

        print(tuple(ray1))
        print(tuple(ray2))

        if not any_intersect(ray1, walls):
            yield (stop_pt, direction1, [])
        if not any_intersect(ray2, walls):
            yield (stop_pt, direction2, [])

    elif use_adjacent:
        end = adj_end
        #print('*', end)
        proposed_double_bk = np.array(end) + np.array(direction) * size
        if proposed_double_bk[0] > max_x or \
            proposed_double_bk[1] > max_y:
            # out of bounds, so end with this line
            yield (end, None, [])
            return

        # - if in bounds then double back along the adjacent wall and recurse
        # doubling back:
        # - 1/4 past end of line
        d = np.array(direction)
        past_end = end + (d * size / 4)
        # - 1/2 distance in direction of normal closest to end
        new_start = past_end + n * size/2
        parts = [
            (*position, *past_end),
            (*past_end, *new_start)
        ]
        new_dir = np.array(direction) * -1
        yield (new_start, new_dir, parts)
    else:
        # out of bounds, so end with this line
        box_walls = np.array([
            [min_x, min_y, max_x, min_y],
            [min_x, min_y, min_x, max_y],
            [min_x, max_y, max_x, max_y],
            [max_x, min_y, max_x, max_y]
        ])
        for wall in box_walls:
            point = intersect(ray, wall)
            if point is not None:
                yield (position, None, [])

class PathFind():
    def __init__(self, position, direction, walls, size):
        self.walls = walls
        self.size = size
        self.current_heads = [(position, direction)]

    def step(self):
        new_heads = []
        for pos, direction in self.current_heads:
            for new_pos, new_dir, paths in path_find(pos, direction, self.walls, self.size):
                if len(paths):
                    for path in paths:
                        yield path
                else:
                    yield (*pos, *new_pos)
                if new_dir is not None:
                    new_heads.append((new_pos, new_dir))
        self.current_heads = new_heads