# q1.1
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

A = Point(1, 2)
B = Point(4, 6)

distance = math.sqrt((B.x - A.x)**2 + (B.y - A.y)**2)
print(distance)

# q1.2
mid_x = (A.x + B.x) / 2
mid_y = (A.y + B.y) / 2
print(mid_x, mid_y)

# q1.3
m = (B.y - A.y) / (B.x - A.x)
c = A.y - m * A.x
print(f"y = {m}x + {c}")

# q1.4
C = Point(3, 1)

d = (C.x + (C.y - c) * m) / (1 + m*m)
x_ref = 2*d - C.x
y_ref = 2*(d*m + c) - C.y
print(x_ref, y_ref)

# q2.1
import numpy as np

A = np.array([2, 3])
B = np.array([4, 1])
C = np.array([1, 5])

R = A + B + C
print(R)

# q2.2
print(np.linalg.norm(A))
print(np.linalg.norm(B))
print(np.linalg.norm(C))

# q2.3
print(np.dot(A, B))
print(np.dot(A, C))
print(np.dot(B, C))

# q2.4
def angle(v1, v2):
    cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1)*np.linalg.norm(v2))
    return math.degrees(math.acos(cos_theta))

print(angle(A, B))
print(angle(A, C))
print(angle(B, C))

# q2.5
proj = (np.dot(A, B) / np.dot(B, B)) * B
print(proj)

# q3.1
S = np.array([1, 2])
E = np.array([6, 5])
P = np.array([4, 3])

seg_len = np.linalg.norm(E - S)
print(seg_len)

# q3.2
t = np.dot(P - S, E - S) / np.dot(E - S, E - S)
t = max(0, min(1, t))
closest = S + t * (E - S)
print(closest)

# q3.3
dist_point_seg = np.linalg.norm(P - closest)
print(dist_point_seg)

# q4.1
a1, b1, c1 = 2, 3, 6
a2, b2, c2 = 4, 6, 12

det = a1*b2 - a2*b1

if det == 0:
    print("Lines are parallel or coincident.")
else:
    x = (c1*b2 - c2*b1) / det
    y = (a1*c2 - a2*c1) / det
    print(x, y)
