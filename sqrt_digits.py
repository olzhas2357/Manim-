from manim import *

config.frame_width = 9.0
config.frame_height = 16.0
config.background_color = "#0B1B4D"

SQRT2 = (
    "1.4142135623 7309504880 1688724209 6980785696 7187537694 "
    "8073176679 7379907324 7846210703 8850387534 3276415727 "
    "3501384623 0912297024 9248360558 5073721264 4121497099 "
    "9358314132 2266592750 5592755799 9505011527 8206057147 "
    "0109559971 6059702745 3459686201 4728517418 6408891986 "
    "0955232923 0484308714 3214508397 6260362799 5251407989 "
    "6872533965 4633180882 9640620615 2583523950 5474575028 "
    "7759961729 8355752203 3753185701 1354374603 4084988471 "
    "6038689997 0699004815 0305440277 9031645424 7823068492 "
    "9369186215 8057846311 1596668713 0130156185 6898723723 "
    "5288509264 8612494977 1542183342 0428568606 0146824720 "
    "7714358548 7415565706 9677653720 2264854470 1585880162 "
    "0758474922 6572260020 8558446652 1458398893 9443709265 "
    "9180031138 8246468157 0826301005 9485870400 3186480342 "
    "1948972782 9064104507"
)
DIGITS = SQRT2.replace(" ", "")


class Sqrt2Digits(Scene):
    def construct(self):

        # --- 1. Хук: √2 = ? ---
        question = MathTex(r"\sqrt{2} = \ ?", color=YELLOW).scale(3.5)
        self.play(Write(question), run_time=1.2)
        self.wait(0.6)
        self.play(FadeOut(question))

        # --- 2. Квадрат және диагональ ---
        sq = Square(side_length=4.0, color=WHITE, stroke_width=6).shift(UP * 2.5)
        lab1 = MathTex("1").scale(1.2).next_to(sq, DOWN, buff=0.2)
        lab2 = MathTex("1").scale(1.2).next_to(sq, LEFT, buff=0.2)
        diag = Line(sq.get_corner(DL), sq.get_corner(UR),
                    color=YELLOW, stroke_width=8)
        d_label = MathTex(r"d = \sqrt{2}", color=YELLOW).scale(1.4).shift(DOWN * 1.0)

        self.play(Create(sq), run_time=1.0)
        self.play(Write(lab1), Write(lab2))
        self.play(Create(diag), run_time=0.8)
        self.play(Write(d_label))
        self.wait(0.8)
        self.play(FadeOut(VGroup(sq, lab1, lab2, diag, d_label)))

        # --- 3. Бірінші цифрлар ірі шрифтпен ---
        first = MathTex(r"1.4142135623\ldots", color=YELLOW).scale(2.0)
        self.play(Write(first), run_time=1.5)
        self.wait(0.8)
        self.play(FadeOut(first))

        # --- 4. Цифрлар ағыны жоғарыдан төмен ---
        chunk = 10
        rows = [DIGITS[i:i+chunk] for i in range(0, len(DIGITS), chunk)]

        # Экранға сыятын қатарлар саны
        row_h = 0.62
        visible = int(config.frame_height / row_h) + 2  # биіктікке сыятын

        label = Text("√2-нің алғашқы 500 цифры",
                     font_size=28, color=BLUE_A).move_to(UP * 7.0)
        self.play(FadeIn(label))

        # Бүкіл цифр блогын бір VGroup ретінде жасаймыз
        all_rows = VGroup()
        for i, r in enumerate(rows):
            # Бірінші '1.' бар жолды ерекшелейміз
            if i == 0:
                t = Text(r, font_size=34, color=YELLOW)
            else:
                # Кезекпен: ақ / ашық көк
                col = WHITE if i % 2 == 0 else BLUE_B
                t = Text(r, font_size=34, color=col)
            all_rows.add(t)

        all_rows.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        all_rows.move_to(ORIGIN)

        # Блок биіктігі
        total_h = all_rows.height

        # Жоғарыдан бастап, төменге ағады
        start_y = config.frame_height / 2 + all_rows.height / 2
        end_y   = -(config.frame_height / 2 + all_rows.height / 2)
        all_rows.move_to(UP * start_y)

        scroll_time = len(rows) * 0.55  # жылдамдық

        self.play(
            all_rows.animate.move_to(DOWN * (total_h / 2 + 1.5)),
            run_time=scroll_time,
            rate_func=linear,
        )

        # --- 5. Финал: сан аяқталмайды ---
        dots = MathTex(r"\ldots", color=YELLOW).scale(4)
        self.play(FadeIn(dots))
        self.wait(0.5)

        msg1 = Text("Бұл сан", font_size=40, color=WHITE).shift(UP * 1.2)
        msg2 = Text("ешқашан аяқталмайды",
                    font_size=40, color=YELLOW).shift(UP * 0.2)
        msg3 = Text("және қайталанбайды",
                    font_size=36, color=BLUE_A).shift(DOWN * 0.8)
        self.play(FadeOut(dots))
        self.play(Write(msg1), run_time=0.8)
        self.play(Write(msg2), run_time=0.8)
        self.play(Write(msg3), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(VGroup(msg1, msg2, msg3, label)))

        # --- 6. Финалдық кадр ---
        final = MathTex(r"\sqrt{2} \notin \mathbb{Q}", color=YELLOW).scale(3.0)
        sub = Text("Иррационал сан", font_size=38, color=WHITE).shift(DOWN * 2.0)
        self.play(Write(final), run_time=1.2)
        self.play(FadeIn(sub, shift=UP * 0.3))
        self.wait(2.5)