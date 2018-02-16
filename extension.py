# this code sort the files on Desktop on the basis of file extension and move them in separate folders in Documents folder.
import os
import shutil
filename, file_extension = os.path.splitext('')

dir1="C:\Users\saurav\Desktop"     
inewpath = "C:\Users\saurav\Documents" 
for file in os.walk(dir1):
   for x in file[2]:
		loc1=file[0]+'\\'+str(x)
		filename, file_extension = os.path.splitext(loc1)  #gives the extension of file
		file_extension=file_extension.replace(".", "")
		#print file_extension
		newpath=inewpath+"\\"+file_extension
		if not os.path.exists(newpath):       #finds if there exist  a folder with searched extension type 
			os.makedirs(newpath)
		shutil.move(loc1,newpath)            #changes the location of file



