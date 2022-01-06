import csv

class CSV:

    def __init__(self, filename="output.csv"):
        self.filename = filename

    def output_data(self, iterations):
        num_iterations = len(iterations)
        headers = [str(i) for i in range(num_iterations)]

        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(headers)

            for index in range(len(iterations[-1])):
                row = []
                for iteration in iterations:
                    try: row.append(iteration[index])
                    except: row.append(0)
                writer.writerow(row)
            
            
        print("done")