from tkinter import *


class Application:
    def __init__(self, root):
        self.root=root
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.pixel_grid_width=1050
        self.pixel_grid_height=700
        root.title("ĐỒ ÁN KỸ THUẬT ĐỒ HỌA")
        root.configure(padx=20, pady=20)
        root.attributes('-topmost', True)
        root.geometry(f"{self.screen_width}x{self.screen_height}")
        

    def create_grid_pixel(self):
        grid_pixel = Frame(self.root, height= self.pixel_grid_height, width=self.pixel_grid_width)
        grid_pixel.pack(side=LEFT)
        self.root.update()

        canvas = Canvas(grid_pixel, width=grid_pixel.winfo_width(), height=grid_pixel.winfo_height(), bg="#FEFAF6")
        self.canvas=canvas
        canvas.pack(fill=BOTH, expand=True)
        canvas.update()
        print(canvas.winfo_width())
        canvas_width = (canvas.winfo_width()//10)*10
        canvas_height = (canvas.winfo_height()//10)*10
        self.canvas_width=canvas_width
        self.canvas_height=canvas_height

        goc_toa_do=(canvas_width/2, canvas_height/2)

        #draw grid
        grid_size=5
        for x in range(0,canvas_width, grid_size):
            canvas.create_line(x, 0, x, canvas_height, fill="#EADBC8")
        for y in range(0,canvas_height, grid_size):
            canvas.create_line(0, y, canvas_width, y, fill="#EADBC8")
            
            
        # X axis
        canvas.create_line(0, canvas_height/2, canvas_width, canvas_height/2)
        
        
        # Y axis
        canvas.create_line(canvas_width/2, 0, canvas_width/2, canvas_height, fill="black")
        

    def put_pixel(self, x, y, color="green"):
        adjusted_x = self.canvas_width/2 + x*5
        adjusted_y = self.canvas_height/2 - y*5
        self.canvas.create_rectangle(adjusted_x-2, adjusted_y-2, adjusted_x+2, adjusted_y+2, fill=color, outline=None)
        
    def draw_line(self, x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1
        x_step=1 if x1<x2 else -1
        y_step=1 if y1<y2 else -1
        f1 = 2 * (dy - dx)
        f2 = 2 * dy 
        p = 2 * dy - dx
        if dx>dy:
            while x != x2:
                x += x_step
                if p < 0:
                    p += f2
                else:
                    p += f1
                    y += y_step
                self.put_pixel(x,y)
        else:
            p=2*dx-dy
            f1 = 2 * (dx - dy)
            f2 = 2 * dx
            while y!=y2:
                y+=y_step
                if p < 0:
                    p += f2
                else:
                    p += f1
                    x += x_step
                self.put_pixel(x,y)

    def draw_circle(self, x_center, y_center, radius):
        x = radius
        y = 0
        p = 1 - radius

        points = []

        while x >= y:
            points.extend([
                (x_center + x, y_center + y),
                (x_center - x, y_center + y),
                (x_center + x, y_center - y),
                (x_center - x, y_center - y),
                (x_center + y, y_center + x),
                (x_center - y, y_center + x),
                (x_center + y, y_center - x),
                (x_center - y, y_center - x)
            ])

            y += 1

            if p <= 0:
                p = p + 2*y + 1
            else:
                x -= 1
                p = p + 2*y - 2*x + 1

        for point in points:
            self.put_pixel(point[0], point[1])

    def draw_rectangle(self, x1, y1, x2, y2):
        self.draw_line(x1, y1, x2, y1)
        self.draw_line(x2, y1, x2, y2)
        self.draw_line(x2, y2, x1, y2)
        self.draw_line(x1, y2, x1, y1)

    def draw_triangle(self, x1, y1, x2, y2, x3, y3):
        self.draw_line(x1, y1, x2, y2)
        self.draw_line(x2, y2, x3, y3)
        self.draw_line(x3, y3, x1, y1)
        
    def draw_isosceles_triangle(self, x1, y1, base, height):
        # Tính toán tọa độ của các đỉnh của tam giác cân
        x2 = x1 + base
        y2 = y1
        x3 = x1 + base / 2
        y3 = y1 + height

        # Vẽ các cạnh của tam giác
        self.draw_line(x1, y1, x2, y2)  # Cạnh đáy
        self.draw_line(x1, y1, x3, y3)  # Cạnh bên
        self.draw_line(x2, y2, x3, y3)  # Cạnh bên
        
    def draw_right_triangle(self, x1, y1, base, height):
        x2 = x1 + base
        y2 = y1
        x3 = x1
        y3 = y1 + height

        # Vẽ các cạnh của tam giác
        self.draw_line( x1, y1, x2, y2)  # Cạnh đáy
        self.draw_line(x2, y2, x3, y3)  # Cạnh kề
        self.draw_line(x3, y3, x1, y1)  # Cạnh huyền