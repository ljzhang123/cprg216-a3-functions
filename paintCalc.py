SQFT_PER_GALLON = 350
COST_PER_GALLON = 42

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
    pass

if __name__ == "__main__":
    roomCount = int(input("Welcome to Shiny Paint Company for indoor painting!\nHow many Rooms do you want to paint:"))
    print("Thank you!")
    computeRoomArea(roomCount)