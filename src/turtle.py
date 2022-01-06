from tqdm import tqdm
import turtle

class Turtle:

    def __init__(self, length=1, speed=10, show_updates=False):
        self.wn = turtle.Screen()
        self.wn.bgcolor("black")
        self.wn.title("fractal")
        self.wn.setup(width=.7, height=.7, )
        self.wn.screensize(canvwidth=3000, canvheight=3000)

        self.turt = turtle.Turtle()
        self.turt.color("white")

        self.length = length
        self.speed = speed
        self.show_updates = show_updates

    def draw_fractal(self, sequence,):
        
        self.wn.title(f"fractal: {len(sequence)} moves")

        self.turt.speed(self.speed)
        
        if not self.show_updates:
            self.wn.tracer(0)

        with tqdm(total=len(sequence), desc="Generating fractal") as t:
            for index,move in enumerate(sequence):
                #self.wn.title(f"fractal: {len(sequence)-index} moves left")
                self.turt.setheading(move)
                self.turt.forward(self.length)
                t.update()

        self.wn.update() 
        self.wn.mainloop()