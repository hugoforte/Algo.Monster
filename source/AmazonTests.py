def isRobotBounded(instructions):
    gcount = 0
    lcount = 0
    rcount = 0
    for char in instructions:
        if char == "G":
            gcount += 1
        elif char == "R":
            rcount += 1
        elif char == "L":
            lcount += 1
    #if we have not moved, we are bounded by definition
    if gcount == 0:
        return True
    #if we have moved, we want to make sure we're not pointing north, if we are, we'll just continue moving north, any other direction will be back in 2 or 4 moves (2 for pointing south, 4 for east or west)
    if (rcount - lcount) % 4 == 0:
        return False
        
    return True

if __name__ == '__main__':
    res = isRobotBounded("GLRLLGLL")
    print(res)