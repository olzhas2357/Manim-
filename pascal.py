from math import comb
from manim import *


class PascalTriangle(Scene):
    def construct(self):
        title = MathTex(r"(a+b)^n", color=YELLOW).scale(1.6)
        title.to_edge(UP, buff=1.5)
        self.play(Write(title))

        rows = 6
        dx, dy = 1.3, 1.1
        top = UP * 4.2

        cells = []
        for n in range(rows):
            row = []
            for k in range(n + 1):
                num = MathTex(str(comb(n, k))).scale(1.3)
                num.move_to(top + DOWN * dy * n + RIGHT * dx * (k - n / 2))
                if 0 < k < n:
                    num.set_color(BLUE_B)
                row.append(num)
            cells.append(row)

        self.play(Write(cells[0][0]))
        self.play(*[Write(c) for c in cells[1]], run_time=0.8)

        # каждое число = сумма двух чисел над ним
        for n in range(2, rows):
            self.play(
                *[Write(c) for c in cells[n]],
                Indicate(cells[n - 1][0], color=YELLOW),
                Indicate(cells[n - 1][1], color=YELLOW),
                run_time=1,
            )

        self.wait(0.5)

        # выделяем ряд 1 3 3 1
        box = SurroundingRectangle(VGroup(*cells[3]), color=YELLOW, buff=0.2)
        self.play(Create(box))

        formula = MathTex(
            r"(a+b)^3 = ", r"1", r"a^3", r"+", r"3", r"a^2b",
            r"+", r"3", r"ab^2", r"+", r"1", r"b^3",
        )
        if formula.width > 8.2:
            formula.set_width(8.2)
        formula.shift(DOWN * 5.5)
        for i in (1, 4, 7, 10):
            formula[i].set_color(YELLOW)

        self.play(Write(formula), run_time=2)
        self.play(Indicate(box))
        self.wait(1.5)
