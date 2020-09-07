def towers_of_hanoi (n , source, destination, buffer):
  #base case: move last piece to destiation
  if n==1: 
      print (f'Move disk 1 from source {source} to destination {destination} ')
      return
  #recursive case:
  towers_of_hanoi(n-1, source, buffer, destination) 
  print (f'Move disk {n} from source {source} to destination {destination} ')
  towers_of_hanoi(n-1, buffer, destination, source) 

if __name__  == '__main__':
  towers_of_hanoi(4,'A','C','B')