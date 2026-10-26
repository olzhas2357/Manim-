from manim import *


class TrapezoidSolution(Scene):
    def construct(self):
        # Координаты фигуры соответствуют решению:
        # a = 9, b = 16, r = 12, высота = 24.
        scale = 0.12
        shift = LEFT * 3.45 + DOWN * 0.25

        def point(x, y):
            return scale * (x * RIGHT + y * UP) + shift

        A = point(-9, 24)
        B = point(9, 24)
        C = point(16, 0)
        D = point(-16, 0)
        O = point(0, 12)

        # Чертёж слева
        trapezoid = Polygon(A, B, C, D, color=BLUE_C, stroke_width=3)
        circle = Circle(radius=12 * scale, color=YELLOW, stroke_width=2.5)
        circle.move_to(O)

        diagonal_OA = Line(O, A, color=GREEN_C, stroke_width=3)
        diagonal_OD = Line(O, D, color=GREEN_C, stroke_width=3)
        centerline = DashedLine(point(0, 0), point(0, 24), color=GRAY_B)
        radius = Line(O, point(0, 24), color=YELLOW, stroke_width=2.5)

        vertices = VGroup(*[
            Dot(p, radius=0.045, color=WHITE)
            for p in (A, B, C, D)
        ])
        center_dot = Dot(O, radius=0.055, color=RED_C)

        vertex_labels = VGroup(
            MathTex("A").scale(0.65).next_to(A, UL, buff=0.08),
            MathTex("B").scale(0.65).next_to(B, UR, buff=0.08),
            MathTex("C").scale(0.65).next_to(C, DR, buff=0.08),
            MathTex("D").scale(0.65).next_to(D, DL, buff=0.08),
            MathTex("O").scale(0.65).next_to(O, RIGHT, buff=0.08),
        )

        length_labels = VGroup(
            MathTex("15", color=GREEN_C).scale(0.65)
                .move_to((O + A) / 2 + LEFT * 0.18),
            MathTex("20", color=GREEN_C).scale(0.65)
                .move_to((O + D) / 2 + LEFT * 0.18),
            MathTex("r", color=YELLOW).scale(0.65)
                .next_to(radius, RIGHT, buff=0.06),
            MathTex("2a").scale(0.65)
                .next_to((A + B) / 2, UP, buff=0.08),
            MathTex("2b").scale(0.65)
                .next_to((D + C) / 2, DOWN, buff=0.08),
        )

        # Вычисления справа — только математические записи
        x = 2.35
        equations = VGroup(
            MathTex(r"a^2+r^2=15^2,\quad b^2+r^2=20^2"),
            MathTex(r"(a+b)^2=(b-a)^2+(2r)^2"),
            MathTex(r"r^2=ab"),
            MathTex(r"a(a+b)=225,\quad b(a+b)=400"),
            MathTex(r"\frac{b}{a}=\frac{400}{225}=\frac{16}{9}"),
            MathTex(r"a=9,\quad b=16,\quad r=12"),
            MathTex(r"S=(a+b)\cdot2r=600"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32)

        equations.scale(0.68)
        equations.move_to(RIGHT * x + DOWN * 0.15)

        # Чтобы формулы не выходили за края экрана
        for equation in equations:
            equation.set_x(x + equation.width / 2)

        # Чертёж появляется постепенно
        self.play(Create(trapezoid), run_time=3)
        self.play(Create(circle), Create(centerline), run_time=3)
        self.play(Create(diagonal_OA), Create(diagonal_OD), Create(radius), run_time=3)
        self.play(FadeIn(vertices), FadeIn(center_dot), run_time=2)
        self.play(Write(vertex_labels), run_time=3)
        self.play(Write(length_labels), run_time=3)
        self.wait(2)

        # Вывод решения по строкам
        for equation in equations:
            self.play(Write(equation), run_time=3)
            self.wait(3)

        self.wait(4)