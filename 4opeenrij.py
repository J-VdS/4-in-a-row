from tkinter import *
import time

class VOR:
    def __init__(self, tk):
        self.tk =  tk
        self.canvas = Canvas(self.tk, width=351, height=320, highlightthickness=0,\
                             bd=0)
        self.canvas.pack()
        
        self.veld = 'E'*42
        self.winnaar = None
        self.speler = 'A'
        self.color = {'A':'yellow', 'B':'red'}
        self.canvas.bind_all('<Button-1>', self.zet)
        self.extra()
        
        try:
            self.scherm()
            self.start()
        except Exception as e:
            print(e)
            self.tk.destroy()
        
    def scherm(self):
        for i in range(6):
            for j in range(7):
                self.canvas.create_rectangle(50*j, 50*i, 50*(j+1), 50*(i+1))
        self.tk.update()
        return

    def zet(self, evt):
        if self.winnaar:
            return
        x = (self.tk.winfo_pointerx() - self.tk.winfo_rootx())//50
        y = self.veld[x::7].count('E')-1
        if y < 0:
            return 
        self.veld = self.veld[:y*7+x]+self.speler+self.veld[y*7+x+1:]
        '''
        for i in range(6):
            print(self.veld[7*i:7*i+7])'''
        #tekent bolletje
        self.canvas.create_oval(50*x, 50*y, 50*(x+1), 50*(y+1), width=2, \
                                fill=self.color[self.speler])
        
        if self.win(self.speler):
            self.canvas.create_text(self.canvas.winfo_width()//2, 6*50,
                                    anchor='n', font=('Calibri',12),
                                    text='Player %s won!' %(self.speler))
            self.tk.update()
            self.winnaar = True
        self.speler = 'A' if (self.speler == 'B') else 'B'

    def win(self, speler):
        #horizontaal:
        for y in range(6):
            if self.veld[7*y:7*y+7].count(speler)>3:
                for x in range(4):
                    if self.veld[7*y+x:7*y+x+4] == speler*4:
                        return True
        #verticaal:
        for x in range(7):
            if self.veld[x::7].count(speler)>3:
                for y in range(3):
                    if self.veld[7*y+x:7*(y+4)+x:7] == speler*4:
                        return True
        #diagonaal linksonder naar rechtsboven
        for x in range(3,7):
            for y in range(3):
                if self.veld[7*y+x:7*y+x+19:6] == speler*4:
                    return True
        #diagonaal linksboven naar rechtsonder
        for x in range(4):
            for y in range(3):
                if self.veld[7*y+x:7*y+x+25:8] == speler*4:
                    return True

        return False
                

    def start(self):
        while 1:
            try:
                #self.pointer() #tekent pijltje boven kolom waar volgende zet zou komen
                self.tk.update()
                self.tk.update_idletasks()
            except Exception as e:
                return e
            time.sleep(0.1)
    
    def restart(self):
        pass
     
    def __str__(self):
        return (self.veld, self.speler)
    
    def extra(self):
        self.b1 = Button(self.tk, text='Restart', command=self.restart, 
                         font=('calibri', 8), width=7)
        self.b1.place(x=0, y=300)


if __name__ ==  '__main__':
    tk = Tk()
    tk.resizable(0,0)
    tk.title('4 op een rij')
    tk.update()
        
    spel = VOR(tk)
