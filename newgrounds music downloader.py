import webbrowser

print('NEWGROUNDS MUSIC DOWNLOADER BY: JACKLSUMMER15')

#get song here
songid = input('Enter song ID: ')

#link
ogg = 'https://www.newgrounds.com/audio/download/' + songid


if songid == '':
    print('ERROR: 1')
else :
    webbrowser.open(ogg)
    print('DONE!')
