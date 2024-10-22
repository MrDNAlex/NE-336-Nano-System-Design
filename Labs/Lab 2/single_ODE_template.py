#complete this file and submit for task 1
#name and student ID go here 

#import solve_ivp here using a suitable statement


#-----------------------
#--define const at top--
#-----------------------
#this is the space to define values such as x(t=10)=5 etc that you will use in all of your code


#---------------------
#-------Task 1.1------
#---------------------
 
#define your function (ode_fun_1) for the ODE dxdt=beta*x * sin(beta*t) by entering the value for beta in the equation

#define ode_fun_1 here 




#solve the ode and call the solution sol1


#plot x vs t for all t values with a suitable label



#---------------------
#-------Task 1.2------
#---------------------
#find the value of x at t=15 by using commands in code (not just reading from graph)

#write a print statement here to show the value of x at t=15 using the command you find


#---------------------
#-------Task 1.3------
#---------------------
#write your ode as a function that now takes three arguments with beta being the last one. 
#call this ode_fun_2


#solve this ODE for beta= 2 by using the args optional argument in solve_ivp


#plot x vs t for all t values with a suitable label in a new figure



#---------------------
#-------Task 1.4------
#---------------------
#use the ode function you developed in the previous task to now solve for a range of beta values
#plot the results for all values of beta=[2,4,6,8] on the same figure. 

#Bonus: include labels to show the value of beta for each solution being plotted