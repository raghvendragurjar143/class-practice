##---------file handling
# 1.file handling in python means reading from and writing to files/folder stored on 
#disk using python.
#2, your python code can open a file , pull out date of it, 



#1. create a file in strict mode.
file=open("strict.txt","x")
print("file created")
except Exception as e:
print("error :file can not  run..")


##contaxt manager
with.open(filename,mode).as file:
    file.write("this is completely python file handaling..")
    file.seek(0)
    r=file.


    with open("demo.txt","r") as f:
        r=f.read()
        print(r)