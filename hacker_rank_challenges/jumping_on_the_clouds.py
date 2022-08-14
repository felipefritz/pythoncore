

def jumpingOnClouds(c):
    avoid = []
    jump = 0
    for i, cloud in enumerate(c):

        if cloud == 1:
            avoid.append(i)
        else:
            jump += 1

    print(avoid)
    print(jump)
    return jump


c =[0, 0, 1, 0, 0, 1, 0]
jumpingOnClouds(c)