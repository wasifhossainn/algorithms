import tkinter
from tkinter import *
from tkinter import PhotoImage
class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()


    

    def initialize(self):
        self.grid()

        
        self.img = PhotoImage(file='sick.gif')
        self.Lineartesting = PhotoImage(file='linear.gif')
        self.Binarytesting = PhotoImage(file='BINARYSEARCH.gif')
        self.Bubbletesting = PhotoImage(file='bubblesort.gif')
        self.Insertiontesting = PhotoImage(file='insertion.gif')
        self.Selectiontesting = PhotoImage(file='selection.gif')
        self.addtesting = PhotoImage(file='add.gif') 

        self.EnterarrayLabel = tkinter.Label(self, text="Entering Arrays", font=("Arial", 20), bg="#1E88E5")
        self.EnterarrayLabel.grid(column=1, row=1)

        self.SearchLabel = tkinter.Label(self, text="Search!", font=("Arial", 20), bg="#1E88E5")
        self.SearchLabel.grid(column=0, row=1)

        self.labelVariable = tkinter.StringVar()
        self.sortedentry = tkinter.Entry(self, textvariable=self.labelVariable)
        self.sortedentry.grid(column=1, row=3, ipadx=100, stick="W", padx=60)
        self.labelVariable.set("Array will appear here")
        
        self.entry = tkinter.Entry()
        self.entryVariable = tkinter.StringVar()
        self.entryVariable.set(u"Enter your array here")
        self.entry["textvariable"] = self.entryVariable
        self.entry.grid(column=1, row=2,  pady=20, ipadx=100, padx=60, sticky="W")
        self.entry.bind("<Return>", self.arraysort)

        
        self.numbertosearchVar = tkinter.StringVar()
        self.numbertosearch = tkinter.Entry(self, textvariable=self.numbertosearchVar)
        self.numbertosearch.grid(column=0, row=4, ipadx=50)
        self.numbertosearchVar.set("Enter the number you want to search")

        label = tkinter.Label(self, image=self.img, highlightthickness=0, borderwidth=0)
        label.grid(column=0, row=0, columnspan=5, stick="W", ipadx=0)

        self.SortLabel1 = tkinter.Label(self, text="Sort!", font=("Arial", 20), bg="#1E88E5")
        self.SortLabel1.grid(column=2, row=1)


        
        self.add1 = tkinter.Button(self, command=self.arraysort1, image=self.addtesting, borderwidth=0, highlightthickness=0)
        self.add1.grid(column=1, row=2, sticky="E", padx=10)

        self.BinaryButton = tkinter.Button(self, command=self.LinearSearch, image=self.Lineartesting, borderwidth=0, highlightthickness=0)
        self.BinaryButton.grid(column=0, row=2, pady=20, padx=10)

        self.LinearButton = tkinter.Button(self, command=self.BinarySearch, image=self.Binarytesting, borderwidth=0, highlightthickness=0)
        self.LinearButton.grid(column=0, row=3, pady=20, padx=10)

        self.BubbleButton = tkinter.Button(self, command=self.BubbleSort, image=self.Bubbletesting, borderwidth=0, highlightthickness=0)
        self.BubbleButton.grid(column=2, row=2, pady=20, padx=10)

        self.InsertionButton = tkinter.Button(self, command=self.InsertionSort, image=self.Insertiontesting, borderwidth=0, highlightthickness=0)
        self.InsertionButton.grid(column=2, row=3, pady=20, padx=100)

        self.SelectionButton = tkinter.Button(self, command=self.SelectionSort, image=self.Selectiontesting, borderwidth=0, highlightthickness=0)
        self.SelectionButton.grid(column=2, row=4, pady=20)

        self.SortEntryVar = tkinter.StringVar()
        self.SortEntry = tkinter.Label(self, textvariable=self.SortEntryVar)
        self.SortEntry.grid(column=2, row=5, ipadx=50)
        self.SortEntryVar.set("Your sorted list will appear here")
        

        
        self.numberinarrayVar = tkinter.StringVar()
        self.numberinarray = tkinter.Label(self, textvariable=self.numberinarrayVar, width=17)
        self.numberinarray.grid(column=0, row=5, ipadx=85)
        self.numberinarrayVar.set("Sorted Array will appear here")
        
        self.numberposition = tkinter.StringVar()
        self.numberpositionbox = tkinter.Label(self, textvariable=self.numberposition, width=17)
        self.numberpositionbox.grid(column=0, row=6, ipadx=85, pady=10)
        self.numberposition.set("Number Position In Array will appear here")

        self.geometry("1080x500")




    def arraysort1(self):
        try:
            array = self.entryVariable.get()
            arrayN = [int(n) for n in array.split(",")]
            self.labelVariable.set(arrayN)
        except ValueError:
            print("stub")

    def arraysort(self, event):
        try:
            array = self.entryVariable.get()
            arrayN = [int(n) for n in array.split(",")]
            self.labelVariable.set(arrayN)
        except ValueError:
            print("stub")
            
    def BinarySearch(self):
        try:
            array = self.entryVariable.get()
            arrayN = [int(n) for n in array.split(",")]
            arrayN = sorted(arrayN)
            self.labelVariable.set(arrayN)
            lower = 0
            upper = len(arrayN)-1
            found = False
            value = self.numbertosearchVar.get()            #Prompts user to enter a number to search for in the array
            while lower <= upper and found == False:
                middle = int((upper + lower)/2)                 #Calculates middle integer value and begins the search
                if arrayN[int(middle)] < int(value):
                    lower = middle + 1
                elif arrayN[int(middle)] > int(value):
                    upper = middle - 1
                else:
                    found = True

            if found:                                           #Displays the position of the number if it is in the array
                self.numberinarrayVar.set(arrayN)
                self.numberposition.set(middle)
            else:
                self.numberinarrayVar.set(arrayN)
                self.numberposition.set("The value is not in the array.")
        except ValueError:
            self.numberinarrayVar.set("Integers only")
            self.numberposition.set("Make sure all entries are filled")
                                    

    def LinearSearch(self):
        try:
            array = self.entryVariable.get()
            arrayN = [int(n) for n in array.split(",")]
            position = 0
            found = False
            item = self.numbertosearchVar.get()
            while position < len(arrayN) and found == False:
                if arrayN[int(position)] == int(item):
                    found = True
                elif found == False:
                    position = position + 1

            if found:
                self.numberinarrayVar.set(arrayN)
                self.numberposition.set(position)
            else:
                self.numberinarrayVar.set(arrayN)
                self.numberposition.set("The value is not in the array")
        except ValueError:
            self.numberinarrayVar.set("Integers only")
            self.numberposition.set("Make sure all entries are filled")
            

    def BubbleSort(self):
        try:
            array = self.entryVariable.get()
            arrayN = [int(n) for n in array.split(",")]
            found = True
            pointer = 0
            arlength = len(arrayN)-1
            while arlength > 0 and found:
                found = False
                for i in range(arlength):
                    if arrayN[i] > arrayN[i+1]:
                        found = True
                        temp = arrayN[i]
                        arrayN[i] = arrayN[i+1]
                        arrayN[i+1] = temp
                arlength = arlength-1
            self.SortEntryVar.set(arrayN)
        except ValueError:
            self.SortEntryVar.set("Anything that is not an integer is not accepted!")
            
    def InsertionSort(self):
        try:
            array = self.entryVariable.get()
            arrayN = [int(n) for n in array.split(",")]
            for index in range(1, len(arrayN)):
                
                currentvalue = arrayN[index]
                position = index
                
                while position > 0 and arrayN[position - 1] > currentvalue:
                    arrayN[position] = arrayN[position-1]
                    position = position - 1
                    
                arrayN[position] = currentvalue
                
            self.SortEntryVar.set(arrayN)
        except ValueError:
            self.SortEntryVar.set("Anything that is not an integer is not accepted!")

    def SelectionSort(self):
        try:
            array = self.entryVariable.get()
            arrayN = [int(n) for n in array.split(",")]
            for fillslot in range(len(arrayN)-1, 0, -1):
                positionOfMax = 0
                for location in range(1, fillslot+1):
                    if arrayN[location] > arrayN[positionOfMax]:
                        positionOfMax = location

                temp = arrayN[fillslot]
                arrayN[fillslot] = arrayN[positionOfMax]
                arrayN[positionOfMax] = temp

            self.SortEntryVar.set(arrayN) 
        except ValueError:
            self.SortEntryVar.set("Anything that is not an integer is not accepted!")
    

        
        

        

if __name__=="__main__":
    
    app = simpleapp_tk(None)
    app.title('Search Algorithms')
    app.mainloop
    app.configure(bg="#1E88E5")
        
'''https://www.tutorialspoint.com/python/tk_grid.htm Use for the GUI GUIDE'''
