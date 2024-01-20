class todo:
    x=0
    list=[]
    def pr(self):
        print(" ")
        print(":::Your To Do List:::")
        print("Sno    task")
        for i in range(0,self.x):
            print(i+1," -- ",self.list[i])
    def add(self):
        
        s=input("enter task :")
        self.x=self.x+1
        self.list.append(s)
    def update(self):
        c=int(input("Enter task's no to be updated :"))
        v=input("Enter task to be updated:")
        self.list[c-1]=v
    def remove(self):
        c=int(input("Enter task's no to be removed :"))
        self.list.pop(c-1)
        self.x=self.x-1


obj=todo()
print("::: Create Your To Do List Here :::")
while True:
    print("")
    print("1-Add\n2-Update\n3-Remove")
    n=int(input("Enter Your choice:"))
    if(n==1):
        obj.add()
        obj.pr()
    elif(n==2):
        obj.update()
        obj.pr()
    elif(n==3):
        obj.remove()
        obj.pr()


    
