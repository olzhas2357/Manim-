from manim import *

# Вертикальное видео 9:16 для Reels
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = BLACK

A = 48291635
B = 71902846

FS = 36        # размер цифр
DX = 0.47      # ширина колонки
X_R = 3.6      # правый край чисел
Y0 = 6.2       # верхняя строка
DY = 0.62      # расстояние между строками

CLOCK_C = np.array([0, -3.6, 0])
CLOCK_R = 1.5


def make_row(s, shift, idx):
    """Строка цифр, выровненная по правому краю (как в столбике)."""
    digits = []
    for j, ch in enumerate(reversed(s)):
        d = Text(ch, font_size=FS, color=WHITE)
        d.move_to(np.array([X_R - (shift + j) * DX, Y0 - idx * DY, 0]))
        digits.append(d)
    return digits  # справа налево


def h_line(idx):
    y = Y0 - idx * DY + DY / 2 - 0.03
    return Line(
        np.array([X_R - 15 * DX - 0.3, y, 0]),
        np.array([X_R + 0.3, y, 0]),
        stroke_width=4,
        color=WHITE,
    )


class ColumnMult(Scene):
    def construct(self):
        np.random.seed(3)
        t = ValueTracker(0)  # 0 -> 1: полчаса на одно умножение

        # --- Часы: стрелка и закрашенный сектор ---
        def clock_face():
            g = VGroup(Circle(radius=CLOCK_R, stroke_color=WHITE, stroke_width=5).move_to(CLOCK_C))
            for k in range(12):
                a = k * PI / 6
                u = np.array([np.cos(a), np.sin(a), 0])
                g.add(Line(CLOCK_C + u * CLOCK_R * 0.86, CLOCK_C + u * CLOCK_R * 0.97,
                           stroke_width=4, color=WHITE))
            return g

        face = clock_face()
        sector = always_redraw(
            lambda: Sector(
                radius=CLOCK_R,
                angle=max(PI * t.get_value(), 1e-3),
                start_angle=PI / 2 - max(PI * t.get_value(), 1e-3),
                arc_center=CLOCK_C,
                fill_color=WHITE,
                fill_opacity=0.3,
                stroke_width=0,
            )
        )
        hand = always_redraw(
            lambda: Line(
                CLOCK_C,
                CLOCK_C + CLOCK_R * 0.9 * np.array(
                    [np.cos(PI / 2 - PI * t.get_value()), np.sin(PI / 2 - PI * t.get_value()), 0]
                ),
                stroke_width=6,
                color=WHITE,
            )
        )
        digital = always_redraw(
            lambda: Text(f"{int(round(30 * t.get_value())):02d}:00", font_size=64, color=WHITE)
            .move_to(DOWN * 6.5)
        )

        # --- Операнды ---
        row_a = make_row(str(A), 0, 0)
        row_b = make_row(str(B), 0, 1)
        times = Text("×", font_size=FS, color=WHITE).move_to(
            np.array([X_R - 9 * DX, Y0 - DY, 0])
        )
        line1 = h_line(2)

        self.play(
            *[FadeIn(d, shift=DOWN * 0.15) for d in row_a + row_b],
            FadeIn(times),
            Create(line1),
            FadeIn(face),
            FadeIn(sector),
            FadeIn(hand),
            FadeIn(digital),
            run_time=0.5,
        )

        # --- 8 частичных произведений ---
        partial_rows = []
        for i, ch in enumerate(reversed(str(B))):
            digits = make_row(str(A * int(ch)), i, 2 + i)
            partial_rows.append(digits)
            self.play(
                LaggedStart(
                    *[FadeIn(d, shift=LEFT * 0.12) for d in digits],
                    lag_ratio=0.1,
                ),
                t.animate.set_value((i + 1) / 8),
                run_time=0.275,
                rate_func=linear,
            )

        # --- Сумма ---
        line2 = h_line(10)
        total = make_row(str(A * B), 0, 10)
        self.play(
            Create(line2),
            LaggedStart(*[FadeIn(d, shift=UP * 0.12) for d in total], lag_ratio=0.04),
            run_time=0.5,
        )

        # --- Одна ошибка: одна цифра меняется, и всё ломается ---
        bad = partial_rows[3][2]
        wrong = Text(
            str((int(bad.text) + 3) % 10), font_size=FS, color=WHITE
        ).move_to(bad)
        box = SurroundingRectangle(bad, color=WHITE, buff=0.1, stroke_width=4)
        self.play(Transform(bad, wrong), Create(box), Flash(bad.get_center(), color=WHITE), run_time=0.3)

        scrambled = [
            Text(str(np.random.randint(0, 10)), font_size=FS, color=WHITE).move_to(d)
            for d in total
        ]
        self.play(
            LaggedStart(*[Transform(d, s) for d, s in zip(total, scrambled)], lag_ratio=0.03),
            run_time=0.3,
        )

        left = total[-1].get_center() + LEFT * 0.4
        right = total[0].get_center() + RIGHT * 0.4
        cross = VGroup(
            Line(left + UP * 0.8, right + DOWN * 0.8, stroke_width=8, color=WHITE),
            Line(left + DOWN * 0.8, right + UP * 0.8, stroke_width=8, color=WHITE),
        )
        self.play(Create(cross), run_time=0.2)

        # --- Итог: таких умножений тысячи ---
        everything = Group(*self.mobjects)
        self.play(FadeOut(everything), run_time=0.3)
        thousand = MathTex(r"\times 1000", color=WHITE).scale(3.5)
        self.play(Write(thousand), run_time=0.5)
        self.wait(0.2)