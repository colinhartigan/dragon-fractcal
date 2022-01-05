from .generator import Generator

def run():
    generator = Generator()
    
    for i in range(10):
        print(f"iteration {i}: \n{generator.generate(i)}\n\n")
