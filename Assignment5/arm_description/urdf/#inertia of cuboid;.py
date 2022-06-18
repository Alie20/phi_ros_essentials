#inertia of cuboid;

def inertia(mass,width,height,depth):
    Ixx = (1/12)*(mass)*(height**2+depth**2)
    Iyy = (1/12)*(mass)*(height**2+width**2)
    Izz = (1/12)*(mass)*(width**2+height**2)
    print(f"Ixx:{Ixx}     Iyy:{Iyy}    Izz:{Izz}")

def main():
    inertia (10,1,1,0.2)
    inertia(1,1,0.5,0.1)
    
if __name__ =="__main__":
    main()