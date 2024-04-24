class star_cinema:
    _hall_list=[]
    
    def entry_hall(self,hall):
        self._hall_list.append(hall)
        

class hall(star_cinema):
    def __init__(self,name,rows,cols,hall_no):
        self.seat={}
        self.name=name
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        super().__init__()
        self.entry_hall(self)
        
    def entry_show(self,id,moviname,time):
        self.__id=id
        self.moviname=moviname
        self.time=time
        x=(self.__id,self.moviname,self.time)
        self.show_list.append(x)
        self.seat[self.__id]=[[0 for i in range(self.cols)] for j in range(self.rows)]

    def book_seat(self,id,row,col):
        f=0
        for i in range(len(self.show_list)):
            if self.show_list[i][0]==id:
                f=1
                break
        if f==1:
            if self.seat[id][row][col]!=1:
                self.seat[id][row][col]=1
                print("successfully seat booked")
            else:
                print("already booked")

        else:
            print("Wrong Id")

        

    def view_show_list(self):
        for i in range(len(self.show_list)):
            print("\t",*self.show_list[i])
        return ""

    def show_available_seat(self,id):
        for i in range(len(self.seat[id])):
            print("\t",self.seat[id][i])
        return ""
    

x=hall("MO",5,5,2)
x.entry_show("009","MOVI: jawan","TIME: 2:30 PM")
x.entry_show("113","MOVI: ninu kuri","TIME: 3:00 PM")



while(True):
    print("\t.....WELCOME TO CINEMA HALL.....")
    print("\t1.VIEW ALL SHOW TODAY\n\t2.VIEW ALL AVAILABLE SEAT\n\t3.BOOK TICKET\n\t4.EXIT")
    op =int(input("\tOption :"))
    if op==1:
        print(x.view_show_list())

    elif op==2:
        id=input("movi id:")
        print(x.show_available_seat(id))
    elif op==3:
        id=input("movi id : ")
        num=int(input("number of ticket :"))
        for i in range(num):
            row=int(input("row :"))
            col=int(input("col :"))
            if row>x.rows-1 or col>x.cols-1:
                print("INVLAID ROW AND COL")
            else:
                x.book_seat(id,row,col)
            
            
        

    elif op==4:
        break




        
    

        




    


