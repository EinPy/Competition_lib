def vec(p1, p2):
    return p2[0]-p1[0], p2[1] - p1[1]

def sign(x):
    if x < 0: return -1
    return 1 if x > 0 else 0

def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]

def on_segment(p, q, r):
    """Check if point q lies on line segment 'pr'"""
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and 
        q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True
    return False

def is_segment_intersection(s1, s2):
    u = vec(*s1)
    v = vec(*s2)
    p1, p2 = s1
    q1, q2 = s2

    # Calculate cross products
    d1 = cross(u, vec(p1, q1))
    d2 = cross(u, vec(p1, q2))
    d3 = cross(v, vec(q1, p1))
    d4 = cross(v, vec(q1, p2))

    # Check general case
    if d1 != 0 or d2 != 0 or d3 != 0 or d4 != 0:
        return sign(d1) != sign(d2) and sign(d3) != sign(d4)

    # Check collinear case
    return (on_segment(p1, q1, p2) or on_segment(p1, q2, p2) or
            on_segment(q1, p1, q2) or on_segment(q1, p2, q2))

print(is_segment_intersection(((0,2),(2, 2)),((2, 0),(2,2))))

print(is_segment_intersection(((0,0),(2, 2)),((3, 3),(4,4))))