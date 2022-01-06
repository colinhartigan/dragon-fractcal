from .generator import Generator
from .parser import Parser
from .turtle import Turtle
from .csv import CSV

def run():
    generator = Generator()
    parser = Parser()
    csv = CSV()
    
    # for i in range(10):
    #     print(f"iteration {i}: \n{generator.generate(i)}\n\n")

    sequences = [generator.generate(i) for i in range(21)]
    #print(f"sequence: {sequence}")

    calculated = [parser.parse(sequence, 90) for sequence in sequences]
    #print(f"calculated: {calculated}")

    # turtle = Turtle(show_updates=False, speed=0)
    # turtle.draw_fractal(calculated)

    csv.output_data(calculated)