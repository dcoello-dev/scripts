import sys
from os import listdir, system
from os.path import isfile, join


def usage():
    print "usage: " + sys.argv[0] + " name.py"


if __name__ == '__main__':
    if len(sys.argv) < 2 \
            or sys.argv[1][len(sys.argv[1])-2:len(sys.argv[1])] != "py":
        usage()
    else:
        command = "pyi-makespec --paths=./app "
        command = command + sys.argv[1]
        system(command)
        system("pyinstaller " +
               sys.argv[1].split(".")[0] +
               ".spec")
        system("sudo cp -r ./dist/" +
               sys.argv[1].split(".")[0] +
               " /usr/lib/")
        system("sudo mkdir /opt/"+sys.argv[1].split(".")[0])
        system("sudo cp -r ./conf/* ./spec/* " +
               "/opt/"+sys.argv[1].split(".")[0])


