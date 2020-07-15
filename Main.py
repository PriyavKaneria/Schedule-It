from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import datetime
import threading
import os.path
import calendar
import os, stat

loginval = False
schoolgo = False
coaching = False  # same as tuitions
coachinghrs = 0
checktime = False
dark=False

#For backgroud Timer to continously check time
class ThreadingEx(object):

	def __init__(self, interval=1):
		self.interval = interval
		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True
		thread.start()

	def run(self):
		global hnow, mnow, dnow, ampmnow, checktime, droot, Time__Interval, somlabel1,first, start
		while True:
			cur = datetime.datetime.now()
			curday = cur.day
			curhr = cur.hour
			curmin = cur.minute
			# print(curday,'     ',curhr,'      ',curmin)
			dnow = calendar.day_name[cur.weekday()]
			if checktime:
				mnow = curmin
				if curhr > 12:
					curhr -= 12
					ampmnow = 1  # PM
					hnow = curhr
				elif curhr ==12:
					curhr=12
					ampmnow = 0
					hnow = curhr
				else:
					hnow = curhr
					ampmnow = 0  # AM
				# print(dnow, '   ', hnow, '   ', mnow, '    ', ampmnow)
				for i in Time__Interval[:-1]:
					l1=i.split('-')
					l2=l1[0].split(':')
					l3=l1[1].split(':')
					if l2[1].split()[1]=='PM':
						ampmthen=1
					else:
						ampmthen=0
					if int(l2[0])==12:
						l2[0]=0
					if len(str(l2[0]))==1:
						l2[0]=str(0)+str(l2[0])
					if len(str(l2[1].split()[0]))==1:
						l2[0]=str(0)+str(l2[0])
					if len(str(hnow))==1:
						hnow=str(0)+str(hnow)
					if len(str(mnow))==1:
						mnow=str(0)+str(mnow)
					myno1=int(str(ampmthen)+str(l2[0])+str(l2[1].split()[0]))
					myno3=int(str(ampmnow)+str(hnow)+str(mnow))
					if myno3>myno1:
						place=i
				else:
					if first:
						image2 = Image.open("arrow2.png")
						self.bcg3 = ImageTk.PhotoImage(image2)
						somlabel1 = Label(droot, image=self.bcg3)
						first=False
					somlabel1.place(x=150,y=start+30*Time__Interval.index(place))
			time.sleep(self.interval)
first=True
ex = ThreadingEx()

