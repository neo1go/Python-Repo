# dies dient der Erklärung für main und die Referenzierung von anderen Dateien, die diese Datei importieren.

print("This will always be shown, regardless of the main method been executed or not.")


print ("First Module's Name: {}".format(__name__))   # wenn main nicht existiert, wird trotzdem beim Start dieser Datei hier für name main eingesetzt.


def main():
    print("First module's main method executed.")


if __name__ == '__main__':
    print("Run directly")
    main()
else:
    print("Run from import wich serves as main instead.")