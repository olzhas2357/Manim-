from manim import *

# Вертикальное видео 9:16 для Reels
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = BLACK


class LogTrick(Scene):
    def construct(self):
        # --- 0:00-0:02  Вопрос ---
        title = MathTex(r"8 \times 16 = ?", color=WHITE).scale(2)
        self.play(Write(title), run_time=1)
        self.wait(0.5)
        self.play(title.animate.move_to(UP * 6.5), run_time=0.5)

        # --- 0:02-0:04.5  Таблица степеней двойки ---
        rows = VGroup(
            *[MathTex(f"2^{{{i}}} = {2 ** i}", color=WHITE) for i in range(1, 8)]
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        rows.scale(1.1).move_to(DOWN * 2.6)
        self.play(FadeIn(rows, shift=UP * 0.3), run_time=1)
        self.wait(1.5)

        # --- 0:04.5-0:06.5  8 = 2^3 ---
        box8 = SurroundingRectangle(rows[2], color=WHITE, buff=0.12)
        eq8 = MathTex(r"8 = 2^3", color=WHITE).scale(1.6).move_to(UP * 4.6)
        self.play(Create(box8), Write(eq8), run_time=1)
        self.wait(1)

        # --- 0:06.5-0:08.5  16 = 2^4 ---
        box16 = SurroundingRectangle(rows[3], color=WHITE, buff=0.12)
        eq16 = MathTex(r"16 = 2^4", color=WHITE).scale(1.6).move_to(UP * 3.2)
        self.play(Create(box16), Write(eq16), run_time=1)
        self.wait(1)

        # --- 0:08.5-0:11  3 + 4 = 7 ---
        plus = MathTex(r"3 + 4 = 7", color=WHITE).scale(2.2).move_to(UP * 1.4)
        self.play(Write(plus), run_time=1.5)
        self.wait(1)

        # --- 0:11-0:13.5  2^7 = 128 в таблице ---
        box128 = SurroundingRectangle(rows[6], color=WHITE, buff=0.12)
        self.play(Create(box128), run_time=1)
        self.wait(1.5)

        # --- 0:13.5-0:16  Результат ---
        result = MathTex(r"8 \times 16 = 128", color=WHITE).scale(2).move_to(UP * 1.4)
        self.play(ReplacementTransform(plus, result), run_time=1.5)
        self.wait(1)

        # --- 0:16-0:20  Финальная фраза ---
        self.play(
            FadeOut(VGroup(title, rows, box8, box16, box128, eq8, eq16, result)),
            run_time=1,
        )
        final = Text(
            "Мы не умножали,\nмы только сложили.",
            color=WHITE,
            font_size=56,
            line_spacing=1.2,
        )
        self.play(Write(final), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(final), run_time=1)