#homepage
class Application(Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets_main()

	def newaccount(self):
		global nroot, dark
		root.destroy()
		dark=False
		nroot = Tk()
		newaccn = newacc(newaccmaster=nroot)
		newaccn.mainloop()

	def loginacc(self):
		global lroot, dark
		root.destroy()
		dark=False
		lroot = Tk()
		loginn = login(loginmaster=lroot)
		loginn.mainloop()

	def create_widgets_main(self):
		self.master.title('Schedule IT!')
		image = Image.open("nbg3.jpg")
		image2 = Image.open("t2-nbg3.jpg")

		self.bcg = ImageTk.PhotoImage(image)
		background_label = Label(self.master, image=self.bcg)
		background_label.place(x=0, y=0)
		wid, heig = image.size
		self.master.resizable(width=False, height=False)
		self.master.geometry("%sx%s" % (wid, heig))

		self.button1 = Button(text='New Account', font=('COURIER', 24), height=1, relief='flat',
							  bg='white', cursor='hand1', borderwidth=0, command=self.newaccount, activebackground='white')
		self.button1.place(x=385, y=348.5)
		self.button2 = Button(text='Login', font=('COURIER', 24), height=1, relief='flat',
							  bg='white', cursor='hand1', borderwidth=0, command=self.loginacc, activebackground='white')
		self.button2.place(x=425, y=205)

#top menubar
def addmenu(self, dmaster):
	global loginval,dark

	def donothing():
		pass

	def aboutscene():
		global aroot, checktime, loginval, dark
		loginval = False
		dmaster.destroy()
		checktime = False
		dark=False
		aroot=Tk()
		abouts = aboutframe(aboutmaster=aroot)
		abouts.mainloop()

	def loginac():
		global lroot, loginval, checktime, dark
		loginval = False
		checktime = False
		dmaster.destroy()
		dark=False
		lroot = Tk()
		loginns = login(loginmaster=lroot)
		loginns.mainloop()

	def newaccoun():
		global nroot, loginval, checktime, dark
		loginval = False
		checktime = False
		dmaster.destroy()
		dark=False
		nroot = Tk()
		newaccn = newacc(newaccmaster=nroot)
		newaccn.mainloop()

	def removeacc():
		global nam, val, checktime
		checktime = False
		makefile = open('ENCRYPTED TEXT USER.txt', 'r')
		list3 = makefile.readlines()
		makefile.close()
		myFile = r'ENCRYPTED TEXT USER.txt'
		fileAtt = os.stat(myFile)[0]
		if (not fileAtt & stat.S_IWRITE):
			   os.chmod(myFile, stat.S_IWRITE)
		makefile = open('ENCRYPTED TEXT USER.txt', 'w')
		list2 = [nam, val]
		newstr = ''
		for i in list3:
			if i == encrypt(list2):
				pass
			else:
				newstr += i
		makefile.write(newstr)
		makefile.close()
		if (not fileAtt & stat.S_IWRITE):
		   pass
		else:
		   os.chmod(myFile, stat.S_IREAD)
		loginac()

	def ask():
		if messagebox.showwarning("Remove Account", "Are you sure you want to remove account?", type='yesno') == 'yes':
			removeacc()

	def darkfun(master=dmaster):
		global background_label, image2,image, dark
		background_label.destroy()
		# image2 = Image.open("t2-nbg2.jpg")
		self.bcg = ImageTk.PhotoImage(image2)
		background_label = Label(master, image=self.bcg)
		background_label.place(x=0, y=0)
		dark=True
		self.maintaskcreate()

	def normalfun(master=dmaster):
		global background_label, image2,image, dark
		background_label.destroy()
		# image2 = Image.open("t2-nbg2.jpg")
		self.bcg = ImageTk.PhotoImage(image)
		background_label = Label(master, image=self.bcg)
		background_label.place(x=0, y=0)
		dark=False
		self.maintaskcreate()

	menubar = Menu(dmaster)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="New Account", command=newaccoun)
	if loginval:
		filemenu.add_command(label="Logout", command=loginac)
		filemenu.add_command(label="Remove account", command=ask)
	else:
		filemenu.add_command(label="Login", command=loginac)
	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=dmaster.destroy)
	menubar.add_cascade(label="File", menu=filemenu)
	Thememenu = Menu(menubar, tearoff=0)
	Thememenu.add_separator()
	Thememenu.add_command(label="Regular Theme", command=normalfun)
	Thememenu.add_separator()
	Thememenu.add_command(label="Dark Theme", command=darkfun)
	Thememenu.add_separator()
	Thememenu.add_command(label="More Themes Coming Soon...", command=donothing)
	menubar.add_cascade(label="Themes", menu=Thememenu)
	menubar.add_cascade(label="About", command=aboutscene)

	dmaster.config(menu=menubar)

#encryption
def encrypt(datalist):
	global dnow,checktime
	outlist = []
	this=False
	for i in datalist:
		if 'list' in str(type(i)):
			this=True
			outlist.append(dnow)
			for k in i:
				if k.isdigit():
					outno = hex(int(k))
					outlist.append(outno)
				else:
					outstr = ''
					alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
								 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','/', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','-', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ','1','2','3','4','5','6','7',':','8','9','0']
					myencryptionlist = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's',
										'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b','/', 'n', 'm','I', 'A', 'Y', 'Z', 'V', 'W', 'F', 'S', 'Q', 'R', 'L', 'M', 'P', 'G', 'E','-', 'D', 'U', 'B', 'H', 'O', 'J', 'T', 'N', 'X', 'C', 'K', ' ','0',':','9','8','7','6','5','4','3','2','1']
					for j in k:
						outstr += myencryptionlist[alphalist.index(j)]
					outlist.append(outstr)
			outlist.append('          ')
		elif i.isdigit():
			outno = hex(int(i))
			outlist.append(outno)
		else:
			outstr = ''
			alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
						 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
			myencryptionlist = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's',
								'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ' ']
			for j in i:
				outstr += myencryptionlist[alphalist.index(j)]
			outlist.append(outstr)
	if this:
		outlist.remove('          ')
	outlist = str(outlist)
	outlist += '\n'
	checktime=False
	return outlist

