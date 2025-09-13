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

        # Joining the arc ends with the centre of the neighboring arc
        arcCentres = [Point(a.get_midpoint()) for a in arcs]
        arcCentreDots = [Dot(p.location, 0.07, color=BLUE).set_z_index(0.0) for p in arcCentres]
        arcEndDots = [Dot(a.get_start(), 0.07, color=BLUE).set_z_index(0.0) for a in arcs]
        lines = []
        for i in range(1, numPoints):
            lines.append(Line(arcs[i].get_start(), arcCentres[i-1]))
        lines.append(Line(arcs[0].get_start(), arcCentres[5]))

        # Create polygons from the shapes
        pizzaSlices = []
        pizzaSlices.append(ArcPolygonFromArcs(arcs[1], 
                            ArcBetweenPoints(start=arcCentres[0].location, end=circle.get_center(), radius=3.0),
                            ArcBetweenPoints(lines[1].get_start(), lines[1].get_end(), radius=None), 
                            color=PURPLE).set_z_index(2.0))


        # --- Animations ---

        self.play(Create(circle))
        self.play(FadeIn(VGroup(circleDots)))
        for a in arcs:
            self.play(Create(a))
        self.play(FadeOut(VGroup(circleDots)))
        self.play(FadeIn(VGroup(arcCentreDots + arcEndDots)))
        for l in lines:
            self.play(Create(l))
        for pz in pizzaSlices:
            self.play(Create(pz))
        self.wait(1.0)

