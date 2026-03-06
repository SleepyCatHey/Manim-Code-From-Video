from manim import *

class Part3ChoosingIDE(Scene):
    def construct(self):
        # Global settings
        BG_COLOR = "#1e1e2e"
        FONT = "JetBrainsMono Nerd Font"
        FONT_WEIGHT = BOLD
        
        self.camera.background_color = BG_COLOR
        
        # Topic + learning place boxes
        FONT_SIZE_BOX_TEXT = 28
        COLOR_TOPIC_BOX = "#89b4fa"
        COLOR_PLACE_BOX = "#a6e3a1"
        COLOR_BOX_TEXT = "#1e1e2e"
        TIME_BOXES_APPEAR = 1.0 
        
        topic_box = Rectangle(height=1.2, width=3.5, color=COLOR_TOPIC_BOX, fill_opacity=1)
        topic_box.move_to(LEFT * 2.5 + UP * 0.5)
        topic_text = Text("Data Science", font=FONT, font_size=FONT_SIZE_BOX_TEXT, color=COLOR_BOX_TEXT, weight=FONT_WEIGHT)
        topic_text.move_to(topic_box.get_center())
        topic_group = VGroup(topic_box, topic_text)
        
        place_box = Rectangle(height=1.2, width=3.5, color=COLOR_PLACE_BOX, fill_opacity=1)
        place_box.move_to(RIGHT * 2.5 + UP * 0.5)
        place_text = Text("FreeCodeCamp", font=FONT, font_size=FONT_SIZE_BOX_TEXT, color=COLOR_BOX_TEXT, weight=FONT_WEIGHT)
        place_text.move_to(place_box.get_center())
        place_group = VGroup(place_box, place_text)
        
        self.play(FadeIn(topic_group), FadeIn(place_group), run_time=TIME_BOXES_APPEAR)
        self.wait(0.5)
        
        # Transform to "where do you write code?"
        FONT_SIZE_WHERE = 36
        COLOR_WHERE_TEXT = "#cdd6f4"
        TIME_WHERE_TRANSFORM = 1.2
        
        where_text = Text("where do you actually write code?", font=FONT, font_size=FONT_SIZE_WHERE, color=COLOR_WHERE_TEXT, weight=FONT_WEIGHT)
        
        self.play(
            Transform(topic_group, where_text),
            FadeOut(place_group),
            run_time=TIME_WHERE_TRANSFORM
        )
        self.wait(0.5)
        
        # Tough emoji
        TIME_EMOJI_APPEAR = 1.0
        
        gigachad = Text("💪😎", font_size=120)
        
        self.play(Transform(topic_group, gigachad), run_time=TIME_EMOJI_APPEAR)
        self.wait(0.5)
        
        # Notepad icon
        COLOR_NOTEPAD_BG = "#cdd6f4"
        COLOR_NOTEPAD_LINES = "#1e1e2e"
        TIME_NOTEPAD_APPEAR = 1.0
        
        notepad_bg = RoundedRectangle(corner_radius=0.3, height=3, width=2.5, color=COLOR_NOTEPAD_BG, fill_opacity=1)
        notepad_lines = VGroup()
        for i in range(5):
            line = Line(LEFT * 0.8, RIGHT * 0.8, color=COLOR_NOTEPAD_LINES, stroke_width=3)
            line.move_to(notepad_bg.get_center() + UP * (1 - i * 0.5))
            notepad_lines.add(line)
        
        notepad = VGroup(notepad_bg, notepad_lines)
        
        self.play(Transform(topic_group, notepad), run_time=TIME_NOTEPAD_APPEAR)
        self.wait(0.5)
        
        # Fade out and type "IDE"
        FONT_SIZE_IDE = 72
        COLOR_IDE_TEXT = "#89b4fa"
        TIME_IDE_WRITE = 1.5
        
        self.play(FadeOut(topic_group), run_time=0.5)
        
        ide_text = Text("IDE", font=FONT, font_size=FONT_SIZE_IDE, color=COLOR_IDE_TEXT, weight=FONT_WEIGHT)
        
        self.play(Write(ide_text), run_time=TIME_IDE_WRITE)
        self.wait(0.5)
        
        # IDE window example
        COLOR_IDE_WINDOW = "#313244"
        COLOR_CODE_LINE = "#a6e3a1"
        COLOR_LINE_NUMBER = "#6c7086"
        TIME_IDE_EXAMPLE = 1.2
        
        ide_window = Rectangle(height=3.5, width=6, color=COLOR_IDE_WINDOW, fill_opacity=1, stroke_width=2, stroke_color="#89b4fa")
        
        title_bar = Rectangle(height=0.4, width=6, color="#45475a", fill_opacity=1)
        title_bar.move_to(ide_window.get_top() + DOWN * 0.2)
        
        line_numbers = VGroup()
        for i in range(1, 6):
            num = Text(str(i), font=FONT, font_size=16, color=COLOR_LINE_NUMBER, weight=FONT_WEIGHT)
            num.move_to(ide_window.get_left() + RIGHT * 0.5 + UP * (1.2 - i * 0.5))
            line_numbers.add(num)
        
        code_lines = VGroup()
        code_samples = ["def hello():", "    print('Hello')", "    return True", "", "hello()"]
        for i, code in enumerate(code_samples):
            line = Text(code, font=FONT, font_size=14, color=COLOR_CODE_LINE, weight=FONT_WEIGHT)
            line.move_to(ide_window.get_left() + RIGHT * 2.5 + UP * (1.2 - i * 0.5))
            code_lines.add(line)
        
        ide_example = VGroup(ide_window, title_bar, line_numbers, code_lines)
        
        self.play(Transform(ide_text, ide_example), run_time=TIME_IDE_EXAMPLE)
        self.wait(0.5)
        
        # Course recommendation
        FONT_SIZE_COURSE = 32
        COLOR_COURSE_TEXT = "#cdd6f4"
        TIME_COURSE_WRITE = 1.5
        
        self.play(FadeOut(ide_text), run_time=0.5)
        
        course_text = Text("Use whatever IDE your course recommends", font=FONT, font_size=FONT_SIZE_COURSE, color=COLOR_COURSE_TEXT, weight=FONT_WEIGHT)
        
        self.play(Write(course_text), run_time=TIME_COURSE_WRITE)
        self.wait(0.5)
        
        # VS Code logo
        TIME_VSCODE_APPEAR = 1.5
        
        self.play(FadeOut(course_text), run_time=0.5)
        
        main_shape = RoundedRectangle(
            corner_radius=0.2,
            height=3,
            width=3,
            color="#007ACC",
            fill_opacity=1,
            stroke_width=0
        )
        
        chevron = Polygon(
            [-0.5, 0.8, 0],
            [0.8, 0, 0],
            [-0.5, -0.8, 0],
            color="#FFFFFF",
            fill_opacity=1,
            stroke_width=0
        )
        
        vscode_text = Text("VS Code", font=FONT, font_size=28, color="#007ACC", weight=FONT_WEIGHT)
        vscode_text.next_to(main_shape, DOWN, buff=0.5)
        
        vscode_logo = VGroup(main_shape, chevron, vscode_text)
        
        self.play(
            FadeIn(vscode_logo, scale=0.8),
            run_time=TIME_VSCODE_APPEAR
        )
        self.wait(0.5)
        
        self.play(FadeOut(vscode_logo), run_time=0.8)
        
        # Advice
        FONT_SIZE_ADVICE = 36
        COLOR_ADVICE_TEXT = "#f9e2af"
        TIME_ADVICE_WRITE = 1.2
        
        advice_text = Text("But here's my advice", font=FONT, font_size=FONT_SIZE_ADVICE, color=COLOR_ADVICE_TEXT, weight=FONT_WEIGHT)
        
        self.play(Write(advice_text), run_time=TIME_ADVICE_WRITE)
        self.wait(0.5)
        
        self.play(advice_text.animate.shift(UP * 1.5), run_time=0.5)
        
        # AI warning
        FONT_SIZE_AI_WARNING = 32
        COLOR_AI_WARNING = "#f38ba8"
        TIME_AI_WARNING_WRITE = 1.5
        
        ai_warning = Text("don't rely on AI while learning the basics.", font=FONT, font_size=FONT_SIZE_AI_WARNING, color=COLOR_AI_WARNING, weight=FONT_WEIGHT)
        ai_warning.move_to(ORIGIN)
        
        self.play(Write(ai_warning), run_time=TIME_AI_WARNING_WRITE)
        self.wait(0.5)
        
        # Learn first
        FONT_SIZE_LEARN = 36
        COLOR_LEARN_TEXT = "#a6e3a1"
        TIME_LEARN_TRANSFORM = 1.0
        
        learn_text = Text("Learn the language first.", font=FONT, font_size=FONT_SIZE_LEARN, color=COLOR_LEARN_TEXT, weight=FONT_WEIGHT)
        
        self.play(
            Transform(ai_warning, learn_text),
            run_time=TIME_LEARN_TRANSFORM
        )
        self.wait(0.5)
        
        self.play(
            advice_text.animate.shift(UP * 0.8),
            ai_warning.animate.shift(UP * 1.5),
            run_time=0.5
        )
        
        # Understand your code
        FONT_SIZE_UNDERSTAND = 30
        COLOR_UNDERSTAND_TEXT = "#89b4fa"
        TIME_UNDERSTAND_WRITE = 1.5
        
        understand_text = Text("Understand what your code is doing.", font=FONT, font_size=FONT_SIZE_UNDERSTAND, color=COLOR_UNDERSTAND_TEXT, weight=FONT_WEIGHT)
        understand_text.move_to(ORIGIN)
        
        self.play(Write(understand_text), run_time=TIME_UNDERSTAND_WRITE)
        self.wait(0.5)
        
        # AI later
        FONT_SIZE_AI_LATER = 38
        COLOR_AI_LATER = "#cdd6f4"
        TIME_AI_LATER_TRANSFORM = 1.2
        
        ai_later_text = Text("We'll use AI later.", font=FONT, font_size=FONT_SIZE_AI_LATER, color=COLOR_AI_LATER, weight=FONT_WEIGHT)
        
        self.play(
            FadeOut(advice_text),
            FadeOut(ai_warning),
            Transform(understand_text, ai_later_text),
            run_time=TIME_AI_LATER_TRANSFORM
        )
        self.wait(2)