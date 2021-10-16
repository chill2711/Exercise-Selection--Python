#Cole Hill, Nate Manning
#CPSC 1301
#We Solve it Project
#Dr. Carroll
#May 12, 2020

#welcome function
def welcome():
    print("Welcome to our Exercise Selection Program!")


#selection of indoor/outdoor function
def IndoorOutdoor():
    while True:
        exerciseChoice=input("Enter 'I' for Indoor Exercise, 'O' for Outdoor Exercise, or 'Q' to quit:")
        if exerciseChoice=='I':
            break
        elif exerciseChoice=='O':
            break
        elif exerciseChoice=='Q':
            break
        else:
            print(f"{exerciseChoice} is not a valid option")
    return exerciseChoice

def Indoor(exerciseChoice):
    if exerciseChoice=='I':
        print("""Your options are:
1. Gym Membership
2. Indoor Courts
3. Exercise Class""")

        choice=input("Please choose a number between 1-3 based on the activity you want to do:")
        while choice!='1' and choice!='2' and choice!='3':
            print(f"Sorry, {choice} is not a valid option")
            choice=input("Please choose a number between 1-3 based on the activity you want to do:")
        if choice=='1':
            GymMembership()
        if choice=='2':
            IndoorCourt()
        if choice=='3':
            ExerciseClasses()
            
    if exerciseChoice=='O':
        print("""Your options are:
1. Hiking/Jogging Trails
2. Golf Courses
3. Outdoor Facilities""")
        choice=input("Please choose a number between 1-3 based on the activity you want to do:")
        while choice!='1' and choice!='2' and choice!='3':
            print(f"Sorry, {choice} is not a valid option")
            choice=input("Please choose a number between 1-3 based on the activity you want to do:")
        if choice=='1':
            HikingJogging()
        if choice=='2':
            GolfCourses()
        if choice=='3':
            OutdoorFacilities()

        
                
#Gym membership file function
def GymMembership():
    try:
        file=open("Gym.txt")
        hello=file.read()
        print(hello)
        file.close()
    except FileNotFoundError:
        print("Unable to open file")
 
    
    

#Indoor Court File Function
def IndoorCourt():
    try:
        file=open("IndoorCourts.txt",'r')
        hello=file.read()
        print(hello)
        file.close()
    except FileNotFoundError:
        print("Unable to open file")


#Exercise classes function
def ExerciseClasses():
    try:
        file=open("ExerciseClasses.txt",'r')
        hello=file.read()
        print(hello)
        file.close()
    except FileNotFoundError:
        print("Unable to open file")
 



#Hiking/Jogging Trail Function
def HikingJogging():
    try:
        file=open("HikingJoggingTrails.txt",'r')
        hello=file.read()
        print(hello)
        file.close()
    except FileNotFoundError:
        print("Unable to open file")



#Golf Course Function
def GolfCourses():
    try:
        file=open("GolfCourses.txt",'r')
        hello=file.read()
        print(hello)
        file.close()
    except FileNotFoundError:
        print("Unable to open file")

    
#Outdoor Facilities Function
def OutdoorFacilities():
    try:
        file=open("OutdoorFacilities.txt",'r')
        hello=file.read()
        print(hello)
        file.close()
    except FileNotFoundError:
        print("Unable to open file")
    

#main function
def main():
    welcome()
    while True:
        exerciseChoice=IndoorOutdoor()
        if exerciseChoice=='Q':
            print("Stay Safe!")
            break
        Indoor(exerciseChoice)



#call main function
main()
