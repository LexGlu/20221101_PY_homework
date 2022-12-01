def create_hfw():
    with open('myfile.txt', 'w') as f:
        f.write('Hello file world!')


def read_hfw():
    with open('myfile.txt') as f:
        data = f.read()
        print(type(data))


create_hfw()
read_hfw()

"""
1) Does the new file show up in the directory where you ran your scripts?
    - Yes, if we indicate only the name of the file
2) What if you add a different directory path to the filename passed to open?
    - File will be created in that directory path (if it exists) and read from it
"""

# __added a different directory path to the filename passed to open__


# def create_hfw_elsewhere():
#     with open('elsewhere/myfile.txt', 'w') as f:
#         f.write('Hello file world!')
#
#
# def read_hfw_from_elsewhere():
#     with open('elsewhere/myfile.txt') as f:
#         print(f.read())
#
#
# create_hfw_elsewhere()
# read_hfw_from_elsewhere()
