from manim import *

class Part1PickAPath(Scene):
    def construct(self):
        # Global settings
        BG_COLOR = "#1e1e2e"
        self.camera.background_color = BG_COLOR
        FONT = "JetBrainsMono Nerd Font"
        
        # Font Weight Options: THIN, LIGHT, NORMAL, BOLD, HEAVY, ULTRABOLD
        FONT_WEIGHT = BOLD
        
        # "First" text
        FONT_SIZE_FIRST = 48
        COLOR_FIRST_TEXT = "#cdd6f4"
        TIME_FIRST_APPEAR = 0.5
        
        first_text = Text("First", font=FONT, font_size=FONT_SIZE_FIRST, color=COLOR_FIRST_TEXT, weight=FONT_WEIGHT)
        self.play(Write(first_text), run_time=TIME_FIRST_APPEAR)
        self.wait(0.5)
        
        # Circle transform
        CIRCLE_RADIUS = 0.3
        COLOR_CIRCLE = "#89b4fa"
        TIME_CIRCLE_TRANSFORM = 1.0 
        
        circle1 = Circle(radius=CIRCLE_RADIUS, color=COLOR_CIRCLE, fill_opacity=1)
        circle1.move_to(LEFT * 3)
        self.play(Transform(first_text, circle1), run_time=TIME_CIRCLE_TRANSFORM)
        self.remove(first_text)
        self.add(circle1)
        self.wait(0.3)
        
        # Path to another circle
        COLOR_PATH = "#cdd6f4"
        TIME_PATH_CREATION = 1.0 
        
        circle2 = Circle(radius=CIRCLE_RADIUS, color=COLOR_CIRCLE, fill_opacity=1)
        circle2.move_to(RIGHT * 3)
        
        path_line = Line(circle1.get_center(), circle2.get_center(), color=COLOR_PATH, stroke_width=6)
        
        self.play(
            Create(path_line),
            FadeIn(circle2),
            run_time=TIME_PATH_CREATION
        )
        self.wait(0.5)
        
        # Circle moves along path
        TIME_CIRCLE_MOVE = 1.0  
        
        self.play(
            circle1.animate.move_to(circle2.get_center()),
            run_time=TIME_CIRCLE_MOVE,
            rate_func=smooth
        )
        self.wait(0.3)
        
        # Slice cuts through
        COLOR_SLICE = "#f38ba8"
        SLICE_WIDTH = 8
        TIME_SLICE_CUT = 1.0 
        
        mid_point = (LEFT * 3 + RIGHT * 3) / 2
        
        slice_line = Line(
            mid_point + UP * 4,
            mid_point + DOWN * 4,
            color=COLOR_SLICE,
            stroke_width=SLICE_WIDTH
        )
        slice_line.set_opacity(0)
        
        left_path = Line(LEFT * 3, mid_point, color=COLOR_PATH, stroke_width=6)
        right_path = Line(mid_point, RIGHT * 3, color=COLOR_PATH, stroke_width=6)
        
        self.add(slice_line)
        self.play(
            slice_line.animate.set_opacity(1),
            Flash(mid_point, color=COLOR_SLICE, flash_radius=1.5, line_length=0.5),
            run_time=0.3 
        )
        
        self.remove(path_line)
        self.add(left_path, right_path)
        
        self.play(
            left_path.animate.shift(LEFT * 0.5),
            right_path.animate.shift(RIGHT * 0.5),
            circle2.animate.shift(RIGHT * 0.5),
            circle1.animate.shift(RIGHT * 0.5),
            slice_line.animate.set_opacity(0.5),
            run_time=TIME_SLICE_CUT
        )
        
        self.wait(0.5)
        
        self.play(
            FadeOut(slice_line),
            FadeOut(left_path),
            FadeOut(right_path),
            FadeOut(circle1),
            FadeOut(circle2),
            run_time=0.5
        )
        
        # "Programming isn't one thing"
        FONT_SIZE_PROGRAMMING = 36
        COLOR_PROGRAMMING_TEXT = "#cdd6f4"
        TIME_TEXT_TRANSFORM = 1.0 
        
        programming_text = Text(
            "Programming isn't one thing.",
            font=FONT,
            font_size=FONT_SIZE_PROGRAMMING,
            color=COLOR_PROGRAMMING_TEXT,
            weight=FONT_WEIGHT
        )
        
        self.play(FadeIn(programming_text), run_time=TIME_TEXT_TRANSFORM)
        self.wait(0.5)
        
        # Tree structure
        COLOR_TREE_ROOT = "#a6e3a1"
        FONT_SIZE_START_BOX = 28
        COLOR_TREE_BOXES = "#89b4fa"
        FONT_SIZE_BRANCH_LABELS = 24
        COLOR_TREE_BRANCHES = "#cdd6f4"
        TIME_TREE_CREATION = 2.0  
        
        tree_root = Rectangle(height=0.6, width=2, color=COLOR_TREE_ROOT, fill_opacity=1)
        tree_root.move_to(UP * 2)
        root_text = Text("Start", font=FONT, font_size=FONT_SIZE_START_BOX, color=BG_COLOR, weight=FONT_WEIGHT)
        root_text.move_to(tree_root.get_center())
        
        branches = []
        branch_boxes = []
        branch_labels = ["Web Dev", "Mobile", "Data", "Game Dev", "AI/ML"]
        
        for i, label in enumerate(branch_labels):
            x_pos = -4 + i * 2
            y_pos = -1
            
            box = Rectangle(height=0.5, width=1.8, color=COLOR_TREE_BOXES, fill_opacity=0.8)
            box.move_to([x_pos, y_pos, 0])
            branch_boxes.append(box)
            
            text = Text(label, font=FONT, font_size=FONT_SIZE_BRANCH_LABELS, color=COLOR_FIRST_TEXT, weight=FONT_WEIGHT)
            text.scale(0.6)
            text.move_to(box.get_center())
            branch_boxes.append(text)
            
            line = Line(tree_root.get_bottom(), box.get_top(), color=COLOR_TREE_BRANCHES, stroke_width=3)
            branches.append(line)
        
        # "There are many paths" text
        FONT_SIZE_MANY_PATHS = 36
        COLOR_MANY_PATHS_TEXT = "#cdd6f4"
        
        many_paths_text = Text(
            "There are many paths",
            font=FONT,
            font_size=FONT_SIZE_MANY_PATHS,
            color=COLOR_MANY_PATHS_TEXT,
            weight=FONT_WEIGHT
        )
        many_paths_text.move_to(DOWN * 2.2)
        
        self.play(
            FadeOut(programming_text),
            FadeIn(tree_root),
            FadeIn(root_text),
            run_time=TIME_TREE_CREATION / 3  
        )
        
        self.play(
            *[Create(line) for line in branches],
            *[FadeIn(box) for box in branch_boxes],
            run_time=TIME_TREE_CREATION * 2/3 
        )
        
        self.play(FadeIn(many_paths_text), run_time=0.5) 
        self.wait(0.5)
        
        # Highlight one path
        COLOR_HIGHLIGHT = "#a6e3a1"
        FONT_SIZE_PICK_ONE = 36
        TIME_PATH_HIGHLIGHT = 1.0 
        
        selected_index = 2
        highlighted_box = branch_boxes[selected_index * 2]
        highlighted_text = branch_boxes[selected_index * 2 + 1]
        
        pick_one_text = Text(
            "But right now, pick only one",
            font=FONT,
            font_size=FONT_SIZE_PICK_ONE,
            color=COLOR_MANY_PATHS_TEXT,
            weight=FONT_WEIGHT
        )
        pick_one_text.move_to(DOWN * 2.2)
        
        fade_anims = []
        for i, box in enumerate(branch_boxes):
            if i != selected_index * 2 and i != selected_index * 2 + 1:
                fade_anims.append(box.animate.set_opacity(0.2))
        
        for i, line in enumerate(branches):
            if i != selected_index:
                fade_anims.append(line.animate.set_opacity(0.2))
        
        self.play(
            highlighted_box.animate.set_color(COLOR_HIGHLIGHT),
            Transform(many_paths_text, pick_one_text),
            *fade_anims,
            run_time=TIME_PATH_HIGHLIGHT
        )
        self.wait(0.5)
        
        # Selected path grows
        SELECTED_SCALE = 2.0
        TIME_PATH_SELECTION = 0.8  
        
        fade_out_anims = []
        for i, box in enumerate(branch_boxes):
            if i != selected_index * 2 and i != selected_index * 2 + 1:
                fade_out_anims.append(FadeOut(box))
        
        for i, line in enumerate(branches):
            if i != selected_index:
                fade_out_anims.append(FadeOut(line))
        
        self.play(
            highlighted_box.animate.scale(SELECTED_SCALE),
            highlighted_text.animate.scale(SELECTED_SCALE),
            FadeOut(tree_root),
            FadeOut(root_text),
            FadeOut(branches[selected_index]),
            FadeOut(many_paths_text),
            *fade_out_anims,
            run_time=TIME_PATH_SELECTION
        )
        self.wait(0.5)
        
        self.play(
            FadeOut(highlighted_box),
            FadeOut(highlighted_text),
            run_time=0.5
        )
        
        # Journey path
        COLOR_JOURNEY_PATH = "#cdd6f4"
        COLOR_DATA_BOX = "#a6e3a1"
        FONT_SIZE_DATA_BOX = 24
        COLOR_YOU_CIRCLE = "#89b4fa"
        COLOR_YOU_LABEL = "#cdd6f4"
        FONT_SIZE_YOU_LABEL = 24
        TIME_YOU_MOVEMENT = 4.0 
        
        start_point = LEFT * 4.5
        end_point = RIGHT * 4.5
        
        points = [
            start_point,
            start_point + RIGHT * 1.5 + DOWN * 1.5,
            start_point + RIGHT * 3 + UP * 1,
            start_point + RIGHT * 4.5 + DOWN * 0.5,
            start_point + RIGHT * 6 + UP * 1.5,
            start_point + RIGHT * 7.5 + DOWN * 0.5,
            end_point
        ]
        
        journey_path = VMobject(color=COLOR_JOURNEY_PATH, stroke_width=6)
        journey_path.set_points_smoothly(points)
        
        end_box = Rectangle(height=0.5, width=1.8, color=COLOR_DATA_BOX, fill_opacity=1)
        end_box.move_to(end_point)
        
        end_text = Text("Data", font=FONT, font_size=FONT_SIZE_DATA_BOX, color=BG_COLOR, weight=FONT_WEIGHT)
        end_text.scale(0.6)
        end_text.move_to(end_box.get_center())
        
        you_circle = Circle(radius=CIRCLE_RADIUS, color=COLOR_YOU_CIRCLE, fill_opacity=1)
        you_circle.move_to(journey_path.get_start())
        
        you_label = Text("You", font=FONT, font_size=FONT_SIZE_YOU_LABEL, color=COLOR_YOU_LABEL, weight=FONT_WEIGHT)
        you_label.next_to(you_circle, UP, buff=0.2)
        
        self.play(
            Create(journey_path),
            FadeIn(end_box),
            FadeIn(end_text),
            FadeIn(you_circle),
            FadeIn(you_label),
            run_time=1.5 
        )
        
        self.play(
            MoveAlongPath(you_circle, journey_path),
            MoveAlongPath(you_label, journey_path.copy().shift(UP * 0.5)),
            run_time=TIME_YOU_MOVEMENT,
            rate_func=smooth
        )
        self.wait(0.3)
        
        # Old you appears
        COLOR_OLD_YOU = "#cdd6f4"
        FONT_SIZE_OLD_YOU = 20
        TIME_CIRCLE_MERGE = 1.5 
        
        old_you_circle = Circle(radius=CIRCLE_RADIUS, color=COLOR_OLD_YOU, fill_opacity=1)
        old_you_circle.move_to(journey_path.get_start())
        
        old_you_label = Text("Old you", font=FONT, font_size=FONT_SIZE_OLD_YOU, color=COLOR_OLD_YOU, weight=FONT_WEIGHT)
        old_you_label.next_to(old_you_circle, UP, buff=0.2)
        
        self.play(
            FadeOut(journey_path),
            FadeOut(end_box),
            FadeOut(end_text),
            FadeIn(old_you_circle),
            FadeIn(old_you_label),
            run_time=0.8 
        )
        
        self.play(
            you_circle.animate.move_to(LEFT * 1.5),
            you_label.animate.move_to(LEFT * 1.5 + UP * 0.5),
            old_you_circle.animate.move_to(RIGHT * 1.5),
            old_you_label.animate.move_to(RIGHT * 1.5 + UP * 0.5),
            run_time=TIME_CIRCLE_MERGE
        )
        self.wait(0.3)
        
        # "Yeah, I'm better than before"
        FONT_SIZE_BETTER_THAN = 16
        COLOR_BETTER_TEXT = "#a6e3a1"
        
        better_text = Text(
            "yeah, I'm better than before.",
            font=FONT,
            font_size=FONT_SIZE_BETTER_THAN,
            color=COLOR_BETTER_TEXT,
            weight=FONT_WEIGHT
        )
        better_text.move_to(LEFT * 1.5 + UP * 0.5)
        
        self.play(
            Transform(you_label, better_text),
            run_time=TIME_TEXT_TRANSFORM 
        )
        self.wait(0.5)
        
        # Leaderboard
        COLOR_LEADERBOARD_YOU = "#a6e3a1"
        FONT_SIZE_LEADERBOARD_YOU = 32
        COLOR_LEADERBOARD_OTHERS = "#cdd6f4"
        FONT_SIZE_LEADERBOARD_OTHERS = 24
        TIME_LEADERBOARD = 1.5 
        
        bar_bottom = DOWN * 2.5
        bar_width = 0.9
        bar_spacing = 1.2
        
        you_bar = Rectangle(
            height=0.1,
            width=bar_width,
            color=COLOR_LEADERBOARD_YOU,
            fill_opacity=1,
            stroke_width=2,
            stroke_color=COLOR_FIRST_TEXT
        )
        you_bar.next_to(bar_bottom, UP, buff=0)
        you_bar.shift(LEFT * 3)
        
        you_bar_label = Text("You", font=FONT, font_size=FONT_SIZE_LEADERBOARD_YOU, color=BG_COLOR, weight=FONT_WEIGHT)
        you_bar_label.move_to(you_bar.get_center())
        
        other_bars = []
        other_bar_heights = [2.5, 2.0, 1.8, 1.5, 1.2]
        
        for i in range(5):
            bar = Rectangle(
                height=0.1,
                width=bar_width,
                color=COLOR_LEADERBOARD_OTHERS,
                fill_opacity=0.7,
                stroke_width=2,
                stroke_color=COLOR_FIRST_TEXT
            )
            bar.next_to(bar_bottom, UP, buff=0)
            bar.shift(RIGHT * (i * bar_spacing - 1.5))
            other_bars.append((bar, other_bar_heights[i]))
        
        others_text = Text("Others", font=FONT, font_size=FONT_SIZE_LEADERBOARD_OTHERS, color=COLOR_FIRST_TEXT, weight=FONT_WEIGHT)
        others_text.next_to(bar_bottom, DOWN, buff=0.3)
        
        self.play(
            FadeOut(you_circle),
            FadeOut(you_label),
            FadeOut(old_you_circle),
            FadeOut(old_you_label),
            FadeIn(you_bar),
            FadeIn(you_bar_label),
            *[FadeIn(bar) for bar, _ in other_bars],
            FadeIn(others_text),
            run_time=0.5 
        )
        
        # Grow bars
        target_you_bar = Rectangle(
            height=4,
            width=bar_width,
            color=COLOR_LEADERBOARD_YOU,
            fill_opacity=1,
            stroke_width=2,
            stroke_color=COLOR_FIRST_TEXT
        )
        target_you_bar.next_to(bar_bottom, UP, buff=0)
        target_you_bar.shift(LEFT * 3)
        
        target_you_label = Text("You", font=FONT, font_size=FONT_SIZE_LEADERBOARD_YOU, color=BG_COLOR, weight=FONT_WEIGHT)
        target_you_label.move_to(target_you_bar.get_center())
        
        grow_anims = [
            Transform(you_bar, target_you_bar),
            Transform(you_bar_label, target_you_label)
        ]
        
        for idx, (bar, target_height) in enumerate(other_bars):
            target_bar = Rectangle(
                height=target_height,
                width=bar_width,
                color=COLOR_LEADERBOARD_OTHERS,
                fill_opacity=0.7,
                stroke_width=2,
                stroke_color=COLOR_FIRST_TEXT
            )
            target_bar.next_to(bar_bottom, UP, buff=0)
            target_bar.shift(RIGHT * (idx * bar_spacing - 1.5))
            grow_anims.append(Transform(bar, target_bar))
        
        self.play(*grow_anims, run_time=TIME_LEADERBOARD)
        self.wait(0.8)
        
        # "To make choosing easier"
        FONT_SIZE_CHOOSING = 36
        COLOR_CHOOSING_TEXT = "#cdd6f4"
        TIME_FINAL_TEXT = 1.0 
        
        choosing_text = Text(
            "To make choosing easier",
            font=FONT,
            font_size=FONT_SIZE_CHOOSING,
            color=COLOR_CHOOSING_TEXT,
            weight=FONT_WEIGHT
        )
        
        self.play(
            Transform(you_bar, choosing_text),
            FadeOut(you_bar_label),
            *[FadeOut(bar) for bar, _ in other_bars],
            FadeOut(others_text),
            run_time=TIME_FINAL_TEXT 
        )
        self.wait(0.5)
        
        # "So remember this"
        FONT_SIZE_REMEMBER = 36
        COLOR_REMEMBER_TEXT = "#cdd6f4"
        TIME_WRITE_SPEED = 0.8
        
        self.play(FadeOut(you_bar), run_time=0.5)
        
        remember_text = Text(
            "So remember this:",
            font=FONT,
            font_size=FONT_SIZE_REMEMBER,
            color=COLOR_REMEMBER_TEXT,
            weight=FONT_WEIGHT
        )
        
        self.play(Write(remember_text), run_time=TIME_WRITE_SPEED)
        self.wait(0.5)
        
        # "Don't research forever"
        FONT_SIZE_RESEARCH = 36
        COLOR_RESEARCH_TEXT = "#cdd6f4"
        
        research_text = Text(
            "Don't research forever.",
            font=FONT,
            font_size=FONT_SIZE_RESEARCH,
            color=COLOR_RESEARCH_TEXT,
            weight=FONT_WEIGHT
        )
        
        self.play(
            Transform(remember_text, research_text),
            run_time=TIME_FINAL_TEXT 
        )
        self.wait(0.3)
        
        self.play(remember_text.animate.shift(UP * 1), run_time=0.5)
        
        # "Decide first. Learn second."
        FONT_SIZE_DECIDE = 36
        COLOR_DECIDE_TEXT = "#cdd6f4"
        COLOR_FIRST_WORD = "#f38ba8"
        COLOR_SECOND_WORD = "#89b4fa"
        
        decide_text = Text("Decide  ", font=FONT, font_size=FONT_SIZE_DECIDE, color=COLOR_DECIDE_TEXT, weight=FONT_WEIGHT)
        first_text = Text("first", font=FONT, font_size=FONT_SIZE_DECIDE, color=COLOR_FIRST_WORD, weight=FONT_WEIGHT)
        dot1 = Text(". ", font=FONT, font_size=FONT_SIZE_DECIDE, color=COLOR_DECIDE_TEXT, weight=FONT_WEIGHT)
        learn_text = Text("Learn  ", font=FONT, font_size=FONT_SIZE_DECIDE, color=COLOR_DECIDE_TEXT, weight=FONT_WEIGHT)
        second_text = Text("second", font=FONT, font_size=FONT_SIZE_DECIDE, color=COLOR_SECOND_WORD, weight=FONT_WEIGHT)
        dot2 = Text(".", font=FONT, font_size=FONT_SIZE_DECIDE, color=COLOR_DECIDE_TEXT, weight=FONT_WEIGHT)
        
        final_line = VGroup(decide_text, first_text, dot1, learn_text, second_text, dot2)
        final_line.arrange(RIGHT, buff=0.1)
        final_line.next_to(remember_text, DOWN, buff=0.5)
        
        self.play(Write(final_line), run_time=TIME_WRITE_SPEED * 2.0)
        self.wait(2)