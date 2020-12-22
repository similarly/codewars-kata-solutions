from itertools import cycle     # I didn't think too much about how do that other way, look further
                                # I just started learning and would appreciate your advice
def snail(array):

    if array == [[]]:
        return []

    def moveInDirection(coord1, coord2, dir, step=1):   # Функция движения по массиву
        coord1 += dir[0]*step   # Move through the massive - takes in starting point,
        coord2 += dir[1]*step   # direction as [x, y] (look at list higher) and number of steps
        return coord1, coord2

    iterDirection = cycle([[0,1],
                          [1,0],
                          [0,-1],
                          [-1,0]])
    size = len(array)
    i = 0   # Определяем начальную позицию | Defining a starting position
    j = 0
    turnPoint = [0, size-1]     # Первая поворотная точка | First turnpoint
    stepsToMove = size - 1      # Изначальное число шагов | Initial amount of steps
    resultList = [array[0][0]]
    direction = next(iterDirection)
    count = -2    # Это чтобы следить сколько надо пройти шагов | It's for tracking how much steps we need

    while stepsToMove:
        count += 1
        while [i, j] != turnPoint:
            i, j = moveInDirection(i, j, direction)    # Движение сквозь массив | Moving through our array
            resultList.append(array[i][j])

        if count % 2 and count > 0:        # Counting turns so steps get reduced every two of them
            stepsToMove -= 1               # Меняю длину пути | Changing how much to move in certain direction
        direction = next(iterDirection)    # Меняю направление | Changing direction
        turnPoint[0], turnPoint[1] = moveInDirection(turnPoint[0], turnPoint[1], direction, stepsToMove)

    return resultList
