from manim import *

class Part4UsingAI(Scene):
    def construct(self):
        # Global settings
        BG_COLOR = "#1e1e2e"
        FONT = "JetBrainsMono Nerd Font"
        FONT_WEIGHT = BOLD
        
        self.camera.background_color = BG_COLOR
        
        # Language learned + small projects
        FONT_SIZE_LEARNED = 32
        COLOR_LEARNED_TEXT = "#a6e3a1"
        TIME_LEARNED_WRITE = 1.5
        
        learned_line1 = Text("✓ Language learned", font=FONT, font_size=FONT_SIZE_LEARNED, color=COLOR_LEARNED_TEXT, weight=FONT_WEIGHT)
        learned_line1.move_to(UP * 0.5)
        
        learned_line2 = Text("✓ Small projects built", font=FONT, font_size=FONT_SIZE_LEARNED, color=COLOR_LEARNED_TEXT, weight=FONT_WEIGHT)
        learned_line2.move_to(DOWN * 0.5)
        
        learned_group = VGroup(learned_line1, learned_line2)
        
        self.play(Write(learned_group), run_time=TIME_LEARNED_WRITE)
        self.wait(0.5)
        
        # AI with power
        TIME_AI_APPEAR = 1.2
        COLOR_AI_BRAIN = "#89b4fa"
        COLOR_POWER = "#f9e2af"
        
        ai_circle = Circle(radius=1, color=COLOR_AI_BRAIN, fill_opacity=0.3, stroke_width=3)
        
        # Neural network nodes
        nodes = VGroup()
        for i in range(8):
            angle = i * TAU / 8
            node = Dot(
                point=ai_circle.get_center() + np.array([np.cos(angle) * 0.7, np.sin(angle) * 0.7, 0]),
                color=COLOR_AI_BRAIN,
                radius=0.08
            )
            nodes.add(node)
        
        # Connections between nodes
        connections = VGroup()
        for i in range(8):
            for j in range(i + 1, 8):
                if (j - i) <= 3:
                    line = Line(nodes[i].get_center(), nodes[j].get_center(), color=COLOR_AI_BRAIN, stroke_width=1, stroke_opacity=0.3)
                    connections.add(line)
        
        ai_label = Text("AI", font=FONT, font_size=36, color=COLOR_AI_BRAIN, weight=FONT_WEIGHT)
        ai_label.move_to(ai_circle.get_center())
        
        ai_brain = VGroup(ai_circle, connections, nodes, ai_label)
        
        power_bolt = Polygon(
            [0.2, 0.6, 0],
            [0, 0.1, 0],
            [0.3, 0.1, 0],
            [0.1, -0.6, 0],
            [0.3, 0, 0],
            [0, 0, 0],
            color=COLOR_POWER,
            fill_opacity=1,
            stroke_width=0
        )
        power_bolt.next_to(ai_brain, RIGHT, buff=0.5)
        
        ai_power = VGroup(ai_brain, power_bolt)
        
        self.play(Transform(learned_group, ai_power), run_time=TIME_AI_APPEAR)
        self.wait(0.5)
        
        # Speedometer
        TIME_SPEEDOMETER_APPEAR = 1.2
        COLOR_SPEEDOMETER = "#cdd6f4"
        COLOR_NEEDLE_SLOW = "#a6e3a1"
        COLOR_NEEDLE_FAST = "#f38ba8"
        
        speedometer_arc = Arc(
            radius=1.5,
            start_angle=-PI * 0.75,
            angle=PI * 1.5,
            color=COLOR_SPEEDOMETER,
            stroke_width=8
        )
        
        marks = VGroup()
        for i in range(11):
            angle = -PI * 0.75 + (PI * 1.5) * (i / 10)
            start = np.array([np.cos(angle) * 1.3, np.sin(angle) * 1.3, 0])
            end = np.array([np.cos(angle) * 1.5, np.sin(angle) * 1.5, 0])
            mark = Line(start, end, color=COLOR_SPEEDOMETER, stroke_width=3)
            marks.add(mark)
        
        needle_angle = -PI * 0.75 + (PI * 1.5) * 0.85
        needle = Line(
            ORIGIN,
            np.array([np.cos(needle_angle) * 1.2, np.sin(needle_angle) * 1.2, 0]),
            color=COLOR_NEEDLE_FAST,
            stroke_width=4
        )
        needle_dot = Dot(ORIGIN, color=COLOR_NEEDLE_FAST, radius=0.1)
        
        workflow_label = Text("Workflow", font=FONT, font_size=24, color=COLOR_SPEEDOMETER, weight=FONT_WEIGHT)
        workflow_label.next_to(speedometer_arc, DOWN, buff=0.3)
        
        speedometer = VGroup(speedometer_arc, marks, needle, needle_dot, workflow_label)
        
        self.play(Transform(learned_group, speedometer), run_time=TIME_SPEEDOMETER_APPEAR)
        self.wait(0.5)
        
        # Don't ask it to do everything
        FONT_SIZE_DONT = 36
        COLOR_DONT_TEXT = "#f38ba8"
        TIME_DONT_APPEAR = 1.0
        
        dont_text = Text("Don't ask it to do everything", font=FONT, font_size=FONT_SIZE_DONT, color=COLOR_DONT_TEXT, weight=FONT_WEIGHT)
        
        self.play(Transform(learned_group, dont_text), run_time=TIME_DONT_APPEAR)
        self.wait(0.5)
        
        self.play(learned_group.animate.shift(UP * 1.5), run_time=0.5)
        
        # Decide what to build
        FONT_SIZE_DECIDE = 32
        COLOR_DECIDE_TEXT = "#a6e3a1"
        TIME_DECIDE_WRITE = 1.5
        
        decide_text = Text("First, decide what you want to build.", font=FONT, font_size=FONT_SIZE_DECIDE, color=COLOR_DECIDE_TEXT, weight=FONT_WEIGHT)
        decide_text.move_to(ORIGIN)
        
        self.play(Write(decide_text), run_time=TIME_DECIDE_WRITE)
        self.wait(0.5)
        
        # App structure
        TIME_STRUCTURE_APPEAR = 1.2
        COLOR_STRUCTURE = "#89b4fa"
        
        header = Rectangle(height=0.5, width=4, color=COLOR_STRUCTURE, fill_opacity=0.5)
        header.move_to(UP * 1.5)
        header_text = Text("Header", font=FONT, font_size=16, color="#cdd6f4", weight=FONT_WEIGHT)
        header_text.move_to(header.get_center())
        
        content_left = Rectangle(height=2, width=1.5, color=COLOR_STRUCTURE, fill_opacity=0.3)
        content_left.move_to(LEFT * 1 + DOWN * 0.2)
        
        content_right = Rectangle(height=2, width=2, color=COLOR_STRUCTURE, fill_opacity=0.3)
        content_right.move_to(RIGHT * 0.75 + DOWN * 0.2)
        
        footer = Rectangle(height=0.4, width=4, color=COLOR_STRUCTURE, fill_opacity=0.5)
        footer.move_to(DOWN * 1.5)
        footer_text = Text("Footer", font=FONT, font_size=16, color="#cdd6f4", weight=FONT_WEIGHT)
        footer_text.move_to(footer.get_center())
        
        structure = VGroup(header, header_text, content_left, content_right, footer, footer_text)
        
        self.play(
            FadeOut(learned_group),
            Transform(decide_text, structure),
            run_time=TIME_STRUCTURE_APPEAR
        )
        self.wait(0.5)
        
        # Control panel
        TIME_CONTROL_APPEAR = 1.0
        COLOR_CONTROL = "#f9e2af"
        
        control_panel = Rectangle(height=2.5, width=3, color=COLOR_CONTROL, fill_opacity=0.2, stroke_width=3)
        
        # Buttons/sliders
        button1 = Circle(radius=0.3, color=COLOR_CONTROL, fill_opacity=0.8)
        button1.move_to(control_panel.get_center() + UP * 0.6 + LEFT * 0.8)
        
        button2 = Circle(radius=0.3, color=COLOR_CONTROL, fill_opacity=0.8)
        button2.move_to(control_panel.get_center() + UP * 0.6 + RIGHT * 0.8)
        
        slider = Rectangle(height=0.15, width=1.5, color=COLOR_CONTROL, fill_opacity=0.5)
        slider.move_to(control_panel.get_center() + DOWN * 0.3)
        
        slider_handle = Rectangle(height=0.3, width=0.2, color=COLOR_CONTROL, fill_opacity=1)
        slider_handle.move_to(slider.get_center() + RIGHT * 0.4)
        
        control_label = Text("You Control", font=FONT, font_size=24, color=COLOR_CONTROL, weight=FONT_WEIGHT)
        control_label.next_to(control_panel, DOWN, buff=0.3)
        
        control_system = VGroup(control_panel, button1, button2, slider, slider_handle, control_label)
        
        self.play(Transform(decide_text, control_system), run_time=TIME_CONTROL_APPEAR)
        self.wait(0.5)
        
        # AI companion
        FONT_SIZE_COMPANION = 30
        COLOR_COMPANION_TEXT = "#cdd6f4"
        COLOR_NOT_REPLACEMENT = "#f38ba8"
        TIME_COMPANION_APPEAR = 1.2
        
        companion_part1 = Text("Use AI as a companion, ", font=FONT, font_size=FONT_SIZE_COMPANION, color=COLOR_COMPANION_TEXT, weight=FONT_WEIGHT)
        companion_part2 = Text("not a replacement.", font=FONT, font_size=FONT_SIZE_COMPANION, color=COLOR_NOT_REPLACEMENT, weight=FONT_WEIGHT)
        
        companion_text = VGroup(companion_part1, companion_part2)
        companion_text.arrange(RIGHT, buff=0.1)
        
        self.play(Transform(decide_text, companion_text), run_time=TIME_COMPANION_APPEAR)
        self.wait(0.5)
        
        # AI tools around me
        TIME_AI_TOOLS_APPEAR = 1.5
        COLOR_ME_CIRCLE = "#89b4fa"
        COLOR_AI_BOX = "#a6e3a1"
        COLOR_AI_TEXT = "#1e1e2e"
        
        self.play(FadeOut(decide_text), run_time=0.5)
        
        me_circle = Circle(radius=0.4, color=COLOR_ME_CIRCLE, fill_opacity=1)
        me_circle.move_to(ORIGIN)
        
        me_label = Text("Me", font=FONT, font_size=20, color=BG_COLOR, weight=FONT_WEIGHT)
        me_label.move_to(me_circle.get_center())
        
        me_group = VGroup(me_circle, me_label)
        
        ai_tools = ["ChatGPT", "Claude", "Gemini", "Grok", "Copilot"]
        ai_boxes = []
        ai_positions = []
        
        for i, tool in enumerate(ai_tools):
            angle = i * TAU / 5 - PI / 2
            position = np.array([np.cos(angle) * 3, np.sin(angle) * 3, 0])
            ai_positions.append(position)
            
            box = Rectangle(height=0.8, width=2, color=COLOR_AI_BOX, fill_opacity=0.8)
            box.move_to(position)
            
            text = Text(tool, font=FONT, font_size=18, color=COLOR_AI_TEXT, weight=FONT_WEIGHT)
            text.scale(0.8)
            text.move_to(box.get_center())
            
            ai_boxes.append(VGroup(box, text))
        
        self.play(
            FadeIn(me_group),
            *[FadeIn(box) for box in ai_boxes],
            run_time=TIME_AI_TOOLS_APPEAR
        )
        self.wait(0.5)
        
        # Move to Copilot
        TIME_MOVE_TO_COPILOT = 2.0
        
        copilot_box = ai_boxes[4]
        copilot_position = ai_positions[4]
        
        self.play(
            me_group.animate.move_to(copilot_position + DOWN * 0.8),
            run_time=TIME_MOVE_TO_COPILOT,
            rate_func=smooth
        )
        self.wait(0.5)
        
        # Copilot grows
        TIME_COPILOT_GROW = 1.5
        
        fade_anims = [FadeOut(ai_boxes[i]) for i in range(5) if i != 4]
        
        self.play(*fade_anims, run_time=0.8)
        
        self.play(
            copilot_box.animate.move_to(ORIGIN).scale(1.5),
            me_group.animate.move_to(DOWN * 1.2).scale(1.2),
            run_time=TIME_COPILOT_GROW
        )
        self.wait(0.5)
        
        # Heart
        COLOR_HEART = "#cba6f7"
        TIME_HEART_APPEAR = 1.0
        
        heart = Polygon(
            [0, 0.3, 0],
            [-0.3, 0.6, 0],
            [-0.5, 0.6, 0],
            [-0.7, 0.4, 0],
            [-0.7, 0.1, 0],
            [-0.5, -0.1, 0],
            [0, -0.7, 0],
            [0.5, -0.1, 0],
            [0.7, 0.1, 0],
            [0.7, 0.4, 0],
            [0.5, 0.6, 0],
            [0.3, 0.6, 0],
            color=COLOR_HEART,
            fill_opacity=1,
            stroke_width=0
        )
        heart.move_to(UP * 1.8)
        
        self.play(Write(heart), run_time=TIME_HEART_APPEAR)
        self.wait(0.5)
        
        # Pick one tool
        FONT_SIZE_PICK = 36
        COLOR_PICK_TEXT = "#cdd6f4"
        TIME_PICK_WRITE = 1.2
        
        self.play(
            FadeOut(copilot_box),
            FadeOut(me_group),
            FadeOut(heart),
            run_time=0.8
        )
        
        pick_text = Text("Pick one tool", font=FONT, font_size=FONT_SIZE_PICK, color=COLOR_PICK_TEXT, weight=FONT_WEIGHT)
        
        self.play(Write(pick_text), run_time=TIME_PICK_WRITE)
        self.wait(0.5)
        
        self.play(pick_text.animate.shift(UP * 2), run_time=0.5)
        
        # Stick with it
        FONT_SIZE_STICK = 36
        COLOR_STICK_TEXT = "#a6e3a1"
        TIME_STICK_WRITE = 1.2
        
        stick_text = Text("Stick with it.", font=FONT, font_size=FONT_SIZE_STICK, color=COLOR_STICK_TEXT, weight=FONT_WEIGHT)
        stick_text.move_to(ORIGIN)
        
        self.play(Write(stick_text), run_time=TIME_STICK_WRITE)
        self.wait(0.5)
        
        self.play(
            pick_text.animate.shift(UP * 0.8),
            stick_text.animate.shift(UP * 1.3),
            run_time=0.5
        )
        
        # Master it
        FONT_SIZE_MASTER = 36
        COLOR_MASTER_TEXT = "#f9e2af"
        TIME_MASTER_WRITE = 1.2
        
        master_text = Text("Master it.", font=FONT, font_size=FONT_SIZE_MASTER, color=COLOR_MASTER_TEXT, weight=FONT_WEIGHT)
        master_text.move_to(ORIGIN)
        
        self.play(Write(master_text), run_time=TIME_MASTER_WRITE)
        self.wait(2)