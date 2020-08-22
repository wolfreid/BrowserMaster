# # import os
import json
try:
     with open("my_file.json","r+") as my_file:
        lines = json.load(my_file)
        lines.update({"hello1":2})
        my_file.seek(0)
        my_file.truncate()
        json.dump(lines,my_file,indent = 4)      
#   # for line in my_file:
#             # print(line)
#         # my_file.write("hello2\n")
#         my_file.writelines("tdsdsad")
#         print(my_file.readlines(2))
except:        
     with open("my_file.json","w") as my_file:
        json.dump({"hello":1},my_file,indent = 4)


# if os.stat(file_path).st_size == 0:
#     print('File is empty')
# else:
#     print('File is not empty')
