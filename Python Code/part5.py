from manim import *

class Part5Outro(Scene):
    def construct(self):
        # Global settings
        BG_COLOR = "#1e1e2e"
        FONT = "JetBrainsMono Nerd Font"
        FONT_WEIGHT = BOLD
        
        self.camera.background_color = BG_COLOR
        
        # Every developer goes through that phase
        FONT_SIZE_PHASE = 32
        COLOR_PHASE_TEXT = "#a6e3a1"
        TIME_PHASE_WRITE = 1.5
        
        phase_text = Text(
            "every developer goes through that phase.",
            font=FONT,
            font_size=FONT_SIZE_PHASE,
            color=COLOR_PHASE_TEXT,
            weight=FONT_WEIGHT
        )
        
        self.play(Write(phase_text), run_time=TIME_PHASE_WRITE)
        self.wait(0.5)
        
        self.play(phase_text.animate.shift(UP * 1.5), run_time=0.5)
        
        # You're not alone
        FONT_SIZE_ALONE = 36
        COLOR_ALONE_TEXT = "#89b4fa"
        TIME_ALONE_WRITE = 1.5
        
        alone_text = Text(
            "You're not alone",
            font=FONT,
            font_size=FONT_SIZE_ALONE,
            color=COLOR_ALONE_TEXT,
            weight=FONT_WEIGHT
        )
        alone_text.move_to(ORIGIN)
        
        self.play(Write(alone_text), run_time=TIME_ALONE_WRITE)
        self.wait(0.5)
        
        # And as always
        FONT_SIZE_ALWAYS = 36
        COLOR_ALWAYS_TEXT = "#f9e2af"
        TIME_ALWAYS_TRANSFORM = 1.0
        
        always_text = Text(
            "And as always",
            font=FONT,
            font_size=FONT_SIZE_ALWAYS,
            color=COLOR_ALWAYS_TEXT,
            weight=FONT_WEIGHT
        )
        
        self.play(
            FadeOut(phase_text),
            Transform(alone_text, always_text),
            run_time=TIME_ALWAYS_TRANSFORM
        )
        self.wait(0.5)
        
        # Take care
        FONT_SIZE_CARE = 48
        COLOR_CARE_TEXT = "#cba6f7"
        TIME_CARE_TRANSFORM = 1.2
        
        care_text = Text(
            "take care of yourself",
            font=FONT,
            font_size=FONT_SIZE_CARE,
            color=COLOR_CARE_TEXT,
            weight=FONT_WEIGHT
        )
        
        self.play(
            Transform(alone_text, care_text),
            run_time=TIME_CARE_TRANSFORM
        )
        self.wait(2)