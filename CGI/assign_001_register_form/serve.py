#!C:\Users\Joel\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe
# the shebang/SHArp bang line


print('content-type: text/html')



import cgi
import html
import os
import cgitb

cgitb.enable()

try:
    import msvcrt
    msvcrt.setmode(0, os.O_BINARY)
    msvcrt.setmode(1, os.O_BINARY)
except ImportError:
    pass


# def tag(tag,text,**kwargs):
#     rt =""
#     rt+= "<"+tag
#     for i in kwargs:
#         rt+= " "+i+"="+"'"+str(kwargs[i])+"'"
#     rt+= ">"
#     rt+= text
#     rt+= "</"+tag+">"
#     return rt

form = cgi.FieldStorage()

name = (form.getvalue('name', 'None'))
email = (form.getvalue('email', 'None'))
password = (form.getvalue('password', 'None'))
emotion = form.getlist('emtions')
satisfied = form.getvalue('satisfied', 'None')
comments = (form.getvalue('comments'))
img = form['photo']
location = form.getvalue('loc', 'None')
filename =img.filename
message=""
if filename:
    open('files/' + os.path.basename(filename), 'wb').write(img.file.read())
    message = 'upload successful'
else:
    message = 'No file was uploaded'

print(f'''
<html>
<head>
    <title>Server Reply</title>
</head>
<body>
    Name: {name}
    <br>
    Email: {email}
    <br>
    Password: {password}
    <br>
    Emotions: {", ".join([i for i in emotion])}
    <br>
    Satisfied: {satisfied}
    <br>
    Comments: {comments}
    <br>
    Photo: {message}
    <br>
    Locaion: {location}
    <br>
</body>
</html>
''')