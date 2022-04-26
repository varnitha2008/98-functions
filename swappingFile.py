def swapFileData():
    fileName =  input("Enter the file name:- ")
    file = open(fileName,"data_a")
    flines=file.readlines()
    with open (file1,"r") as a:
        data_a =a.read()
    with open(file1,'w') as a:
        a.write(data_b)




