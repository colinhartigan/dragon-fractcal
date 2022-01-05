class Generator:

    def __init__(self, first_move="R", ):
        self.first_move = first_move
        self.cache = [[],[self.first_move]] # empty list at index 0 so indexing is easier (start at 1)
        self.max_iter = 1

    def mirror(self, moves):
        # helper method to mirror moves for next iteration
        mirrored = [] # empty list to hold the mirrored moves
        for move in moves: # iterate through every move
            if move == "R": # if the move move is R flip it to L
                mirrored.append("L")
            elif move == "L": # vice versa
                mirrored.append("R")
        return mirrored # return the mirrored list

    def reverse(self, moves):
        # helper method to reverse a list, could be done in the generate method but i kept it separate to keep code clean and consistent
        return moves[::-1]

    def generate(self,target_iter):
        # generate the sequence of moves to get to the target iteration
        
        while self.max_iter < target_iter:
            # i implemented a cache to avoid recalculating the same sequence of moves (useful when we get to thousands of moves and want to keep calculation time relatively fast)
            last_iter_data = self.cache[self.max_iter] # get the most recent kown iteration 
            last_iter_mirrored_reversed = self.reverse(self.mirror(last_iter_data)) # reverse and mirror

            next_iter_data = [] # initialize an empty list of the next iteration
            next_iter_data.extend(last_iter_data) # start the new iteration by appending the previous iteration
            next_iter_data.append("R") # add an R
            next_iter_data.extend(last_iter_mirrored_reversed) # append the mirrored/reversed data to complete the iteration
            
            self.cache.append(next_iter_data) # add the new iteration to the cache
            self.max_iter += 1 # incriment the amount of known iterations

        return self.cache[target_iter] # return the target iteration