def decrypt(datalist):
	global Time__Interval,taskorder,mylist
	Time__Interval=[]
	taskorder=[]
	change=False
	for i in eval(datalist):
		if i.isspace():
			change=True
			mylist.remove('          ')
		if change:
			if i.isdigit():
				outno = hex(int(i))
				taskorder.append(outno)
			else:
				outstr = ''
				alphalist = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's','d', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b','/', 'n', 'm','I', 'A', 'Y', 'Z', 'V', 'W', 'F', 'S', 'Q', 'R', 'L', 'M', 'P', 'G', 'E','-', 'D', 'U', 'B', 'H', 'O', 'J', 'T', 'N', 'X', 'C', 'K', ' ','0',':','9','8','7','6','5','4','3','2','1']
				myencryptionlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','/', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','-', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ','1','2','3','4','5','6','7',':','8','9','0']
				for j in i:
					outstr += myencryptionlist[alphalist.index(j)]
				taskorder.append(outstr)
		else:
			if i.isdigit():
				outno = hex(int(i))
				Time__Interval.append(outno)
			else:
				outstr = ''
				alphalist = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's','d', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b','/', 'n', 'm','I', 'A', 'Y', 'Z', 'V', 'W', 'F', 'S', 'Q', 'R', 'L', 'M', 'P', 'G', 'E','-', 'D', 'U', 'B', 'H', 'O', 'J', 'T', 'N', 'X', 'C', 'K', ' ','0',':','9','8','7','6','5','4','3','2','1']
				myencryptionlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','/', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','-', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ','1','2','3','4','5','6','7',':','8','9','0']
				for j in i:
					outstr += myencryptionlist[alphalist.index(j)]
				Time__Interval.append(outstr)
	return [Time__Interval,taskorder]


class newacc(Frame):

	def __init__(self, newaccmaster=None):
		super().__init__(newaccmaster)
		self.newaccmaster = newaccmaster
		self.pack()
		self.create_widgets()

	def printvalues(self):
		global droot, loginval, nam, val, dark
		val = self.spin.get()
		nam = self.name.get()
		makefile = open('ENCRYPTED TEXT USER.txt', 'r')
		makefile.close()
		myFile = r'ENCRYPTED TEXT USER.txt'
		fileAtt = os.stat(myFile)[0]
		if (not fileAtt & stat.S_IWRITE):
		   os.chmod(myFile, stat.S_IWRITE)
		makefile=open('ENCRYPTED TEXT USER.txt','a')
		list2 = [nam, val]
		line = encrypt(list2)
		makefile.write(line)
		makefile.close()
		loginval = True
		nroot.destroy()
		dark=False
		myFile = r'ENCRYPTED TEXT USER.txt'
		 
		fileAtt = os.stat(myFile)[0]
		if (not fileAtt & stat.S_IWRITE):
		   pass
		else:
		   os.chmod(myFile, stat.S_IREAD)
		droot = Tk()
		dash = Dashboard(dashmaster=droot)
		dash.mainloop()

	def create_widgets(self):
		global background_label, image2,image
		self.newaccmaster.title('Schedule IT! - New Account')
		image = Image.open("nbg2.jpg")
		image2 = Image.open("t2-nbg2.jpg")
		self.bcg = ImageTk.PhotoImage(image)
		background_label = Label(self.newaccmaster, image=self.bcg)
		background_label.place(x=0, y=0)
		wid, heig = image.size
		self.newaccmaster.resizable(width=False, height=False)
		self.newaccmaster.geometry("%sx%s" % (wid, heig))
		self.maintaskcreate()

	def maintaskcreate(self):
		global dark
		self.butt = Label(text='Please enter your name : ', font=(
			'COURIER', 14), height=1, border='0', bg='white', relief='ridge', cursor='target')
		self.butt.place(x=95, y=260)
		self.name = Entry(self.newaccmaster, width=18, font=(
			'COURIER', 16), border=2, cursor='hand1')
		self.name.place(x=360, y=260)

		self.butt = Label(text='Please select your age : ', font=(
			'COURIER', 18), height=1, border='0', bg='white', relief='ridge', cursor='target')
		self.butt.place(x=100, y=375)

		self.spin = Spinbox(self.newaccmaster, from_=10, to=18,
							width=5, state='readonly', font=('COURIER', 18), bg='white', relief='ridge', cursor='circle')
		self.spin.place(x=460, y=375)

		self.button1 = Button(text='GO', font=('COURIER', 18), height=1, relief='flat',
							  bg='green', cursor='hand1', command=self.printvalues, borderwidth=0, activebackground='green')
		self.button1.place(x=560, y=370)
		if dark:
			self.button1.configure(bg="#8922d1", activebackground='#8922d1')
		addmenu(self, dmaster=self.newaccmaster)


