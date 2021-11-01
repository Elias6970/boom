import os

os.system("cd '/Users/Elias6970/Desktop/try' &&  touch a.txt")

for a in range(5):
   
   y="cd '/Users/Elias6970/Desktop/try' &&  touch "+str(a)+".txt"
   os.system(y) 
