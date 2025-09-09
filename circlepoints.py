from manim import *

class PointsOnCircle(Scene):
    def construct(self):
        circle = Circle(radius=3.0, color=GREEN)
        # Number of points required
        num_points = 16
        # Calculate each angle
        angles = [n * (360 / num_points) for n in range(num_points)]
        # Points on circumference of circle
        points = [circle.point_at_angle(n*DEGREES) for n in angles]
        # Create circles at each point
        circles = [Circle(radius=0.05, color=RED, fill_opacity=1).move_to(p) for p in points]
        # Add the circle to the scene
        self.add(circle)
        # Add each of the points to the scene
        for c in circles:
            self.add(c)