class aboutframe(Frame):

	def __init__(self, aboutmaster=None):
		super().__init__(aboutmaster)
		self.aboutmaster = aboutmaster
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		global background_label, image2,image
		self.aboutmaster.title('Schedule IT! - About The Developers')
		image = Image.open("nbg5.jpg")
		image2 = Image.open("t2-nbg5.jpg")
		self.bcg = ImageTk.PhotoImage(image, master=self.aboutmaster)
		background_label = Label(self.aboutmaster, image=self.bcg)
		background_label.place(x=0, y=0)
		wid, heig = image.size
		self.aboutmaster.resizable(width=False, height=False)
		self.aboutmaster.geometry("%sx%s" % (wid, heig))
		self.maintaskcreate()

	def maintaskcreate(self):
		global dark
		addmenu(self, dmaster=self.aboutmaster)



class login(Frame):

	def __init__(self, loginmaster=None):
		super().__init__(loginmaster)
		self.loginmaster = loginmaster
		self.pack()
		self.create_widgets()

	def check(self):
		global droot, loginval, val, nam, dark
		val = self.spin.get()
		nam = self.name.get()
		makefile = open('ENCRYPTED TEXT USER.txt', 'r')
		# line = '[{},{}]\n'.format(nam, val)
		list2 = [nam, val]
		line = encrypt(list2)
		list1 = makefile.readlines()
		if line in list1:
			loginval = True
			self.butt3.place_forget()
			makefile.close()
			dark=False
			lroot.destroy()
			droot = Tk()
			dash = Dashboard(dashmaster=droot)
			dash.mainloop()
		else:
			self.butt3.place(x=150, y=500)
		myFile = r'ENCRYPTED TEXT USER.txt'
		 
		fileAtt = os.stat(myFile)[0]
		if (not fileAtt & stat.S_IWRITE):
		   pass
		else:
		   os.chmod(myFile, stat.S_IREAD)

	def create_widgets(self):
		global background_label, image2,image
		self.loginmaster.title('Schedule IT! - Login')

		# self.dir=filedialog.askopenfilename()
		# self.labl=Label(text=self.dir)
		# self.labl.pack()

		image = Image.open("nbg2.jpg")
		image2=Image.open("t2-nbg2.jpg")

		self.bcg = ImageTk.PhotoImage(image)
		background_label = Label(self.loginmaster, image=self.bcg)
		background_label.place(x=0, y=0)
		wid, heig = image.size
		self.loginmaster.resizable(width=False, height=False)
		self.loginmaster.geometry("%sx%s" % (wid, heig))
		self.maintaskcreate()

	def maintaskcreate(self):
		global dark
		self.butt = Label(text='Enter your name : ', font=(
			'COURIER', 18), height=1, border='0', bg=self.loginmaster['bg'], relief='ridge', cursor='target')
		self.butt.place(x=95, y=260)
		self.name = Entry(self.loginmaster, width=18, font=(
			'COURIER', 16), border=2, cursor='hand1')
		self.name.place(x=360, y=260)

		self.butt = Label(text='Enter your age : ', font=(
			'COURIER', 20), height=1, border='0', bg=self.loginmaster['bg'], relief='ridge', cursor='target')
		self.butt.place(x=100, y=375)

		self.spin = Spinbox(self.loginmaster, from_=10, to=18,
							width=5, state='readonly', font=('COURIER', 20), bg=self.loginmaster['bg'], relief='ridge', cursor='circle')
		self.spin.place(x=440, y=375)

		self.button1 = Button(text='GO', font=('COURIER', 18), height=1, relief='flat',
							  bg='green', cursor='hand1', command=self.check, borderwidth=0, activebackground='green')
		self.button1.place(x=560, y=370)
		self.butt3 = Label(text='The account does not exist ! :( ', font=(
			'COURIER', 20), height=1, border='0', bg=self.loginmaster['bg'], relief='ridge', cursor='target', fg='red')
		if dark:
			self.button1.configure(bg="#8922d1", activebackground='#8922d1')
		addmenu(self, dmaster=self.loginmaster)

