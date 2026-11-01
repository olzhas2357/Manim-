from manim import *

# Вертикальное видео 9:16 для Reels
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = BLACK

W, H = 5.5, 7.0              # размер книги
BOOK_Y = 1.5                 # высота центра книги на экране
N0 = 10**9                   # миллиард записей


def page_lines(height, count, center_y):
    """Горизонтальные строчки на страницах."""
    step = height / (count + 1)
    return VGroup(
        *[
            Line(
                LEFT * (W / 2 - 0.3) + UP * (center_y - height / 2 + step * i),
                RIGHT * (W / 2 - 0.3) + UP * (center_y - height / 2 + step * i),
                stroke_width=2,
                stroke_opacity=0.35,
                color=WHITE,
            )
            for i in range(1, count + 1)
        ]
    )


def target_line(y):
    """Ярко выделенная строка: имя, которое мы ищем."""
    return Line(
        LEFT * (W / 2 - 0.2) + UP * y,
        RIGHT * (W / 2 - 0.2) + UP * y,
        stroke_width=9,
        color=WHITE,
    )


def make_book(f):
    """Полная книга; f (0..1) - положение искомой строки снизу вверх."""
    rect = Rectangle(width=W, height=H, stroke_color=WHITE, stroke_width=4)
    rect.move_to(UP * BOOK_Y)
    lines = page_lines(H, 20, BOOK_Y)
    target = target_line(BOOK_Y - H / 2 + H * f)
    return VGroup(rect, lines, target)


def make_half(top, rel=None):
    """Половина книги; rel - положение искомой строки внутри неё."""
    cy = BOOK_Y + (H / 4 if top else -H / 4)
    rect = Rectangle(width=W, height=H / 2, stroke_color=WHITE, stroke_width=4)
    rect.move_to(UP * cy)
    parts = [rect, page_lines(H / 2, 10, cy)]
    if rel is not None:
        parts.append(target_line(cy - H / 4 + (H / 2) * rel))
    return VGroup(*parts)


def make_tear():
    """Рваная линия разрыва по середине книги."""
    xs = np.linspace(-W / 2, W / 2, 12)
    pts = [np.array([x, BOOK_Y + np.random.uniform(-0.22, 0.22), 0]) for x in xs]
    tear = VMobject(stroke_color=WHITE, stroke_width=6)
    tear.set_points_as_corners(pts)
    return tear


class BookSplit(Scene):
    def construct(self):
        np.random.seed(7)
        n = ValueTracker(0)
        f = 0.6180339  # где спрятано искомое имя

        remaining = always_redraw(
            lambda: Integer(max(1, int(N0 / 2 ** n.get_value())), color=WHITE)
            .scale(1.5)
            .move_to(UP * 6.4)
        )
        counter = always_redraw(
            lambda: Integer(int(round(n.get_value())), color=WHITE)
            .scale(3.2)
            .move_to(DOWN * 5.6)
        )

        book = make_book(f)

        # --- 0:00-0:01  Появление ---
        self.play(FadeIn(book), FadeIn(remaining), FadeIn(counter), run_time=1)

        # --- 0:01-0:06.5  30 разрывов, всё быстрее и быстрее ---
        for k in range(1, 31):
            top_has = f >= 0.5
            f_new = 2 * f - 1 if top_has else 2 * f

            top = make_half(True, f_new if top_has else None)
            bottom = make_half(False, None if top_has else f_new)
            tear = make_tear()

            self.remove(book)
            self.add(top, bottom, tear)

            kept, gone = (top, bottom) if top_has else (bottom, top)
            vertical = DOWN if top_has else UP
            side = RIGHT if k % 2 else LEFT
            angle = -0.6 if k % 2 else 0.6

            new_book = make_book(f_new)
            rt = max(0.07, 0.8 * 0.8 ** (k - 1))

            self.play(
                gone.animate.shift(vertical * 9 + side * 3).rotate(angle).set_opacity(0),
                FadeOut(tear),
                ReplacementTransform(kept, new_book),
                n.animate.set_value(k),
                run_time=rt,
                rate_func=linear,
            )
            self.remove(gone)
            book = new_book
            f = f_new

        self.wait(0.4)

        # --- 0:06.5-0:07.2  Нашли ---
        self.play(Flash(book[2].get_center(), color=WHITE, flash_radius=1.0), run_time=0.7)

        # --- 0:07.2-0:10  Итог ---
        remaining.clear_updaters()
        counter.clear_updaters()
        final30 = Integer(30, color=WHITE).scale(3.2).move_to(DOWN * 5.6)
        self.remove(counter)
        self.add(final30)

        self.play(FadeOut(VGroup(remaining, book)), run_time=0.5)
        self.play(final30.animate.scale(0.6).move_to(UP * 1.2), run_time=0.6)
        formula = MathTex(r"\log_2 10^9 \approx 30", color=WHITE).scale(1.8)
        formula.move_to(DOWN * 1.5)
        self.play(Write(formula), run_time=0.9)
        self.wait(0.5)