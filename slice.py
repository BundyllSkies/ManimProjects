from manim import *

class PizzaSlice(Scene):
    def construct(self):
        # Create circle
        circle = Circle(radius=3.0, color=WHITE)

        # Set number of points
        numPoints = 6

        # Calculate the needed angles and get the corresponding points
        angles = [n * (360/numPoints) for n in range(numPoints)]
        points = [circle.point_at_angle(n*DEGREES) for n in angles]
        circleDots = [Dot(p, 0.07, color=RED).set_z_index(1.0) for p in points]

        # Get the arcs to join each point to the centre
        arcs = [ArcBetweenPoints(d.get_center(), circle.get_center(), radius=3.0).set_z_index(0.0) for d in circleDots]

        # Adding centre dot
        circleDots.append(Dot(circle.get_center(), 0.07, color=RED).set_z_index(1.0))

        #lines = Line(arcs[2].get_start(), arcs[1].get_arc_center())
        centrePoints = [Point(a.get_arc_center()) for a in arcs]
        # --- Animations ---

        #
        self.play(Create(circle))
        for d in circleDots:
            self.play(Create(d))
        for a in arcs:
            self.play(Create(a))
        self.play(FadeOut(VGroup(circleDots)))
        #self.add(lines)
        for p in centrePoints:
            self.add(p)
        self.wait(1.0)

