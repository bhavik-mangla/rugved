import os
 
path1 = "/Users/bhavikmangla/Documents"
arr = os.listdir(path1)
 
print("Files and directories in '", path1, "' :")
t=0
j=0
path = path1
while t==0:
    try:
        arr1 = os.listdir(path)
        print("Files and directories in '", path, "' :")
        for i in arr1:
            if i[-4:] == ".cpp":
                print(i)
                t=1
    except:
        pass
    print("No .cpp files in ",path)

    path=path1+"/"+arr[j]

    if j<len(arr):
        j+=1