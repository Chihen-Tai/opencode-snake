import random
import tkinter as tk

WIDTH, HEIGHT = 600, 400
GRID = 20
SPEED = 120

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Snake')
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()

        self.direction = 'Right'
        self.next_direction = 'Right'
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.spawn_food()
        self.score = 0
        self.running = True

        self.root.bind('<Up>', lambda e: self.set_direction('Up'))
        self.root.bind('<Down>', lambda e: self.set_direction('Down'))
        self.root.bind('<Left>', lambda e: self.set_direction('Left'))
        self.root.bind('<Right>', lambda e: self.set_direction('Right'))
        self.root.bind('w', lambda e: self.set_direction('Up'))
        self.root.bind('s', lambda e: self.set_direction('Down'))
        self.root.bind('a', lambda e: self.set_direction('Left'))
        self.root.bind('d', lambda e: self.set_direction('Right'))
        self.root.bind('r', lambda e: self.restart())

        self.tick()

    def set_direction(self, d):
        opposite = {'Up':'Down','Down':'Up','Left':'Right','Right':'Left'}
        if d != opposite[self.direction]:
            self.next_direction = d

    def spawn_food(self):
        while True:
            x = random.randrange(0, WIDTH, GRID)
            y = random.randrange(0, HEIGHT, GRID)
            if (x, y) not in self.snake:
                return (x, y)

    def move_head(self, head):
        x, y = head
        d = self.direction
        if d == 'Up':
            y -= GRID
        elif d == 'Down':
            y += GRID
        elif d == 'Left':
            x -= GRID
        elif d == 'Right':
            x += GRID
        return (x, y)

    def collision(self, head):
        x, y = head
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return True
        if head in self.snake:
            return True
        return False

    def draw(self):
        self.canvas.delete('all')
        for i, (x, y) in enumerate(self.snake):
            color = '#00ff66' if i == 0 else '#22cc66'
            self.canvas.create_rectangle(x, y, x+GRID, y+GRID, fill=color, outline='')

        fx, fy = self.food
        self.canvas.create_oval(fx+2, fy+2, fx+GRID-2, fy+GRID-2, fill='#ff4444', outline='')

        self.canvas.create_text(8, 8, anchor='nw', fill='white',
                                text=f'Score: {self.score}  (WASD/方向鍵, R重開)')

        if not self.running:
            self.canvas.create_text(WIDTH//2, HEIGHT//2, fill='white',
                                    text='Game Over! Press R to restart', font=('Arial', 18, 'bold'))

    def tick(self):
        if self.running:
            self.direction = self.next_direction
            new_head = self.move_head(self.snake[0])

            if self.collision(new_head):
                self.running = False
            else:
                self.snake.insert(0, new_head)
                if new_head == self.food:
                    self.score += 1
                    self.food = self.spawn_food()
                else:
                    self.snake.pop()

        self.draw()
        self.root.after(SPEED, self.tick)

    def restart(self):
        self.direction = 'Right'
        self.next_direction = 'Right'
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.spawn_food()
        self.score = 0
        self.running = True

if __name__ == '__main__':
    root = tk.Tk()
    SnakeGame(root)
    root.resizable(False, False)
    root.mainloop()
