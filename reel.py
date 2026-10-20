from manim import *

# Вертикальный кадр (9:16)
config.frame_width = 9
config.frame_height = 16
config.background_color = "#0B1B4D"


class Diagonal(Scene):
    def construct(self):
        sq = Square(side_length=5, color=WHITE, stroke_width=6).shift(UP * 2)
        one_a = MathTex("1").next_to(sq, DOWN)
        one_b = MathTex("1").next_to(sq, LEFT)
        diag = Line(sq.get_corner(DL), sq.get_corner(UR),
                    color=YELLOW, stroke_width=8)

        eq1 = MathTex(r"1^2 + 1^2 = d^2").scale(1.6).shift(DOWN * 2.5)
        eq2 = MathTex(r"d^2 = 2").scale(1.6).move_to(eq1)
        eq3 = MathTex(r"d = \sqrt{2}", color=YELLOW).scale(2).move_to(eq1)

        self.play(Create(sq), run_time=1.5)
        self.play(Write(one_a), Write(one_b))
        self.play(Create(diag))
        self.play(Write(eq1))
        self.wait(0.5)
        self.play(ReplacementTransform(eq1, eq2))
        self.play(ReplacementTransform(eq2, eq3))
        self.play(Indicate(eq3))
        self.wait(1)


class Fractions(Scene):
    def construct(self):
        title = MathTex(r"\sqrt{2} = 1.41421356\ldots", color=YELLOW)
        title.scale(1.3).to_edge(UP, buff=2)
        self.play(Write(title))

        rows = [
            r"\frac{7}{5} = 1.4",
            r"\frac{17}{12} = 1.4166\ldots",
            r"\frac{41}{29} = 1.4137\ldots",
            r"\frac{99}{70} = 1.4142857\ldots",
        ]
        group = VGroup()
        for tex in rows:
            row = VGroup(
                MathTex(tex),
                MathTex(r"\neq \sqrt{2}", color=RED),
            ).arrange(RIGHT, buff=0.5)
            group.add(row)
        group.arrange(DOWN, buff=0.8).next_to(title, DOWN, buff=1.2)

        for row in group:
            self.play(FadeIn(row, shift=RIGHT * 0.5), run_time=0.8)
            self.wait(0.3)
        self.wait(1)


class Rationalize(Scene):
    def construct(self):
        a = MathTex(r"\frac{1}{\sqrt{2}}").scale(2.5)
        b = MathTex(r"\frac{1 \cdot \sqrt{2}}{\sqrt{2} \cdot \sqrt{2}}").scale(1.7)
        c = MathTex(r"\frac{\sqrt{2}}{2}", color=YELLOW).scale(2.5)

        self.play(Write(a))
        self.wait(1)
        self.play(TransformMatchingTex(a, b))
        self.wait(1)
        self.play(TransformMatchingTex(b, c))
        self.play(Indicate(c))
        self.wait(1)