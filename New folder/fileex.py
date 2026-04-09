import pickle
def WriteStudents(records):
    with open("Students.dat" "wb") as file:
       for i in records:
         pickle.dump(i,file)

def ReadStudents():
    try:
         with open("Students.dat" "rb") as file2:
          while True:

            try:
                readrecord = pickle.load(file2)
                print(readrecord.name,readrecord.grade)
            except EOFError:
                 break
    except IOError:
       print("There is no file to be read")





def SaveAnimalsToFile(animals_array,filename):
    try:
        with open("animals.txt" "w") as f:
            for X in animals_array:
                f.write(X +"\n")
    except IOError:
        print("file could not be accesed")
    

    animal_array = ["Lion", "Tiger", "Elephant", "Zebra"]
    SaveAnimalsToFile(animal_array,animals.txt)