from datetime import datetime as dt

while True:
    code = input('Input code to save: ')
    try:
        open('record.csv', 'a').write(f'{dt.now().strftime("%d-%m-%Y, %H:%M:%S")}, https://lihkg.com/thread/{code}/page/1\n')
        print('Record updated, see record.csv')
    except:
        print('You may have the record file opened. Please close it before adding new posts.')
