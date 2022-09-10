#!/usr/bin/python3

import os
import cgi

print_list = []
root = "/home/calvin/MainCode/Self"
# root = "/var/www/html/"

# parses url 
def get_args():
    arguments = cgi.FieldStorage()
    path = arguments.getfirst("dir")
    if not path:
        path = ""

    search = arguments.getfirst("search")
    if not search:
        search = ""

    return path, search


# Converts bytes to needed unit
def format_file_size(size):
  unit = 0
  units = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]

  while (size >= 1024):
    size /= 1024
    unit += 1
  
  return f"{round(size, 2)} {units[unit]}"


# TODO finish alphabetical sort
def print_directery(path):

    for x in os.listdir(root + path):
        if os.path.isdir(root + path + "/" + x):
            print (f"<li><a href=\"?dir={path}/{x}\">{x}</a></li>")

        else:
            file_size = os.path.getsize(f"{root}{path}/{x}")
            print (f"<li><a href=\"{path}/{x}\">{x} &#9 | &#9 {format_file_size(file_size)}</a></li>")


# Recursivly finds file names that match the search term
def search_func(search, path):
    for x in os.listdir(root + path):    
        if os.path.isdir(root + path + "/" + x):
            # print (f"<h1>search = {search}, path = {path}, x = {x} ----- </h1>")
            search_func(search, path + "/" + x)

        if search.lower() in x.lower():
            file_size = os.path.getsize(f"{root}{path}/{x}")
            print_list.append(f"<li><a href=\"{path}/{x}\">{x} &#9 | &#9 {format_file_size(file_size)}</a></li>")


def main():
    css = "body {color: #fca311; background-color: #14213d;} a {color: #ffffff; font-size: 1.5em; line-height: 1.6;} a:hover {color: #f8adff}  ol li {list-style-type: none;}"
    
    path, search = get_args()

    print ("Content-type:text/html\n\n")
    print (f"<style>{css}</style>")
    print ("<html>")
    print ("<head>")
    print ("<title>Hello World - First CGI Program</title>")
    print ("</head>")
    print ("<body>")
    print ("<form action=\"?\" method=\"GET\">")
    print ("<h2>Index of </h2>")
    # print ("Content-Type: text/html")

    print (f'<input type="hidden" name="dir" value="{path}" />')
    print ("<input type=\"text\" name=\"search\">")
    print ("<input type=\"submit\" value=\"send\">")
    print ("<ol>")

    # allows navigation to the parent directory
    PD = path[:path.rfind("/")] #the ":" allows the string is a substring operation
    print (f"<li><a href=\"?dir={PD}\"> &lt&lt PD</a></li>")
    
    if search == "":
        print_directery(path)

    if search != "":
        search_func(search, path)
    
    sorted(print_list)

    for x in print_list:
                print (x)
            
    print ("</ol>")
    print ("</form>")
    print ("</body>")
    print ("</html>")

if __name__ == '__main__':
    main()


# run command 
# scp /home/calvin/MainCode/PyServer/Main.py ubuntu@192.168.50.2:/usr/lib/cgi-bin/foo/