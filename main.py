#12
import random

def generationListwithFunction(countElements):
    generationList = [random.randint(5, 1100) for i in range(countElements)]
    print(generationList)
generationListwithFunction(21)