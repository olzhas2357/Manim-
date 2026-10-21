from manim import *

# Вертикальный формат 9:16. Разрешение задаём флагом -r при запуске.
config.frame_width = 9.0
config.frame_height = 16.0
config.background_color = "#0B1B4D"

FONT = ""  # если казахские буквы отображаются неверно: FONT = "Arial"


def fit(mob, max_width):
    """Уменьшает объект, если он шире max_width."""
    if mob.width > max_width:
        mob.set_width(max_width)
    return mob


def make_label(symbol, text, color, font_size, max_width):
    sym = MathTex(symbol, color=color, font_size=font_size * 1.2)
    txt = Text("— " + text, font=FONT, font_size=font_size, color=color)
    label = VGroup(sym, txt).arrange(RIGHT, buff=0.15)
    return fit(label, max_width)


def make_row(items, color, scale, buff, max_width):
    row = VGroup(*[MathTex(t, color=color) for t in items]).scale(scale)
    row.arrange(RIGHT, buff=buff)
    return fit(row, max_width)


class NumberSetsKazakh(Scene):
    def construct(self):
        title = Text("Сандар жиындарының иерархиясы",
                     font=FONT, font_size=36, color=WHITE)
        fit(title, 8.0).move_to(UP * 7.2)
        self.play(Write(title), run_time=1.5)

        # ℝ: нақты сандар
        r_ell = Ellipse(width=8.6, height=13.4, color=BLUE,
                        fill_opacity=0.2).move_to(DOWN * 0.4)
        r_label = make_label(r"\mathbb{R}", "Нақты сандар",
                             BLUE_A, 26, 3.4).move_to(UP * 5.4)
        self.play(Create(r_ell), FadeIn(r_label, shift=DOWN * 0.3), run_time=1.5)

        # 𝕀: иррационал сандар (ℚ-дан тыс, ℝ ішінде)
        i_ell = Ellipse(width=6.4, height=2.8, color=ORANGE,
                        fill_opacity=0.3).move_to(UP * 3.5)
        i_label = make_label(r"\mathbb{I}", "Иррационал сандар",
                             ORANGE, 24, 4.2).move_to(UP * 4.25)
        i_row = make_row([r"\pi", r"e", r"\sqrt{2}", r"\sqrt{5}",
                          r"\sqrt{11}", r"\varphi"],
                         WHITE, 0.8, 0.45, 5.2).move_to(UP * 3.2)
        self.play(Create(i_ell), FadeIn(i_label), Write(i_row), run_time=1.5)

        # ℚ: рационал сандар
        q_ell = Ellipse(width=7.0, height=8.0, color=GREEN,
                        fill_opacity=0.25).move_to(DOWN * 2.6)
        q_label = make_label(r"\mathbb{Q}", "Рационал сандар",
                             GREEN_A, 24, 3.6).move_to(UP * 0.45)
        q_row = make_row([r"\frac{1}{2}", r"2\frac{3}{4}",
                          r"-0{,}333\ldots", r"0{,}75"],
                         WHITE, 0.65, 0.4, 5.0).move_to(DOWN * 0.35)
        self.play(Create(q_ell), FadeIn(q_label), Write(q_row), run_time=1.5)

        # ℤ: бүтін сандар
        z_ell = Ellipse(width=5.6, height=5.4, color=YELLOW,
                        fill_opacity=0.25).move_to(DOWN * 3.7)
        z_label = make_label(r"\mathbb{Z}", "Бүтін сандар",
                             YELLOW, 22, 3.2).move_to(DOWN * 1.8)
        z_row = make_row(["-5", "-1", "-3", "0", "17"],
                         WHITE, 0.8, 0.45, 4.4).move_to(DOWN * 2.75)
        self.play(Create(z_ell), FadeIn(z_label), Write(z_row), run_time=1.5)

        # ℕ: натурал сандар
        n_ell = Ellipse(width=3.8, height=2.6, color=RED,
                        fill_opacity=0.3).move_to(DOWN * 4.9)
        n_label = make_label(r"\mathbb{N}", "Натурал сандар",
                             RED_A, 20, 2.6).move_to(DOWN * 4.25)
        n_row = make_row(["1", "2", "7", "9", "100"],
                         WHITE, 0.6, 0.25, 3.0).move_to(DOWN * 5.4)
        self.play(Create(n_ell), FadeIn(n_label), Write(n_row), run_time=1.5)

        # √2 иррационал сандардың ішінде екенін көрсетеміз
        self.play(Indicate(i_row[2], color=YELLOW, scale_factor=1.8), run_time=1.5)
        self.wait(3)