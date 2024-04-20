from tkinter import *
import GUI 

def main():

    root=Tk()
    App=GUI.Application(root)
    App.create_grid_pixel()
    App.put_pixel(10, 10)
    App.draw_line(-10, -10, 50, -80)
    App.draw_circle(10,10,20)
    App.draw_rectangle(5,10,20,20)
    #App.draw_triangle(1,1,5,20,20,4)
    App.draw_isosceles_triangle(2,2,30,50)
    
    
    root.mainloop()
if __name__ == "__main__":
    main()
    