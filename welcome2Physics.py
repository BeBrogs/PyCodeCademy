#PYTHON CODECADEMY: 'Getting ready for physics class'

train_mass = 22680
train_acceleration = 10
train_distance = 100

#Calculating newtons of force behind a GE train 
def get_force(mass, accelaration):
  force = mass*accelaration
  return force

train_force=get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force. \n")


#c = constant aka the speed of light, which is roughly 3 x 10^8
c = 3*10**8
bomb_mass = 1

def get_energy(mass, c):
  result = mass * (c**2)
  return result

bomb_energy = get_energy(bomb_mass, c)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.\n")


#Defining 'Work' - Force multiplied by distance
def get_work(mass, acceleration, distance):
  result = get_force(mass, acceleration)
  return result
  
train_work=get_work(train_mass, train_acceleration, train_distance)

print(train_work)

#Function which returns celsius translation of fareinheit input
def f_to_c(f_temp):
  c_temp = (f_temp -32) * (5/9)
  return c_temp

#Variable equal to returned value based on f 100
f100_in_celsius = f_to_c(100)
print("100 Fareinheit to celsius is: ")
print(str(f100_in_celsius)+" Celsius \n")


#Function which returns farenheit translation of celsius input
def c_to_f(c_temp):
  f_temp=(c_temp*9/5) + 32
  return f_temp

#Variable equal to returned value based on c 0
c0_in_farenheit = c_to_f(0)
print("0 celsius to fareinheit is: ")
print(str(c0_in_farenheit)+" Fareinheit\n")
