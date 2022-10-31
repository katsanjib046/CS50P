#-------- Some imports ---------------
import sys
import re


#-------- Functions -----------------
def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if matches := re.search(r"^(?P<f>([0-9]|0[0-9]|1[0-2])|(([0-9]|0[0-9]|1[0-2]):([0-5][0-9]))) (?P<fap>AM|PM) to (?P<s>([0-9]|0[0-9]|1[0-2])|(([0-9]|0[0-9]|1[0-2]):([0-5][0-9]))) (?P<sap>AM|PM)$", s):
        if matches.group('fap') == 'AM' and ':' not in matches.group('f'):
            first = f"{int(matches.group('f')) % 12:02}:00"
        elif matches.group('fap') == 'AM' and ':' in matches.group('f'):
            faf, fas = matches.group('f').split(':')
            first = f"{(int(faf) % 12):02}" + ':' + fas
        elif ':' not in matches.group('f'):
            first = f"{(int(matches.group('f')) + 12) % 24 if int(matches.group('f')) < 12 else int(matches.group('f')):02}" + ':' + '00'
        else:
            fpf, fps = matches.group('f').split(':')
            first = f"{(int(fpf) + 12) % 24 if int(fpf) < 12 else int(fpf):02}" + ':' + fps

        if matches.group('sap') == 'AM' and ':' not in matches.group('s'):
            second = f"{int(matches.group('f')) % 12:02}:00"
        elif matches.group('sap') == 'AM' and ':' in matches.group('s'):
            saf, sas = matches.group('s').split(':')
            second = f"{int(saf) % 12:02}" + ':' + sas
        elif ':' not in matches.group('s'):
            second = f"{(int(matches.group('s')) + 12) % 24 if int(matches.group('s')) < 12 else int(matches.group('s')):02}" + ':' + '00'
        else:
            spf, sps = matches.group('s').split(':')
            second = f"{(int(spf) + 12) % 24 if int(spf) < 12 else int(spf):02}" + ':' + sps
        return f"{first} to {second}"
    else:
        raise ValueError('Not a valid input time format')






#-------- Testing -------------------
if __name__ == "__main__":
    main()