find=True


class Dashboard(Frame):
	global nam

	def __init__(self, dashmaster=None):
		super().__init__(dashmaster)
		self.dashmaster = dashmaster
		self.pack()
		self.create_widgets_dash()

	def makelist(self):
		global coaching, coachinghrs, Maindict, coachingval, schoolgo, val
		Maindict = {}
		Fixed_Task_Time_dict = {'Lunch': (1, 0),
								'School': (6, 0), 'Coaching/Tuitions': (coachinghrs, 0), 'Morning Rituals': (1, 0)}
		ti = (6, 30)
		somevar = ti

		def dicter(task, t, time=None):
			global Maindict, ti, somevar
			if time == None:
				time = Fixed_Task_Time_dict[task]
			ti2 = []
			for i in t:
				ti2.append(int(i))
			ti = ti2
			tin = []
			tin.append(ti[0] + time[0])
			tin.append(ti[1] + time[1])
			if ti[1] == 0:
				ti[1] = '00'
			if tin[1] == 0:
				tin[1] = '00'
			if tin[1] == 60:
				tin[1] = '00'
				tin[0] += 1
			if ti[0] == 0:
				ti[0] = '12'
			if tin[0] == 0:
				tin[0] = '12'
			if int(ti[0]) < 12:
				ampm1 = 'A'
			else:
				ampm1 = 'P'
			if int(tin[0]) < 12:
				ampm2 = 'A'
			else:
				ampm2 = 'P'
			if ampm2 == 'P' and ampm1 == 'A':
				if int(tin[0])!=12:
					Maindict[
						task] = '{}:{} {}M - {}:{} {}M'.format(ti[0], ti[1], ampm1, tin[0] - 12, tin[1], ampm2)
				else:
					Maindict[
						task] = '{}:{} {}M - {}:{} {}M'.format(ti[0], ti[1], ampm1, tin[0], tin[1], ampm2)
			elif ampm1 == 'P' and ampm2 == 'A':
				if int(ti[0])!=12:
					Maindict[
						task] = '{}:{} {}M - {}:{} {}M'.format(ti[0]-12, ti[1], ampm1, tin[0], tin[1], ampm2)
				else:
					Maindict[
						task] = '{}:{} {}M - {}:{} {}M'.format(ti[0], ti[1], ampm1, tin[0], tin[1], ampm2)
			elif ampm2 == 'P':
				if int(ti[0])!=12:
					Maindict[
						task] = '{}:{} {}M - {}:{} {}M'.format(ti[0]-12, ti[1], ampm1, tin[0]-12, tin[1], ampm2)
				else:
					Maindict[
						task] = '{}:{} {}M - {}:{} {}M'.format(ti[0], ti[1], ampm1, tin[0]-12, tin[1], ampm2)
			else:
				Maindict[
					task] = '{}:{} {}M - {}:{} {}M'.format(ti[0], ti[1], ampm1, tin[0], tin[1], ampm2)
			somevar = []
			for j in tin:
				somevar.append(int(j))
			return somevar
		if int(val) <= 14:
		    if schoolgo:
		        somevar = dicter('Morning Rituals', somevar)
		        somevar = dicter('School', somevar)
		        somevar = dicter('Lunch', somevar)
		        somevar = dicter('Self Study', somevar, (1, 30))
		        somevar = dicter('Refreshment', somevar, (0, 30))
		        somevar = dicter(' Self Study ', somevar, (1, 30))
		        somevar = dicter('Play Time', somevar, (2, 00))
		    else:
		        somevar = dicter('Morning Rituals', somevar)
		        somevar = dicter('Home-Work/Read', somevar, (2, 00))
		        somevar = dicter('Play Time', somevar, (2, 30))
		        somevar = dicter('Lunch', somevar)
		        somevar = dicter('Self Study', somevar, (1, 00))
		        somevar = dicter('Nap', somevar, (2, 00)) 
		        somevar = dicter(' Self Study ', somevar, (1, 00))
		        somevar = dicter('Play Time ', somevar, (3, 00))
		        somevar = dicter('Refreshment', somevar, (0, 30))

		    if somevar[0] == 20:
		        somevar = dicter('Dinner', somevar, (1, 0))
		        somevar = dicter('Me Time', somevar, (1, 00))
		        somevar = dicter('Family Time', somevar, (0, 30))
		        somevar = dicter('Sleep', somevar, (-17, 30))
		else:
			if schoolgo:
				somevar = dicter('Morning Rituals', somevar)
				somevar = dicter('School', somevar)
				somevar = dicter('Lunch', somevar)
				somevar = dicter('Self Study', somevar, (1, 0))
				if coaching:
					somevar = dicter('Coaching/Tuitions', somevar)
					if coachinghrs == 4:
						somevar = dicter('Refreshment', somevar, (0, 30))
					else:
						somevar = dicter('Self Study ', somevar,
										 ((19 - somevar[0]), (30 - somevar[1])))
						somevar = dicter('Refreshment', somevar, (0, 30))
				else:
					somevar = dicter('Self Study ', somevar, (2, 0))
					somevar = dicter('Refreshment', somevar, (0, 30))
					somevar = dicter('Self Study  ', somevar, (2, 0))
			else:
				somevar = (7, 0)
				somevar = dicter('Morning Rituals', somevar)
				if coaching:
					if not coachingval:
						somevar = dicter('Coaching/Tuitions', somevar)
						if coachinghrs == 4:
							somevar = dicter('Refreshment', somevar, (0, 30))
						else:
							somevar = dicter(' Self Study ', somevar,
											 ((12 - somevar[0]), (30 - somevar[1])))
							somevar = dicter('Refreshment', somevar, (0, 30))
						somevar = dicter('Lunch', somevar)
						somevar = dicter('  Self Study  ', somevar, (3, 0))
						somevar = dicter(' Refreshment ', somevar, (0, 15))
						somevar = dicter('   Self Study   ', somevar, (2, 15))
						somevar = dicter('ME Time', somevar, (1, 0))
					else:
						somevar = dicter('Self Study', somevar, (4, 30))
						somevar = dicter('Lunch', somevar)
						somevar = dicter(' Self Study ', somevar, (1, 30))
						somevar = dicter('Refreshment', somevar, (0, 30))
						somevar = dicter('Coaching/Tuitions', somevar)
						if coachinghrs == 4:
							somevar = dicter(' Refreshment ', somevar, (0, 30))
						else:
							somevar = dicter('  Self Study  ', somevar,
											 ((19 - somevar[0]), (30 - somevar[1])))
							somevar = dicter(' Refreshment ', somevar, (0, 30))
				else:
					somevar = dicter('Self Study', somevar, (4, 30))
					somevar = dicter('Lunch', somevar)
					somevar = dicter(' Self Study ', somevar, (1, 30))
					somevar = dicter('Refreshment', somevar, (0, 30))
					somevar = dicter('  Self Study  ', somevar, (4, 0))
					somevar = dicter(' Refreshment ', somevar, (0, 30))
			if somevar[0] == 20:
				somevar = dicter('Dinner', somevar, (1, 0))
				somevar = dicter('    Self Study    ', somevar, (2, 30))
				somevar = dicter('Sleep', somevar, (-17, 00))

	def showtable(self):
		global Time__Interval, taskorder, Maindict, checktime,nam,find, val, start, dark
		self.butt.place_forget()
		self.button2.configure(state=DISABLED)
		self.button1.configure(state=DISABLED)
		if find:
			self.makelist()
			Time__Interval = []
			taskorder = []
			Time__Interval = list(Maindict.values())
			taskorder = list(Maindict.keys())
		self.l = []
		h = 0
		if int(val)<=14:
			start=100
		else:
			start=120
		index2=0
		for i in range(2):
			for j in range(len(Time__Interval)):
				if i == 0:
					self.l.append(Label(self.dashmaster, text=Time__Interval[j], relief=RIDGE, font=(
						'COURIER', 16), fg='white', bg='black', width=20))
					if dark:
						self.l[index2].configure(fg='black',bg='white')
				else:
					self.l.append(Label(self.dashmaster, text=taskorder[j], relief=RIDGE, font=(
						'COURIER', 16), fg='white', bg='#777777', width=20))
					if dark:
						self.l[index2].configure(fg='black',bg='white')
				index2+=1
				self.l[h].place(x=200 + (270 * i), y=start + (30 * j))
				h += 1
		self.butt6.configure(state=NORMAL)
		checktime = True
		ex = ThreadingEx()
		encryptednamestr=''
		for i in eval(encrypt(nam)):
			encryptednamestr+=i
		if os.path.exists('ENCRYPTED SCHEDULES {}.txt'.format(encryptednamestr)):
			file=open('ENCRYPTED SCHEDULES {}.txt'.format(encryptednamestr))
			mylis=file.readlines()
			list2 = [Time__Interval, taskorder]
			line = encrypt(list2)
			file.close()
			myFile = r'ENCRYPTED SCHEDULES {}.txt'.format(encryptednamestr)
			 
			fileAtt = os.stat(myFile)[0]
			if (not fileAtt & stat.S_IWRITE):
			   os.chmod(myFile, stat.S_IWRITE)
			if line in mylis:
				pass
			else:
				if dnow in str(mylis):
					makefile = open('ENCRYPTED SCHEDULES {}.txt'.format(encryptednamestr), 'w')		
					makefile.write(line)
					makefile.close()
				else:
					makefile = open('ENCRYPTED SCHEDULES {}.txt'.format(encryptednamestr), 'a')		
					makefile.write(line)
					makefile.close()
			myFile = r'ENCRYPTED SCHEDULES {}.txt'.format(encryptednamestr)
			 
			fileAtt = os.stat(myFile)[0]
			if (not fileAtt & stat.S_IWRITE):
			   pass
			else:
			   os.chmod(myFile, stat.S_IREAD)
		else:
			list2 = [Time__Interval, taskorder]
			line = encrypt(list2)
			makefile = open('ENCRYPTED SCHEDULES {}.txt'.format(encryptednamestr), 'a')		
			makefile.write(line)
			makefile.close()
		checktime=True

	def cleart(self):
		global somlabel1,checktime,butt,first,dark
		for i in self.l:
			i.place_forget()
			self.butt6.configure(state=DISABLED)
		somlabel1.place_forget()
		somlabel1.destroy()
		first=True
		checktime=False
		self.button2.configure(state=NORMAL)
		self.butt.place(x=320, y=263)
		self.button1.configure(state=NORMAL)
		if dark:
			self.butt0.configure(bg='#bcbcbc',fg='black')
			self.button1.configure(bg='white', activebackground='white')
			self.button2.configure(bg='white', activebackground='white')
		else:
			self.butt0.configure(bg='#00a2e8',fg='#FF1414')
			self.button1.configure(bg='#FFC90E', activebackground='#FFC90E')
			self.button2.configure(bg='#FFC90E', activebackground='#FFC90E')

	def asksch(self):
		global val, coaching, coachinghrs, coachingval, schoolgo, find
		if int(val) <= 14:
			if messagebox.askquestion('Q-1.', 'Are you going to school nowadays?', type='yesno') == 'yes':
				schoolgo = True
			else:
				schoolgo = False
			self.showtable()
		if int(val) in range(15, 18):
			if messagebox.askquestion('Q-1.', 'Are you going to school nowadays?', type='yesno') == 'yes':
				schoolgo = True
			else:
				schoolgo = False
			if messagebox.askquestion('Q-2.', 'Do you go to coaching or tuitions?', type='yesno') == 'yes':
				coaching = True

				def sel1():
					global coachingval
					coachingval = 0

				def sel2():
					global coachingval
					coachingval = 1

				def save():
					global coachinghrs,find
					coachinghrs = int(spin2.get())
					self.newframe.destroy()
					find=True
					self.showtable()

				self.newframe = Tk()
				self.newframe.title('Coaching Or Tuitions')
				self.image6 = Image.open("back - Copy(4).jpg")

				# master written to prevent the pyimage% doesnt exist
				self.bcgg = ImageTk.PhotoImage(
					self.image6, master=self.newframe)
				background_labelg = Label(self.newframe, image=self.bcgg)
				background_labelg.image = self.bcgg
				background_labelg.place(x=0, y=0)
				wid, heig = self.image6.size
				self.newframe.resizable(width=False, height=False)
				self.newframe.geometry("%sx%s" % (wid, heig))
				var = IntVar()
				R1 = Radiobutton(self.newframe, text="Early Morning", font=('COURIER', 15),
								 command=sel1, variable=var, value=0, bg='white')
				R1.place(x=wid / 2 - 180, y=35)
				R1.deselect()
				if schoolgo:
					R1.configure(state=DISABLED)
				R3 = Radiobutton(self.newframe, command=sel1,
								 variable=var, value=2)
				R3.place(x=2000, y=2000)
				R3.select()
				R2 = Radiobutton(self.newframe, text="Afternoon", font=(
					'COURIER', 15), bg='white', command=sel2, variable=var, value=1)
				R2.place(x=wid / 2 + 45, y=35)
				R2.deselect()
				butt5 = Label(self.newframe, text='Enter no. of hrs : ', font=(
					'COURIER', 18), height=1, border='0', relief='ridge', cursor='target', fg='black', bg='white')
				butt5.place(x=70, y=123)
				spin2 = Spinbox(self.newframe, from_=1, to=4, width=3, state='readonly', font=(
					'COURIER', 18), relief='ridge', cursor='circle', bg='white')
				spin2.place(x=350, y=123)
				butt4 = Button(self.newframe, text='Done', width=4, font=(
					'COURIER', 18), relief='flat', cursor='hand1', fg='black', command=save, bg='white', activebackground='white')
				butt4.place(x=215, y=230)
			else:
				coaching=False
				find=True
				self.showtable()

	def makeschedule(self):
		self.asksch()

	def checksch(self):
		global nam,dnow,checktime,find,mylist
		encryptednamestr=''
		for i in eval(encrypt(nam)):
			encryptednamestr+=i
		if os.path.exists('ENCRYPTED SCHEDULES {}.txt'.format(encryptednamestr)):
			file=open('ENCRYPTED SCHEDULES {}.txt'.format(encryptednamestr),'r')
			mylist2=(file.readlines())
			file.close()
			file=open('ENCRYPTED SCHEDULES {}.txt'.format(encryptednamestr),'r')
			mylist=eval(file.readline())
			notime=True
			def check():
				global notime
				if mylist[0]==dnow:
					mylist.remove(dnow)
					list1,list2=decrypt(str(mylist))
					Time__Interval=list1
					taskorder=list2
					taskorder.remove('          ')
					find=False
					self.showtable()
					notime=False
			check()
			for i in range(len(mylist2)-1):
				mylist=eval(file.readline())
				check()
			if notime:
				self.butt.configure(text='No time table of today made yet')
			file.close()
		else:
			self.butt.configure(text='No time table exists')

	def create_widgets_dash(self):
		global somlabel,butt,background_label, image2,image, dark
		self.dashmaster.title('Schedule IT! - Dashboard')
		image = Image.open("nbg4.jpg")
		image2 = Image.open("t2-nbg4.jpg")
		self.bcg2 = ImageTk.PhotoImage(image)
		background_label = Label(self.dashmaster, image=self.bcg2)
		background_label.place(x=0, y=0)
		wid, heig = image.size
		self.dashmaster.resizable(width=False, height=False)
		self.dashmaster.geometry("%sx%s" % (wid, heig))
		self.maintaskcreate()

	def maintaskcreate(self):
		global dark
		self.butt0 = Label(text='Welcome, \n {}'.format(nam), font=(
			'COURIER', 20), height=2, border='0', bg='#00a2e8', relief='ridge', cursor='target', fg='#FF1414')
		self.butt0.place(x=20, y=5)
		self.butt = Label(text='No Schedule\'s yet', font=(
			'COURIER', 20), height=1, border='0', bg='white', relief='flat', cursor='target', fg='red')
		self.butt.place(x=320, y=263)

		self.button1 = Button(text='Today\'s Schedule', font=('COURIER', 18), height=1, relief='flat',
							  bg='#FFC90E', cursor='hand1', command=self.checksch, borderwidth=0, activebackground='#FFC90E')
		self.button1.place(x=335, y=25)
		self.button2 = Button(text='New Schedule', font=('COURIER', 18), height=1, relief='flat',
							  bg='#FFC90E', cursor='hand1', command=self.makeschedule, borderwidth=0, activebackground='#FFC90E')
		self.button2.place(x=655, y=25)
		self.butt6 = Button(self.dashmaster, text='Clear Table', width=11, font=(
			'COURIER', 18), relief='flat', cursor='hand1', fg='black', command=self.cleart, bg='white', activebackground='white')
		self.butt6.place(x=350, y=490)
		self.butt6.configure(state=DISABLED)
		if dark:
			self.butt0.configure(bg='#bcbcbc',fg='black')
			self.button1.configure(bg='white', activebackground='white')
			self.button2.configure(bg='white', activebackground='white')
		addmenu(self, dmaster=self.dashmaster)

root = Tk()
app = Application(master=root)
app.mainloop()
