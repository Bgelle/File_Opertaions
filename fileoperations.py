import os
from pathlib import Path
class File_Operations():
    # def Get_Directory(self):
    #     print(Path.cwd())
    # def Create_Directory(self):
    #     try:
    #         os.mkdir("test")
    #         print("Directory Created")
    #     except:
    #         print("Directory aleady exists")
    os.chdir("test")
    # def Write_File(self):
    #     try:
    #         with open("file1", "w") as file:
    #             file.write("This is File 1,There are more files")
    #         with open("file2", "w") as file:
    #             file.write("This is File 2,There are more files")
    #         with open("file3", "w") as file:
    #             file.write("This is File 3,There are more files")
    #         with open("file4", "w") as file:
    #             file.write("This is File 4,There is one more files")
    #         with open("file5", "w") as file:
    #             file.write("This is File 5,I am the last one")
    #         print("File is created")
    #     except:
    #         print("Filename already exists!!")
    #     finally:
    #         file.close()
    #         print("File Closed")
    # def Read_File(self,filename):
    #     try:
    #         with open(filename,"r") as file:
    #             content=file.read()
    #             print(content)
    #         # with open("file1", "r") as file:
    #         #     content=file.read()
    #         #     print(content)
    #         # with open("file2", "r") as file:
    #         #     content=file.read()
    #         #     print(content)
    #         # with open("file3", "r") as file:
    #         #     content=file.read()
    #         #     print(content)
    #         # with open("file4", "r") as file:
    #         #     content=file.read()
    #         #     print(content)
    #         # with open("file5", "r") as file:
    #         #     content=file.read()
    #         #     print(content)
    #
    #     except:
    #         print("Required File is not present")
    #     finally:
    #         file.close()
    #         print("File Closed")
    # def List_FilesinDirectory(self,directoryname):
    #     print(os.listdir())
        # fileList=os.listdir(directoryname)
        # for filename in fileList:
        #     print(filename)
    # def Rename_File(self):
    #     try:
    #         src = "file1"
    #         dest = "File_one"
    #         os.rename(src, dest)
    #         src = "file2"
    #         dest = "File_two"
    #         os.rename(src, dest)
    #         src = "file3"
    #         dest = "File_three"
    #         os.rename(src, dest)
    #         src = "file4"
    #         dest = "File_four"
    #         os.rename(src, dest)
    #         src = "file5"
    #         dest = "File_five"
    #         os.rename(src, dest)
    #         print("Files Renamed")
    #     except:
    #         print("File already Renamed")
    # def File_Append(self,filename):
    #     with open(filename,"a") as file:
    #         file.writelines(input("Enter content to be appended"))
    #     print("Content Appended")
    #def Is_Directory(self,filename):

        # try:
        #     if ((os.path.isdir(filename)) == True):
        #         print("Yes, Its a Directory!")
        # finally:
        #     if ((os.path.isfile(filename)) == True):
        #         print("May be its a file")
    # def Remove_File(self,filename):
    #     os.remove(filename)
    #     print("File Removed")
    def Write_Properties(self):

       try:
           List = os.listdir()
           with open("filename_proprties", "w") as file:
               for filename in List:
                   file.write(filename+"\n")



       finally:
        file.close()




        print("Filenames added in properties File")


# File_Operations.Get_Directory(self=File_Operations)
# File_Operations.Create_Directory(self=File_Operations)
# File_Operations.Write_File(self=File_Operations)
# File_Operations.Read_File(self=File_Operations,filename=input("Enter the file name to be read"))
#File_Operations.List_FilesinDirectory(self=File_Operations,directoryname=input("Enter Directory anme in which you wnat to list files"))
#File_Operations.Rename_File(self=File_Operations)
#File_Operations.File_Append(self=File_Operations,filename=input("Enter file name to which data has to be apended"))
#File_Operations.Is_Directory(self=File_Operations,filename=input("Enetr the File/Directory name you want to check"))
#File_Operations.Remove_File(self=File_Operations,filename=input("Enter Filename to be removed"))
File_Operations.Write_Properties(self=File_Operations)