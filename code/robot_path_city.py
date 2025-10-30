from manim import *

class RobotPathCity(Scene):
    def construct(self):
        # 1. Add city background
        bg = ImageMobject("assets/your_latest_city_background.png")
        bg.scale_to_fit_width(16)
        self.add(bg)

        # 2. Define node positions on your map
        positions = {
            'A': [-5, 2.8, 0],
            'B': [-2, 1.6, 0],
            'C': [-2, 4, 0],
            'D': [1, 1, 0],
            'E': [3.5, 3.5, 0],
            'F': [3.8, -0.5, 0],
            'G': [5, -2.5, 0]
        }

        # 3. Show all possible paths (gray)
        edges = [
            ('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'),
            ('C', 'D'), ('D', 'E'), ('E', 'F'), ('D', 'F'), ('F', 'G')
        ]
        for start, end in edges:
            line = Line(positions[start], positions[end], color=GRAY)
            self.play(Create(line), run_time=0.3)

        # 4. Draw all nodes and their labels
        for name, pos in positions.items():
            dot = Dot(pos, color=WHITE, radius=0.1)
            label = Text(name, font_size=24, color=WHITE).next_to(dot, UP, buff=0.1)
            self.add(dot, label)

        # 5. Animate the shortest path
        shortest_path = ['A', 'B', 'D', 'F', 'G']
        for i in range(len(shortest_path) - 1):
            start = positions[shortest_path[i]]
            end = positions[shortest_path[i + 1]]
            yellow_line = Line(start, end, color=YELLOW, stroke_width=6)
            self.play(Create(yellow_line), run_time=0.4)

        # 6. Add robot image and animate movement
        robot = ImageMobject("assets/robot.png").scale(0.2).move_to(positions['A'])
        self.add(robot)

        for i in range(1, len(shortest_path)):
            next_pos = positions[shortest_path[i]]
            self.play(robot.animate.move_to(next_pos), run_time=2)

        self.wait(1)
