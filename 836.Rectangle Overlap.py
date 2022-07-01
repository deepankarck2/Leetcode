from traceback import print_tb


def sol(rect1, rect2):
    
    if(rect1[0]< rect2[0] < rect1[2]):
        if(rect1[1]< rect2[1] < rect1[3]):
            print(True)
    else:
        print(False)


sol([0,0,1,1],[1,0,2,1])