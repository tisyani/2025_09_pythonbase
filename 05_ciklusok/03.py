
folytatja = True
while folytatja:
      print('Vidd ki a szemetet!')
      valasz = input('Mondjam még egyszer?  (i/n)')
      if valasz == 'n' or valasz == "nem":
            folytatja = False
      elif valasz == "igen":
          print("i-n-el ne valaszolj")
print('>> Program vége! <<')      
  