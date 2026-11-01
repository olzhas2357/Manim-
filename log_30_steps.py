from manim import *

# Вертикальное видео 9:16 для Reels
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = BLACK


class ThirtySteps(Scene):
    def construct(self):
        N0 = 10**9
        n = ValueTracker(0)  # номер шага: 0 -> 30

        # --- Сколько записей осталось (цифры сверху) ---
        remaining = always_redraw(
            lambda: Integer(
                max(1, int(N0 / 2 ** n.get_value())), color=WHITE
            ).scale(1.5).move_to(UP * 6.2)
        )

        # --- Полоса данных: каждый шаг режет её пополам ---
        bar_w = 7.0
        left_x = -bar_w / 2
        frame_bar = Rectangle(
            width=bar_w, height=0.7, stroke_color=WHITE, stroke_width=3
        ).move_to(UP * 4.3)

        def make_bar():
            w = max(bar_w * 2 ** (-n.get_value()), 0.04)
            return Rectangle(
                width=w, height=0.7, fill_color=WHITE, fill_opacity=1, stroke_width=0
            ).move_to(np.array([left_x + w / 2, 4.3, 0]))

        bar = always_redraw(make_bar)

        # --- График: сколько записей остаётся после каждого шага ---
        ax = Axes(
            x_range=[0, 30, 10],
            y_range=[0, 1, 0.5],
            x_length=7.0,
            y_length=4.6,
            axis_config={"color": WHITE, "stroke_width": 3},
            x_axis_config={"include_numbers": True, "font_size": 32},
            tips=False,
        ).move_to(DOWN * 0.6)
        curve = ax.plot(
            lambda x: 2 ** (-x), x_range=[0, 30], color=WHITE, stroke_width=6
        )

        dot = always_redraw(
            lambda: Dot(
                ax.c2p(n.get_value(), 2 ** (-n.get_value())),
                radius=0.14,
                color=WHITE,
            )
        )
        guide = always_redraw(
            lambda: DashedLine(
                ax.c2p(n.get_value(), 2 ** (-n.get_value())),
                ax.c2p(n.get_value(), 0),
                color=WHITE,
                stroke_width=2,
                dash_length=0.1,
            )
        )

        # --- Счётчик шагов (большие цифры внизу) ---
        counter = always_redraw(
            lambda: Integer(int(round(n.get_value())), color=WHITE)
            .scale(3.2)
            .move_to(DOWN * 5.6)
        )

        # --- 0:00-0:01.8  Появление ---
        self.play(
            FadeIn(frame_bar),
            FadeIn(bar),
            FadeIn(remaining),
            Create(ax),
            run_time=1,
        )
        self.play(Create(curve), run_time=0.8)
        self.add(dot, guide, counter)

        # --- 0:01.8-0:07.3  30 шагов ---
        self.play(n.animate.set_value(30), run_time=5.5, rate_func=smooth)
        self.wait(0.2)

        # --- 0:07.5-0:10  Итог ---
        for m in (remaining, bar, dot, guide, counter):
            m.clear_updaters()
        final30 = Integer(30, color=WHITE).scale(3.2).move_to(DOWN * 5.6)
        self.remove(counter)
        self.add(final30)

        self.play(
            FadeOut(VGroup(remaining, frame_bar, bar, ax, curve, dot, guide)),
            run_time=0.6,
        )
        self.play(final30.animate.scale(0.6).move_to(UP * 1.2), run_time=0.6)
        formula = MathTex(r"\log_2 10^9 \approx 30", color=WHITE).scale(1.8)
        formula.move_to(DOWN * 1.5)
        self.play(Write(formula), run_time=0.9)
        self.wait(0.4)