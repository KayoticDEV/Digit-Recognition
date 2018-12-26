import tkinter
import threading

class XYZ(threading.Thread):
    top = tkinter.Tk()
    i = 0;

    def helloCallBack(self):
        while True:
            print (self.i)
            self.i+=1
            
        
    def callFunction(self):
        t = threading.Thread(target=self.helloCallBack)
        t.start()
        

    def makeButton(self):
        B = tkinter.Button(self.top, text ="Hello", command = self.callFunction)
        B.pack()

gui = XYZ()
gui.makeButton()
gui.top.mainloop()
