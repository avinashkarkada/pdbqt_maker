from tkinter import *
import os


root = Tk()
root.title("VS ligand converter")
root.geometry("400x200")




Checkbutton1 = IntVar()  
Checkbutton2 = IntVar() 
Checkbutton3 = IntVar()


Button1 = Checkbutton(root, text = "Convert sdf", variable = Checkbutton1)
Button1.pack()  

Button2 = Checkbutton(root, text = "Convert pdb", variable = Checkbutton2)
Button2.pack()

Button3 = Checkbutton(root, text = "Convert mol2", variable = Checkbutton3)
Button3.pack()

def run():
	if Checkbutton1.get() == 1:
		os.popen("obabel *.sdf -opdbqt -m")
	elif Checkbutton2.get() == 1:
		os.popen("obabel *.pdb -opdbqt -m")
	elif Checkbutton3.get() == 1:
		os.popen("obabel *.mol2 -opdbqt -m")
	else:
		print("Error selection")


run_button = Button(root, text = "Convert ", command = run)
run_button.pack()


root.mainloop()

