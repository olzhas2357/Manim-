from manim import *

# Настройка вертикального разрешения 9:16 (Shorts / Reels / TikTok)
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0

class SqrtTwoAnimation(Scene):
    def construct(self):
        # 1. Заголовок
        title = Text("Магия числа √2", font_size=42, color=BLUE_A).to_edge(UP, buff=1.0)
        self.play(Write(title), run_time=1.2)

        # 2. Демонстрация геометрии: квадрат и диагональ
        square = Square(side_length=3.0, color=BLUE, stroke_width=4).shift(UP * 3.5)
        
        # Подписи сторон квадрата
        s_top = MathTex("1", font_size=32).next_to(square, UP, buff=0.1)
        s_left = MathTex("1", font_size=32).next_to(square, LEFT, buff=0.1)
        
        # Диагональ
        diagonal = Line(square.get_corner(DL), square.get_corner(UR), color=YELLOW, stroke_width=6)
        d_label = MathTex(r"\sqrt{2} \approx ?", font_size=36, color=YELLOW).move_to(diagonal.get_center() + LEFT * 0.8 + UP * 0.4)

        self.play(Create(square), Write(s_top), Write(s_left), run_time=1.5)
        self.play(Create(diagonal), Write(d_label), run_time=1.5)
        self.wait(0.5)

        # Переход к точному значению
        eq_transform = MathTex(r"\sqrt{2} =", font_size=44, color=WHITE).shift(UP * 0.8)
        self.play(Transform(d_label, eq_transform), run_time=1.0)
        self.play(square.animate.scale(0.7).to_edge(UP, buff=0.5), FadeOut(s_top), FadeOut(s_left), FadeOut(diagonal), run_time=1)

        # 3. Вывод длинной последовательности цифр (разбитой на строки для читаемости)
        # Целая часть и первые знаки
        part1 = Text("1,", font_size=38, color=GREEN_A)
        
        # Переданная вами длинная строка цифр, разбитая на блоки по 10 знаков для красоты
        digits_str = (
            "4142135623 7309504880 1688724209 6980785696 "
            "7187537694 8073176679 7379907324 7846210703 "
            "8850387534 3276415727 3501384623 0912297024 "
            "9248360558 5073721264 4121497099 9358314132 "
            "2266592750 5592755799 9505011527 8206057147 "
            "0109559971 6059702745 3459686201 4728517418 "
            "6408891986 0955232923 0484308714 3214508397 "
            "6260362799 5251407989 6872533965 4633180882 "
            "9640620615 2583523950 5474575028 7759961729 "
            "8355752203 3753185701 1354374603 4084988471 "
            "6038689997 0699004815 0305440277 9031645424 "
            "7823068492 9369186215 8057846311 1596668713 "
            "0130156185 6898723723 5288509264 8612494977 "
            "1542183342 0428568606 0146824720 7714358548 "
            "7415565706 9677653720 2264854470 1585880162 "
            "0758474922 6572260020 8558446652 1458398893 "
            "9443709265 9180031138 8246468157 0826301005 "
            "9485870400 3186480342 1948972782 9064104507"
        )

        # Создаем текстовый блок с настраиваемым переносом строк для узкого экрана 9:16
        digits_text = Paragraph(
            digits_str, 
            font_size=20, 
            color=LIGHT_GRAY, 
            line_spacing=1.2,
            alignment="center"
        ).scale(0.85).shift(DOWN * 1.5)

        # Эффект плавного появления цифр потоком
        self.play(FadeIn(part1.next_to(eq_transform, RIGHT)), run_time=0.5)
        self.play(Write(digits_text), run_time=5.0)

        # 4. Финальный акцент: бесконечность
        infinity_sign = MathTex(r"\dots \infty", font_size=36, color=ORANGE).next_to(digits_text, DOWN, buff=0.4)
        inf_text = Text("И этот ряд никогда не заканчивается!", font_size=24, color=YELLOW).next_to(infinity_sign, DOWN, buff=0.3)
        
        self.play(FadeIn(infinity_sign, shift=UP), FadeIn(inf_text, shift=UP), run_time=1.5)

        self.wait(3)