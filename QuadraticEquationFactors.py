import numpy

def CheckFactors_Quadratic(a,b,c, reach):
    # factorsFound = False
    right_i = 0
    right_j = 0
    for i in numpy.arange(0,reach+1,0.1):
        for j in numpy.arange (0, reach+1, 0.1):
            # print (j)
            if i+j == b and i*j == a*c:
                # factorsFound = True;
                right_i = i
                right_j = j
    print (right_i)
    print (right_j)


CheckFactors_Quadratic(1,2.1,1.1, 100)


# for i in numpy.arange(0,1,0.1):
#     print (i)

#
# print (1.1+1.2)
# print (1.1*1.2)
# for i in numpy.arange(1,2,0.1):
#         for j in numpy.arange (1,2, 0.1):
#             print("SOMA: ", i+j)
#             print("MULTI: ", i*j)
