import shutil, os
a=input('What home work is this?\n')
shutil.copytree(r'Homework',r'Homework '+a)
i=1
for folderName,subfolders,filenames in os.walk('Homework '+a):
	print('The current folder is ' + folderName)
	if folderName==r'Homework '+a+"\HW":
		os.rename(folderName,r'Homework '+a+"\HW"+a)
		print("renamed")
	if folderName==r'Homework '+a+"\HW P"+str(i):
		print("renamed")
		os.rename(folderName, r'Homework '+a+"\HW"+a+" P"+str(i))
	for subfolder in subfolders:
		print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
			
		print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
	for filename in filenames:
		if filename=="HW P.tex":
			os.rename(r'Homework '+a+"\HW"+a+" P"+str(i)+"\HW P.tex",r'Homework '+a+"\HW"+a+" P"+str(i)+"\HW"+a+" P"+str(i)+".tex")
			i+=1
		print('FILE INSIDE ' + folderName + ': '+ filename)

	print('')
shutil.move(r'hw_'+a+'.tex',r'Homework '+a+'\HW'+a)