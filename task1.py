from manim import *

class TrapezoidSolution(Scene):
    def construct(self):
        # Масштабируем реальные координаты, чтобы фигура поместилась на экране
        s = 0.16

        A = LEFT * 9 * s + UP * 24 * s
        B = RIGHT * 9 * s + UP * 24 * s
        C = RIGHT * 16 * s
        D = LEFT * 16 * s
        O = UP * 12 * s

        # title = Text("Равнобедренная трапеция", font_size=32)
        # title.to_edge(UP)

        trapezoid = Polygon(A, B, C, D, color=BLUE, stroke_width=3)
        circle = Circle(radius=12 * s, color=YELLOW, stroke_width=3)
        circle.move_to(O)

        # Отрезки от центра до вершин
        OA = Line(O, A, color=GREEN, stroke_width=3)
        OD = Line(O, D, color=GREEN, stroke_width=3)

        # Радиус к основанию и высота трапеции
        radius_line = DashedLine(O, UP * 24 * s, color=YELLOW)
        height_line = DashedLine(ORIGIN, O, color=YELLOW)

        # Вершины и центр
        dots = VGroup(
            Dot(A), Dot(B), Dot(C), Dot(D),
            Dot(O, color=RED),
        )

        labels = VGroup(
            MathTex("A").next_to(A, UL, buff=0.08),
            MathTex("B").next_to(B, UR, buff=0.08),
            MathTex("C").next_to(C, DR, buff=0.08),
            MathTex("D").next_to(D, DL, buff=0.08),
            MathTex("O").next_to(O, RIGHT, buff=0.12),
        )

        # Длины от центра до вершин
        length_labels = VGroup(
            MathTex("15", color=GREEN).scale(0.8).next_to(OA, LEFT, buff=0.08),
            MathTex("20", color=GREEN).scale(0.8).next_to(OD, LEFT, buff=0.08),
            MathTex("r=12", color=YELLOW).scale(0.75).next_to(radius_line, RIGHT, buff=0.08),
        )

        base_labels = VGroup(
            MathTex("2a=18").scale(0.75).next_to((A + B) / 2, UP, buff=0.12),
            MathTex("2b=32").scale(0.75).next_to((D + C) / 2, DOWN, buff=0.12),
        )

        solution = MathTex(
            "S=\\frac{18+32}{2}\\cdot24=600"
        ).scale(0.9).to_edge(DOWN)

        self.play(Write(title))
        self.play(Create(trapezoid), FadeIn(dots), Write(labels))
        self.play(Create(circle), Create(OA), Create(OD))
        self.play(Create(radius_line), Create(height_line))
        self.play(Write(length_labels), Write(base_labels))
        self.play(Write(solution))
        self.wait(2)