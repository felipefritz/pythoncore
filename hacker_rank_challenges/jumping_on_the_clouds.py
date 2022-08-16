

def jumpingOnClouds(c):
    avoid = []
    jump = 0
    for i, cloud in enumerate(c):

        if cloud == 1:
            avoid.append(i)

        if i + 2 < len(c) and c[i + 2] == 0:
            jump += 1

    print(avoid)
    print(jump)
    return jump


c =[0, 0, 1, 0, 0, 1, 0]
jumpingOnClouds(c)