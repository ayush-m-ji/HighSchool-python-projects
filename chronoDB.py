# chronoDB 
try:
    def write_data(name,percentage):
        with open("data.txt",'a') as f:
            f.write(f"{name}:{percentage}%\n")
        input("press Enter key to go menu ")        

    def read_all():
        with open("data.txt",'r') as f:      
            print (f.read())
        input("press Enter key to go menu ")

    def search_data():
        word = input ("Enter your key ")
        data = True
        line_no = 1

        with open ("data.txt", 'r') as f: 
            if (word in f.read()):
                with open ("data.txt", 'r') as f:
                    while data:            
                        data = f.readline()
                        if (word in data):
                            print (data)
                    line_no += 1
            else:
                print ("key are not exist in data.txt")                       
        input("press Enter key to go menu ")
                    
    def delete_data():
        
        User_say = input()
        if User_say == "area":
            starting = int(input("to: "))
            ending = int(input("from: "))

            with open("data.txt",'r') as f:
                data_list = f.read().split("\n")
                del data_list[starting-1:ending]
                data_list.pop(-1)               
                    
        else:
            num = int(User_say)
            with open("data.txt",'r') as f:
                data_list = f.read().split("\n")
                data_list.pop(num-1)
                data_list.pop(-1)

# rewrite in data.txt

        print ("done")   
        new_data = data_list       
        with open("data.txt", 'w') as f:
            for i in new_data:
                f.write(f"{i}\n")
        input("press Enter key to go menu ")

except Exception as e:
    print(e)


while True: 
    try:
        print ("1. Add data")
        print ("2. Search data")
        print ("3. Delete any data")
        print ("4. Read all data")
        print ("5. Exit")
        user_input = int(input("Enter the number to action "))
        
        if user_input == 1:
            print ("Enter you data")
            a = input("Name: ")
            b = input("Percentage: ")
            write_data(a,b)
        
        elif user_input == 2:
            search_data()

        elif user_input == 3:
            line_no = 0
            with open ("data.txt", "r") as f:
                data = f.read().split()
                for i in data:
                    line_no += 1
                    print (f"{line_no} {i}")
                    
            print ("delete any data in this list, with the use of line number")
            print ("and you can delete specific area of list, so you can enter 'area'")
            delete_data()

        elif user_input == 4:
            read_all()

        elif user_input == 5:
            print ("Thank you for visit")
            break

        else:
            print("please follow instructions")
            input("press Enter key to go menu ")

    except Exception as e:
        print (e)
        