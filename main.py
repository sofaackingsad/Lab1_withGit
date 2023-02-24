#12
import random
def generationListwithFunction(countElements):
    generationList = []
    for i in range(countElements):
        generationList.append(random.randint(5, 1100))
    print(generationList)
generationListwithFunction(5)


