#Introduction to the user
print ('\nWelcome to the flightplanner \n')

#Imports time for UNIX-execution time
import time

#Ask for the name of the flightplanner. This is also the name of the .txt 
fp_name = input("Enter the name of the flightplanner: ")
if len(fp_name) <= 0:
    print("Error: You need to give the flightplanner a name")
print("The flighplanner name is: " + str(fp_name))

#Ask for the number of timers
timers = input("How many timers do you want to make? ")
if len(fp_name) <= 0:
    print("Error: You have to state a number")
print("The number of timers are: " + str(timers))

timers = int(timers)
indexes = []
for i in range(timers):
    #Ask for the timer name. If the timer name has length of 0, it gives an error.
    #The timer name will be printed afterwards
    timer_name = input("Enter the name of the timer: ")
    if len(timer_name) <= 0:
        print ("Error: You have to give your timer a name")
    print ("The timer name is: " +str(timer_name))


    #Ask for the command you want to execute. Gives an error if length = 0.
    #Will print what the typed command is.
    command = input("Enter the command you want to execute: ")
    if len(command) <=0:
        print("Error: You have to enter a command")
    print ("The command is: " +str(command))

    #Ask if you want you timer to be active or dormant. Does not quite work yet.
    #Checks that if length = 0, prints an error.
    #Should print active or dormant and set the state depending on the answer.
    state = input("Enter the state of the timer. Active is 0 and dormant is 1.: ")
    if len(state) <= 0:
        print("Error: You have to enter whether the timer is active or dormant")
    if state is ('0'):
        print ("The state is active")
    if state is ('1'):
        print ("The state is dormant")

    #Ask for the UNIX execution time. Will go back to asking
    #if the time is before present time or further than 2 weeks into the future
    execution_time=1
    while ((float(execution_time) < (time.time())) or (float(execution_time) > (time.time())+1.2e6)):    
        execution_time = input("When do you want to execute your command? Please enter UNIX-timestamp: ")
        if len(execution_time) <=0:
            print("Error: You have to set a UNIX-time")
        if (time.time()) < float(execution_time) < (time.time())+1.2e6:
            print("The execution time is valid. The time is "+ time.ctime(float(execution_time)))
        elif(float(execution_time) < (time.time())):
            print("Error: The execution time is in the past. The time is "+ time.ctime(float(execution_time)))
        elif(float(execution_time) > (time.time())+1.2e6):
            print("Error:The execution time is more than 2 weeks into the future. The time is "+ time.ctime(float(execution_time)))

    #Ask for repitions
    repeats = input("How many repitions do you want to execute? ")
    if float(repeats) < 1:
        print("Error: You need to have at least 1 repition")

    indexes.append(timer_name +',' + command+',' + state +',' + str(0)+',' + str(0)+',' + str(0)+',' + execution_time+',' + str(0)+',' + repeats + '\n')
    print("\nOn to the next timer! \n")

#Creates a file with the flightplan name.I want to have it save the inputs
#like:<timer_name>,<command>,<state>,0,0,0,<execution_time>,0,<repeats>
indexes[-1]=indexes[-1][:-1]
f=open('%s.txt' % fp_name,'w')
for i in range(timers):
    f.write(indexes[i])
f.close()
print("The flightplanner file named %s has been saved to the directory \n" % fp_name)
    
