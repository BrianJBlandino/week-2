import numpy as np

def ways(n):
    """Creating a function that takes an integer (n) and returns the number of ways you
    can make change using only pennies and nickels"""
    
    # ensuring the number of cents entered is valid
    if n < 0:
        return 'Cannot make change for 0 cents.'
    # setting the counter of ways
    num_ways = 0

    # creating a loop to iterate through each possibility (using +1 to account for range excluding the stop value)
    for nickels in range(n // 5 + 1):
        
        # calculating pennies by taking the inputted number and subracting it from the nickel total value
        pennies = n - (nickels * 5)

        # adding incrementally to the number of ways possible
        num_ways += 1

    # producing the final number of ways
    return num_ways

# creating an array of names per exercise
names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
# creating an array of respective scores per exercise
scores = np.array([99, 71, 85, 62, 91])

def lowest_scores(names, scores):
    """Creating a function that returns the name of the student with the lowest score"""

    # setting the score to the maximum possible value of 100
    score = 100
    # converting the array of names to a list
    names = names.tolist()
    # converting the array of scores to a list
    scores = scores.tolist()
    # creating an empty dictionary to build upon
    student_scores = {}

    # zipping the two lists to create a dictionary from the results
    for n, s in zip(names, scores):
        student_scores[n] = s
        
    # finding the student with the lowest score by iterating through the dictionary
    for a, b in student_scores.items():
        if b < score:
            score = b
            lowest_score = a

    # Returning the result being the student with the lowest score
    return(lowest_score)

# creating an array of names per exercise
names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
# creating an array of respective scores per exercise
scores = np.array([99, 71, 85, 62, 91])

def sort_names(names, scores):
    """Creating a function that sorts the students and their respective scores
    by descending order"""

    # converting the array of names to a list
    names = names.tolist()
    # converting the array of scores to a list
    scores = scores.tolist()
    # creating an empty list to build upon
    student_scores = []
    # zipping through the names and scores list to build upon the empty list
    for n, s in zip(names, scores):

        # appending the empty list with a tuple pair of the previous lists
        student_scores.append((n,s))

        # sorting the list by the second value of the tuple in descending order
        sorted_scores = sorted(student_scores, key=lambda item: item[1], reverse=True)

    # Returning the end result of a sorted list of tuples of pairs of the students and their scores
    return(sorted_scores)
