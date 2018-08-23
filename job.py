from time import sleep
from subprocess import call
cmd5 = "rm Tetris.tar.gz"
cmd4 = "rm /var/www/html/Tetris.tar.gz"
cmd1 = "tar -czvf Tetris.tar.gz ./Tetris"
cmd2 = "cp Tetris.tar.gz /var/www/html"

while True:
  call(cmd4, shell=True)
  call(cmd5, shell=True)
  call(cmd1, shell=True)
  call(cmd2, shell=True)
  print "Durmiendo..."
  sleep(5)
