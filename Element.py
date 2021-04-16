import MapReader

class Element:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.max_x = None
        self.max_y = None
        self.maxMin()
        

    def moveUp(self):
        if self.pos_y > 0 and self.verifyMove([0, -1], self.pos_x, self.pos_y -1):
            oldPosY = self.pos_y
            self.pos_y -= 1
            self.moving(self.pos_x, oldPosY, self.pos_x, self.pos_y)
        
    def moveDown(self):
        if self.pos_y < self.max_y and self.verifyMove([0, 1], self.pos_x, self.pos_y + 1):
            oldPosY = self.pos_y
            self.pos_y += 1
            self.moving(self.pos_x, oldPosY, self.pos_x, self.pos_y)
        
    def moveRight(self):
        if self.pos_x < self.max_x[self.pos_y] - 1 and self.verifyMove([1, 0], self.pos_x + 1, self.pos_y):
            oldPosX = self.pos_x
            self.pos_x += 1
            self.moving(oldPosX, self.pos_y, self.pos_x, self.pos_y)
        
    def moveLeft(self):
        if self.pos_x > 0 and self.verifyMove([-1, 0], self.pos_x -1, self.pos_y):
            oldPosX = self.pos_x
            self.pos_x -= 1
            self.moving(oldPosX, self.pos_y, self.pos_x, self.pos_y)
        
    def maxMin(self):
        self.max_x = []
        map = MapReader.MapReader.getStaticMap()
        
        self.max_y = len(map) - 1
        
        for line in map:
            self.max_x.append(len(line))
        

    def moving(self, oldPosX, oldPosY, posX, posY):
        map = MapReader.MapReader.getStaticMap()

        # On remplace l'ancien charactere P par un espace
        oldTempString = map[oldPosY]
        oldTempString = [char for char in oldTempString]
        oldTempString[oldPosX] = ' '
        map[oldPosY] = ''.join(oldTempString)

        targetChar = 'P'

        import Box
        if type(self) == Box.Box:
            targetChar = 'X'

        # On place P à son nouvel emplacement
        newTempString = map[posY]
        newTempString = [char for char in newTempString]
        newTempString[posX] = targetChar
        map[posY] = ''.join(newTempString)

    def verifyMove(self, direction, posX, posY):
        map = MapReader.MapReader.arrayMap
        target = map[posY][posX]
        
        if target == 'X':
            if self.verifyMove(direction, posX + direction[0], posY + direction[1]):
                import Box
                box = Box.Box()
                if direction == [0, -1]:
                    box.moveUp()
                elif direction == [0, 1]:
                    box.moveDown()
                elif direction == [1, 0]:
                    box.moveRight()
                elif direction == [-1, 0]:
                    box.moveLeft()
                return True
            else:
                return False
        elif target != '#':
            return True
        else:
            return False
            
            


