SQFT_PER_GALLON = 350
COST_PER_GALLON = 42
SHAPE = {"1":"rectangular", "2":"square", "3":"custom"}

def computeRectangleWallsArea():
    length = float(input('input a the length of the rectangle wall in feet:\n')) #user to enter length
    width = float(input('input a the width of the rectangle wall in feet:\n')) #user to enter width
    height = float(input('input a the height of the rectangle wall in feet: \n')) #user to enter height

    Surface_Area = (2*computeRectangleArea(length, height))+(2*computeRectangleArea(width, height))
    return Surface_Area

def computeRectangleArea(x, y): # sorry i'm using x and y variable here because i used the length and with on above function
    area = x*y
    return area 

def computeSquareArea(sideLength):
    return sideLength ** 2
  
def computeSquareWallsArea():
    sideLength = float(input("Enter the length of one side of the room: "))
    return 4 * computeSquareArea(sideLength)

def computeWindowsDoorsArea():
    pass

def computeCustomWallsArea():
    pass

def computeGallons(area):
    pass

def computePaintPrice(area) -> float:
    pass

# Basically the main function, most inputs are asked for here, 
# and picking and choosing which functions are used
def computeRoomArea(roomCount: int):
    if roomCount == 0:
        return 0, 0, 0
    else:
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

    windowsDoorsArea = computeWindowsDoorsArea()
    paintArea = wallsArea - windowsDoorsArea
    paintVolume = paintArea / SQFT_PER_GALLON
    paintCost = paintVolume * COST_PER_GALLON

    print(f"\nFor Room: {computeRoomArea.count}, the area to be painted is {paintArea} square ft and will require {paintVolume:.2f} gallons to paint. This will cost the customer ${paintCost:.2f}\n")

    recursiveTotal = computeRoomArea(roomCount-1)
    
    totalPaintArea = paintArea + recursiveTotal[0]
    totalPaintVolume = paintVolume + recursiveTotal[1]
    totalPaintCost = paintCost + recursiveTotal[2]

    if computeRoomArea.count == roomCount:
        print(f"Area to be painted is {totalPaintArea} square ft and will require {totalPaintVolume:.2f} gallons to paint. This will cost the customer ${totalPaintCost:.2f}")

    return totalPaintArea, totalPaintVolume, totalPaintCost
    

if __name__ == "__main__":
    roomCount = int(input("Welcome to Shiny Paint Company for indoor painting!\nHow many Rooms do you want to paint:\n"))
    print("Thank you!")
    computeRoomArea.count = 0
    computeRoomArea(roomCount)