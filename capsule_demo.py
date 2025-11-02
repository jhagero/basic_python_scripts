# ------------------------------------------------------------
# capsule_demo.py  –  pure Python 3.12, no external libraries
# ------------------------------------------------------------
from __future__ import annotations
from typing import Self, cast
from wrappers import smart_wrapper
import math

# ------------------------------------------------------------------
# 1. Vec3 – a minimal 3-D vector with only the ops we need
# ------------------------------------------------------------------
class Vec3:
    __slots__ = ("x", "y", "z")

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        self.x, self.y, self.z = float(x), float(y), float(z)

    @classmethod
    def zero(cls) -> Vec3:
        return cls(0,0,0)
    
    @classmethod
    def from_tuple(cls, t: tuple[float, float, float]) -> Vec3:  # ← Fixed
        return cls(*t)
    
    # arithmetic
    def __add__(self, other: Self) -> Self:
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: Self) -> Self:
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> Self:
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)
    
    __rmul__ = __mul__

    def __truediv__(self, scalar: float) -> Self:
        return Vec3(self.x / scalar, self.y / scalar, self.z / scalar)

    def __neg__(self) -> Self:
        return Vec3(-self.x, -self.y, -self.z)

    # ---------- useful math ----------
    def dot(self, other: Self) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length_sq(self) -> float:
        return self.dot(self)

    def length(self) -> float:
        return math.sqrt(self.length_sq())

    def normalized(self) -> Self:
        L = self.length()
        return self if L == 0 else self / L

    # ---------- pretty printing ----------
    def __repr__(self) -> str:
        return f"Vec3({self.x:.3f}, {self.y:.3f}, {self.z:.3f})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vec3):
            return NotImplemented
        return (abs(self.x - other.x) < 1e-9 and
                abs(self.y - other.y) < 1e-9 and
                abs(self.z - other.z) < 1e-9)
    
# ------------------------------------------------------------------
# 2. Helper math functions (pure Python)
# ------------------------------------------------------------------
def distance(a: Vec3, b: Vec3) -> float:
    """Euclidean distance between two points."""
    return (b - a).length()

def clamp(value: float, lo: float, hi: float) -> float:
    """Clamp value to [lo, hi]."""
    return max(lo, min(hi, value))

# ------------------------------------------------------------------
# 3. Capsule definition & collision test
# ------------------------------------------------------------------
class Capsule:
    """A capsule = line segment (A to B) + radius."""

    def __init__(self, a: Vec3, b: Vec3, radius: float) -> None:
        self.a = a
        self.b = b
        self.radius = float(radius)

    def __repr__(self) -> str:
        return f"Capsule(A={self.a}, B={self.b}, r={self.radius})"

    # ------------------------------------------------------------
    # Core test: is point P inside / touching the capsule?
    # ------------------------------------------------------------
    def contains_point(self, p: Vec3) -> bool:
        """
        Returns True if distance from p to the capsule ≤ radius.
        The algorithm works for the cylinder *and* both caps.
        """
        ab = self.b - self.a
        ap = p - self.a

        # Project p onto the infinite line through A-B
        proj = ap.dot(ab) / ab.length_sq()

        # Clamp to the segment [0, 1]
        t = clamp(proj, 0.0, 1.0)

        # Closest point on the *segment*
        closest = self.a + ab * t

        return distance(p, closest) <= self.radius

    # ------------------------------------------------------------
    # Bonus: capsule-capsule test (segment-to-segment distance)
    # ------------------------------------------------------------
    def intersects_capsule(self, other: "Capsule") -> bool:
        """True if the two capsules overlap."""
        # Find closest points between the two line segments
        c1, c2 = closest_points_segment_segment(
            self.a, self.b, other.a, other.b
        )
        return distance(c1, c2) <= self.radius + other.radius


# ------------------------------------------------------------------
# 4. Segment-to-segment closest points (used by capsule-capsule)
# ------------------------------------------------------------------
def closest_points_segment_segment(
    p1: Vec3, q1: Vec3, p2: Vec3, q2: Vec3
) -> tuple[Vec3, Vec3]:
    """
    Returns (closest_on_seg1, closest_on_seg2).
    Classic algorithm from Real-Time Collision Detection (Ericson).
    """
    d1 = q1 - p1
    d2 = q2 - p2
    r = p1 - p2

    a = d1.length_sq()
    e = d2.length_sq()
    f = d2.dot(r)

    EPS = 1e-9
    if a <= EPS and e <= EPS:          # both degenerate to points
        return p1, p2

    if a <= EPS:                       # first segment degenerate
        return p1, p2 + d2 * clamp(f / e, 0.0, 1.0)

    c = d1.dot(r)
    if e <= EPS:                       # second segment degenerate
        t = clamp(-c / a, 0.0, 1.0)
        return p1 + d1 * t, p2

    b = d1.dot(d2)
    denom = a * e - b * b

    # Parallel non-degenerate segments
    if denom != 0.0:
        t = clamp((b * f - c * e) / denom, 0.0, 1.0)
    else:
        t = 0.0

    s = clamp((b * t + f) / e, 0.0, 1.0)

    # Recompute t for the new s (to avoid numerical drift)
    if denom != 0.0:
        t = clamp((b * s + c) / a, 0.0, 1.0)

    c1 = p1 + d1 * t
    c2 = p2 + d2 * s
    return c1, c2


# ------------------------------------------------------------------
# 5. Demo / Playground
# ------------------------------------------------------------------
def demo() -> None:
    print("=== Capsule Collision Playground ===\n")

    # Build a vertical capsule (character style)
    cap = Capsule(
        a=Vec3(0, 2, 0),      # top of head
        b=Vec3(0, 0, 0),      # feet
        radius=0.5
    )
    print(f"Capsule: {cap}\n")

    # Helper to test a point
    @smart_wrapper
    def test_point(p: Vec3, label: str) -> None:
        hit = cap.contains_point(p)
        dist = distance(p, cap.a + (cap.b - cap.a) *
                        clamp((p - cap.a).dot(cap.b - cap.a) /
                              (cap.b - cap.a).length_sq(), 0.0, 1.0))
        print(f"{label:20} -> {'HIT' if hit else 'MISS'}  (dist={dist:.3f})")

    # 1. Middle height – just inside the cylinder
    test_point(Vec3(0.4, 1.0, 0), "Middle inside")
    # 2. Middle height – just outside
    test_point(Vec3(0.6, 1.0, 0), "Middle outside")
    # 3. Top cap
    test_point(Vec3(0.0, 2.4, 0), "Top cap inside")
    test_point(Vec3(0.0, 2.6, 0), "Top cap outside")
    # 4. Bottom cap
    test_point(Vec3(0.0, -0.4, 0), "Bottom cap inside")
    test_point(Vec3(0.0, -0.6, 0), "Bottom cap outside")
    # 5. Corner of a wall (diagonal)
    test_point(Vec3(0.4, 1.0, 0.4), "Diagonal corner")

    print("\n--- Capsule vs Capsule ---")
    other = Capsule(
        a=Vec3(1.0, 1.5, 0),
        b=Vec3(1.0, 0.5, 0),
        radius=0.4
    )
    print(f"Other capsule: {other}")
    print("Intersect?", cap.intersects_capsule(other))

    print("\n=== End of demo ===")


if __name__ == "__main__":
    demo()