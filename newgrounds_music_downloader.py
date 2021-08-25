import os

print('NEWGROUNDS MUSIC DOWNLOADER BY: JACKLSUMMER15')

try:
  os.mkdir('music')
  
except:
  pass

#get song here
songid=input('Enter song ID: ')

#link
mp3='https://www.newgrounds.com/audio/download/'+songid

#downloading process
os.system('curl --fail --silent -# -H "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64)" -L '+mp3+' -o music/'+songid+'.mp3')


