#!/usr/bin/env python



import random
import optparse

def main():
  usage = "usage: %prog [options"
  p = optparse.OptionParser(usage) 
  
  p.add_option('-m', '--max', type='int', default=10, help='Maximum allowable season [10]')

  opts, args = p.parse_args()

  # Will hold list of lists where index is season number and the list at
  # that index is a list of episodes
  seas_list = []
  # There might be a better way to make the index 1-based, but this is easy
  seas_list.append([])
  
  with open("simpsons-world.txt", "r") as fin:
    for line in fin:
      if line.startswith("#"):
        curr_seas = int(line.rstrip().split(" ")[2])
        seas_list.append([])
      else:
        seas_list[curr_seas].append(line.rstrip())
  
  season_number = random.randint(1,opts.max)
  seas = seas_list[season_number]

  episode = random.choice(seas)
  print(season_number, episode)

if __name__ == '__main__':
  main()