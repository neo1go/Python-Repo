from assignment2 import LogFile, DelimFile



def main():
    log = LogFile('log.txt')
    c = DelimFile('text.csv', ',')

    log.write('this is a log message')
    log.write('this is another log message')

    c.write(['a', 'b', 'c', 'd'])
    c.write(['1', '2', '3', '4'])






if __name__ == '__main__':
    main()      # darf erst hier aufgerufen werden da es kein hoisting wie in js gibt.