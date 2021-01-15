"""
FROM: https://en.wikipedia.org/wiki/Tower_of_Hanoi#Iterative_solution

For an even number of disks:

    make the legal move between pegs A and B (in either direction),
    make the legal move between pegs A and C (in either direction),
    make the legal move between pegs B and C (in either direction),
    repeat until complete.

For an odd number of disks:

    make the legal move between pegs A and C (in either direction),
    make the legal move between pegs A and B (in either direction),
    make the legal move between pegs B and C (in either direction),
    repeat until complete.

In each case, a total of 2n − 1 moves are made. 
"""
def sortedarray(array, size):
    if(n == 0 or n == 1):
        return true
    
    for i in range(1,size):
        if(array[i-1] > array[i]):
            return False
    return True

def printTowers():
    print("\nTower A: ",Tower_A)
    print("Tower B: ",Tower_B)
    print("Tower C: ",Tower_C, "\n")
    return

n = input("\nHow many disks do you want to have?: ")
n = int(n)
number_of_moves = pow(2,n) #calculate number of moves needed.

Tower_A = []
Tower_B = []
Tower_C = []

#Populate Tower_One:
for index in range(n):
    Tower_A.append(n - index)

#for loop for tower of Hanoi:
if(n % 2 == 0): #even number of disks
    for index in range(number_of_moves):

        #make the legal move between pegs A and B (in either direction
        if(Tower_A and not Tower_B):
            disk = Tower_A[len(Tower_A) -1]
            Tower_A.pop()
            Tower_B.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower A to Tower B.\n")

        elif not Tower_A and Tower_B:
            disk = Tower_B[len(Tower_B) -1]
            Tower_B.pop()
            Tower_A.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower B to Tower A.\n")

        elif Tower_A[len(Tower_A) -1] < Tower_B[len(Tower_B) -1] :
            disk = Tower_A[len(Tower_A) -1]
            Tower_A.pop()
            Tower_B.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower A to Tower B.\n")

        elif Tower_A[len(Tower_A) -1] > Tower_B[len(Tower_B) -1] :
            disk = Tower_B[len(Tower_B) -1]
            Tower_B.pop()
            Tower_A.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower B to Tower A.\n")


        
        #make the legal move between pegs A and C (in either direction)
        if (Tower_A and not Tower_C):
            disk = Tower_A[len(Tower_A) -1]
            Tower_A.pop()
            Tower_C.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower A to Tower C.\n")

        elif not Tower_A and Tower_C:
            disk = Tower_C[len(Tower_C) -1]
            Tower_C.pop()
            Tower_A.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower C to Tower A.\n")

        elif Tower_A[len(Tower_A) -1] < Tower_C[len(Tower_C) -1] :
            disk = Tower_A[len(Tower_A) -1]
            Tower_A.pop()
            Tower_C.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower A to Tower C.\n")

        elif Tower_A[len(Tower_A) -1] > Tower_C[len(Tower_C) -1] :
            disk = Tower_C[len(Tower_C) -1]
            Tower_C.pop()
            Tower_A.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower C to Tower A.\n")

        #make the legal move between pegs B and C (in either direction)
        if (Tower_B and not Tower_C):
            disk = Tower_B[len(Tower_B) -1]
            Tower_B.pop()
            Tower_C.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower B to Tower C.\n")

        elif not Tower_B and Tower_C:
            disk = Tower_C[len(Tower_C) -1]
            Tower_C.pop()
            Tower_B.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower C to Tower B.\n")

        elif Tower_B[len(Tower_B) -1] < Tower_C[len(Tower_C) -1] :
            disk = Tower_B[len(Tower_B) -1]
            Tower_B.pop()
            Tower_C.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower B to Tower C.\n")

        elif Tower_B[len(Tower_B) -1] > Tower_C[len(Tower_C) -1] :
            disk = Tower_C[len(Tower_C) -1]
            Tower_C.pop()
            Tower_B.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower C to Tower B.\n")

        #sorting completed
        if( sortedarray(Tower_C,len(Tower_C)) and not Tower_A and not Tower_B):
            print("\nHanoi Completed!\n")
            printTowers()
            break

        
else: #odd number of disks
    for index in range(number_of_moves):

        #make the legal move between pegs A and C (in either direction)
        if (Tower_A and not Tower_C):
            disk = Tower_A[len(Tower_A) -1]
            Tower_A.pop()
            Tower_C.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower A to Tower C.\n")

        elif not Tower_A and Tower_C:
            disk = Tower_C[len(Tower_C) -1]
            Tower_C.pop()
            Tower_A.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower C to Tower A.\n")

        elif Tower_A[len(Tower_A) -1] < Tower_C[len(Tower_C) -1] :
            disk = Tower_A[len(Tower_A) -1]
            Tower_A.pop()
            Tower_C.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower A to Tower C.\n")

        elif Tower_A[len(Tower_A) -1] > Tower_C[len(Tower_C) -1] :
            disk = Tower_C[len(Tower_C) -1]
            Tower_C.pop()
            Tower_A.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower C to Tower A.\n")


        #make the legal move between pegs A and B (in either direction)
        if(Tower_A and not Tower_B):
            disk = Tower_A[len(Tower_A) -1]
            Tower_A.pop()
            Tower_B.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower A to Tower B.\n")

        elif not Tower_A and Tower_B:
            disk = Tower_B[len(Tower_B) -1]
            Tower_B.pop()
            Tower_A.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower B to Tower A.\n")

        elif Tower_A[len(Tower_A) -1] < Tower_B[len(Tower_B) -1] :
            disk = Tower_A[len(Tower_A) -1]
            Tower_A.pop()
            Tower_B.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower A to Tower B.\n")

        elif Tower_A[len(Tower_A) -1] > Tower_B[len(Tower_B) -1] :
            disk = Tower_B[len(Tower_B) -1]
            Tower_B.pop()
            Tower_A.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower B to Tower A.\n")

        #make the legal move between pegs B and C (in either direction)
        if (Tower_B and not Tower_C):
            disk = Tower_B[len(Tower_B) -1]
            Tower_B.pop()
            Tower_C.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower B to Tower C.\n")

        elif not Tower_B and Tower_C:
            disk = Tower_C[len(Tower_C) -1]
            Tower_C.pop()
            Tower_B.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower C to Tower B.\n")

        elif Tower_B[len(Tower_B) -1] < Tower_C[len(Tower_C) -1] :
            disk = Tower_B[len(Tower_B) -1]
            Tower_B.pop()
            Tower_C.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower B to Tower C.\n")

        elif Tower_B[len(Tower_B) -1] > Tower_C[len(Tower_C) -1] :
            disk = Tower_C[len(Tower_C) -1]
            Tower_C.pop()
            Tower_B.append(disk)
            printTowers()
            print("\nMoved ", disk, " from Tower C to Tower B.\n")

        #sorting completed
        if( sortedarray(Tower_C,len(Tower_C)) and not Tower_A and not Tower_B):
            print("\nHanoi Completed!\n")
            printTowers()
            break
