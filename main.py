import write_html as wh
import sys

def main() :
    lenlen = len(sys.argv)
    if lenlen in [4, 5]:
        if lenlen == 4 :
            month = int(input('Month: '))
        else :
            month = int(sys.argv[4])
        wh.write_in_html(sys.argv[1].upper(), sys.argv[2].capitalize(), month, sys.argv[3].upper())
    else :
        print('Error, need 3 argv : name, firstname, english group, month number (optionnal)')

main()
