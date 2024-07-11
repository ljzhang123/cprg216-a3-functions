SQFT_PER_GALLON = 350
COST_PER_GALLON = 42

def computeRectangleWallsArea():
    pass

def computeRectangleArea(length, width):
    pass

def computeSquareWallsArea():
    pass

def computeSquareArea(sideLength):
    pass

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
    pass

if __name__ == "__main__":
    roomCount = int(input("Welcome to Shiny Paint Company for indoor painting!\nHow many Rooms do you want to paint:"))
    print("Thank you!")
    computeRoomArea(roomCount)