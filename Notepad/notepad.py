from tkinter import * 
from tkinter import filedialog
from tkinter.messagebox import * 
import os


class Notepad_GUI:
	root = Tk()				#creating root frame
	__thisWidth = 300			#size of window
	__thisHeight = 300
	__TextArea = Text(root, wrap= WORD)
	__MenuBar = Menu(root)			#creating menubar with file,edit,help items		
	__FileMenu = Menu(__MenuBar, tearoff=0) 
	__EditMenu = Menu(__MenuBar, tearoff=0)
	__HelpMenu = Menu(__MenuBar, tearoff=0)
	__ScrollBar = Scrollbar(__TextArea)	#creating scrollbar over TextArea
	__file = None
	
	def __init__(self):
		
		self.root.title("Untitled-Notepad")
                self.root.geometry(f"{self.__thisWidth}x{self.__thisHeight}") 
		self.root.grid_rowconfigure(0, weight=1) 
		self.root.grid_columnconfigure(0, weight=1)

		self.__TextArea.grid(sticky = N + E + S + W) 
		self.__FileMenu.add_command(label="New", command=self.__newFile)     #adding subitems to MenuBar Options
		self.__FileMenu.add_command(label="Open", command=self.__openFile)
		self.__FileMenu.add_command(label="Save", command=self.__saveFile)
		self.__FileMenu.add_separator()                                          
		self.__FileMenu.add_command(label="Exit", command=self.__quitApplication)
		self.__MenuBar.add_cascade(label="File", menu=self.__FileMenu)
		
		self.__EditMenu.add_command(label="Cut", command=self.__cut)
		self.__EditMenu.add_command(label="Copy", command=self.__copy)
		self.__EditMenu.add_command(label="Paste", command=self.__paste)
		self.__FileMenu.add_separator()                                          
		self.__MenuBar.add_cascade(label="Edit", menu=self.__EditMenu)
		
		self.__HelpMenu.add_command(label="About Notepad", command=self.__showAbout)                                     
		self.__MenuBar.add_cascade(label="Help", menu=self.__HelpMenu)
		
		self.root.config(menu=self.__MenuBar)		#setting the MenuBar
		self.__ScrollBar.pack(side=RIGHT,fill=Y)	#setting the ScrollBar
		self.__ScrollBar.config(command=self.__TextArea.yview)      
		self.__TextArea.config(yscrollcommand=self.__ScrollBar.set)
		

class Functions(Notepad_GUI):	#defining functionalities of MenuBar items
	
	def __openFile(self): 
		self.__file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")]) 
  
		if self.__file == "": 
			# no file to open 
			self.__file = None
		else: 
			# Try to open the file 
			# set the window title 
			self.root.title(os.path.basename(self.__file) + " - Notepad") 
			self.__TextArea.delete(1.0,END) 
			file = open(self.__file,"r") 
			self.__TextArea.insert(1.0,file.read()) 
			file.close() 
  
	def __newFile(self): 
		self.root.title("Untitled - Notepad") 
		self.__file = None
		self.__TextArea.delete(1.0,END) 
  
	def __saveFile(self): 
		if self.__file == None: 
			# Save as new file 
			self.__file = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")]) 
			if self.__file == "": 
				self.__file = None
			else: 
				# Try to save the file 
				file = open(self.__file,"w") 
				file.write(self.__TextArea.get(1.0,END)) 
				file.close() 
                  
				# Change the window title 
				self.root.title(os.path.basename(self.__file) + " - Notepad") 
		else: 
			file = open(self.__file,"w") 
			file.write(self.__TextArea.get(1.0,END)) 
			file.close() 
  
	def __quitApplication(self):
		self.root.destroy()
		
	
	def __cut(self): 
		self.__TextArea.event_generate("<<Cut>>") #using Tkinter event binding for cut, copy and paste 
  
	def __copy(self): 
		self.__TextArea.event_generate("<<Copy>>") 
  
	def __paste(self): 
		self.__TextArea.event_generate("<<Paste>>") 
		
	def __showAbout(self):
		showinfo("Notepad",f"Amit Bora \nGUI learning ")	
  
	def run(self): 
		# Run main application 
		self.root.mainloop() 
		
def main():
	notepad = Functions() 
	notepad.run()	

from notepad import main

if __name__ == "__main__":
	main()
else:
	pass
