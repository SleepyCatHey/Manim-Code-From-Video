from manim import *

class BootcampDemo(Scene):
    def construct(self):
        # Global settings
        BG_COLOR = "#1e1e2e"
        FONT = "JetBrainsMono Nerd Font"
        FONT_WEIGHT = BOLD
        
        self.camera.background_color = BG_COLOR
        
        # Colors
        COLOR_YOU = "#89b4fa"
        COLOR_LESSON_BOX = "#a6e3a1"
        COLOR_CERTIFICATE = "#f9e2af"
        COLOR_TEXT = "#cdd6f4"
        COLOR_ARROW = "#cdd6f4"
        TIME_TOTAL = 3.0
        
        # Bootcamp demo
        
        you_circle = Circle(radius=0.3, color=COLOR_YOU, fill_opacity=1)
        you_circle.move_to(LEFT * 5)
        you_text = Text("You", font=FONT, font_size=20, color=COLOR_TEXT, weight=FONT_WEIGHT)
        you_text.next_to(you_circle, UP, buff=0.2)
        
        lesson_boxes = VGroup()
        for i in range(3):
            box = Rectangle(height=0.8, width=1.2, color=COLOR_LESSON_BOX, fill_opacity=0.8, stroke_width=2)
            box.move_to(LEFT * 2 + RIGHT * i * 1.8)
            lesson_num = Text(f"{i+1}", font=FONT, font_size=24, color=BG_COLOR, weight=FONT_WEIGHT)
            lesson_num.move_to(box.get_center())
            lesson_boxes.add(VGroup(box, lesson_num))
        
        cert_rect = Rectangle(height=1.5, width=1.2, color=COLOR_CERTIFICATE, fill_opacity=0.9, stroke_width=3)
        cert_rect.move_to(RIGHT * 5)
        cert_seal = Circle(radius=0.15, color=COLOR_YOU, fill_opacity=1)
        cert_seal.move_to(cert_rect.get_center() + DOWN * 0.4 + RIGHT * 0.3)
        cert_lines = VGroup()
        for i in range(2):
            line = Line(LEFT * 0.4, RIGHT * 0.4, color=BG_COLOR, stroke_width=2)
            line.move_to(cert_rect.get_center() + UP * (0.2 - i * 0.3))
            cert_lines.add(line)
        certificate = VGroup(cert_rect, cert_seal, cert_lines)

        start_arrow = Arrow(
            you_circle.get_right() + RIGHT * 0.1,
            lesson_boxes[0].get_left() + LEFT * 0.1,
            color=COLOR_ARROW,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3
        )
        
        arrow_1_to_2 = Arrow(
            lesson_boxes[0].get_right() + RIGHT * 0.1,
            lesson_boxes[1].get_left() + LEFT * 0.1,
            color=COLOR_ARROW,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3
        )
        
        arrow_2_to_3 = Arrow(
            lesson_boxes[1].get_right() + RIGHT * 0.1,
            lesson_boxes[2].get_left() + LEFT * 0.1,
            color=COLOR_ARROW,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3
        )
        
        end_arrow = Arrow(
            lesson_boxes[2].get_right() + RIGHT * 0.1,
            certificate.get_left() + LEFT * 0.1,
            color=COLOR_ARROW,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3
        )
       
        bootcamp_label = Text("Coding Bootcamp", font=FONT, font_size=32, color=COLOR_TEXT, weight=FONT_WEIGHT)
        bootcamp_label.to_edge(UP, buff=0.5)
        

        self.play(
            FadeIn(you_circle),
            FadeIn(you_text),
            FadeIn(bootcamp_label),
            run_time=0.3 
        )
        
        self.play(
            FadeIn(lesson_boxes),
            FadeIn(certificate),
            run_time=0.4  
        )
              
        self.play(
            Create(start_arrow),
            run_time=0.3  
        )
        
        self.play(
            Create(arrow_1_to_2),
            run_time=0.3  
        )
        
        self.play(
            Create(arrow_2_to_3),
            run_time=0.3  
        )
        
        self.play(
            Create(end_arrow),
            run_time=0.3
        )
        self.play(
            certificate.animate.scale(1.2),
            run_time=0.25  
        )
        self.play(
            certificate.animate.scale(1/1.2),
            run_time=0.25  
        )
        

        self.wait(0.5)  
