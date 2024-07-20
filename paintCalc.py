SQFT_PER_GALLON = 350
COST_PER_GALLON = 42
SHAPE = {"1":"rectangular", "2":"square", "3":"custom"}

def computeRectangleWallsArea():
    length = float(input('Enter the length of the room in feet:\n')) #user to enter length
    width = float(input('Enter the width of the room in feet:\n')) #user to enter width
    height = float(input('Enter the height of the room in feet: \n')) #user to enter height

    Surface_Area = (2*computeRectangleArea(length, height))+(2*computeRectangleArea(width, height))
    return Surface_Area

def computeRectangleArea(x, y): # sorry i'm using x and y variable here because i used the length and with on above function
    area = x*y
    return area 

def computeSquareArea(sideLength):
    return sideLength ** 2
  
def computeSquareWallsArea():
    sideLength = float(input("Enter the length of one side of the room:\n"))
    return 4 * computeSquareArea(sideLength)

def computeWindowsDoorsArea():
    #asks the user to enter the number of windows and doors in a room
    numWindowsandDoors = int(input("How many windows and doors does the room contain?\n"))
    totalAreaWinDoor = 0

    #asks the user for the length and width of each door/window, and calculates the sum of areas of all doors and windows in the room
    for i in range(numWindowsandDoors):
        lengthWinDoor = float(input("Enter window/door length for window/door {} in feet \n".format(i+1)))
        widthWinDoor = float(input("Enter window/door width for window/door {} in feet \n".format(i+1)))
        totalAreaWinDoor += lengthWinDoor * widthWinDoor

    return totalAreaWinDoor


def computeCustomWallsArea():
    #asks the user to enter the number of walls in the room
    numWalls = int(input("How many walls are there in the room? \n"))
    totalAreaWalls = 0

    #asks for height and length of each wall in order to calculate the room area, then returns room area
    for i in range(numWalls):
        heightWall = float(input(f"Enter the height of wall {i+1} in feet\n"))
        lengthWall = float(input(f"Enter the length of wall {i+1} in feet\n"))
        totalAreaWalls += heightWall * lengthWall
    return totalAreaWalls


def computeGallons(area) -> float:
    return area / SQFT_PER_GALLON

def computePaintPrice(area) -> float:
    volume = computeGallons(area)
    return volume * COST_PER_GALLON

# main loop
def computeRoomArea(roomCount: int):
    # if case is computeRoomArea(0), start backtracking up
    if roomCount == 0:
        return 0, 0, 0
    else:
    # increment the function call count by 1 otherwise
        computeRoomArea.count += 1
    
    print(f"Room: {computeRoomArea.count}")
    shapeSelection = input("Select the shape of the room:\n1 - Rectangular\n2 - Square\n3 - Custom (more or less than 4 walls, all square or rectangles)\n")
    roomShape = SHAPE[shapeSelection]
    
    wallsArea = 0
    if roomShape == "rectangular":
        wallsArea = computeRectangleWallsArea()
    elif roomShape == "square":
        wallsArea = computeSquareWallsArea()
    elif roomShape == "custom":
        wallsArea = computeCustomWallsArea()

    # get paint area, volume, and cost of this room
    paintArea = wallsArea - computeWindowsDoorsArea()
    paintVolume = computeGallons(paintArea)
    paintCost = computePaintPrice(paintArea)

    print(f"\nFor Room: {computeRoomArea.count}, the area to be painted is {paintArea} square ft and will require {paintVolume:.2f} gallons to paint. This will cost the customer ${paintCost:.2f}\n")

    # continue to calculate the remaining rooms with computeRoomArea(n-1)
    recursiveTotal = computeRoomArea(roomCount-1)
    
    # add the accumulated totals from each lower depth function calls
    totalPaintArea = paintArea + recursiveTotal[0]
    totalPaintVolume = paintVolume + recursiveTotal[1]
    totalPaintCost = paintCost + recursiveTotal[2]

    # print the final house totals if # of function calls is equal to number of rooms
    if computeRoomArea.count == roomCount:
        print(f"Area to be painted is {totalPaintArea} square ft and will require {totalPaintVolume:.2f} gallons to paint. This will cost the customer ${totalPaintCost:.2f}")

    # return the accumulated totals for passing back to previous function calls
    return totalPaintArea, totalPaintVolume, totalPaintCost
    

if __name__ == "__main__":
    roomCount = int(input("Welcome to Shiny Paint Company for indoor painting!\nHow many Rooms do you want to paint:\n"))
    print("Thank you!")
    computeRoomArea.count = 0
    computeRoomArea(roomCount)