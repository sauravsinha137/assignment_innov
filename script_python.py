
import os


print "which drive you want to search?"

drive=raw_input()

dir1 =drive+":\\"
maxdict={'A':0.0,'B':0.0,'C':0.0,'D':0.0,'E':0.0,'F':0.0,'G':0.0,'H':0.0,'I':0.0,'J':0.0}
print "searching...."
for file in os.walk(dir1):
	for x in file[2]:
		loc1=file[0]+'\\'+str(x)
		#print x
		b=os.path.getsize(loc1)    #getting size of file
		mini=maxdict.values()[0]
		minik=maxdict.keys()[0]
		for key in maxdict:
			if(mini>maxdict[key]):
				mini=maxdict[key]
				minik=key          #finds minimum value in dictionary
		if(b>mini):
			del maxdict[minik]
			maxdict[loc1]=b        #delete and replace file from dictionary if minimum key in maxdict is  smaller than current file size

	
print " location of file with size ..."		
for keys in sorted(maxdict, key=maxdict.get, reverse=True):     #sorting list according to size
        print keys+ "  =  "+ str(float(maxdict[keys])/1048576.0)+" Mb"
