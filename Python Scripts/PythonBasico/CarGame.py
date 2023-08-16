
command= ""
started= False
#identação dando erro
while True:
 command=input(">").lower()

 if command == "start" and started==False: 
     if started == False:
      started= True
     print("Car started.....Ready to go!")
    # else:
       # start_cont= True 
 elif command == "start" and started==True: 
    print("Car já em movimento")
 elif command == "stop":
     if started == False:
        print("car já parado")
     else:
       print("Car stopped")
 elif command == "help":
     print("""
star - to start the car
stop - stop the car
quit - to quit
      """)
 elif command == "quit":
     break
 else:
     print("I don't undertand that...")



