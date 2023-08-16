weight_lbs= int(input('What is your weight(lbs)?'))
bs_or_g= input('(L)bs or (K)g: ')


if bs_or_g.lower() == 'l': 
 convert=  weight_lbs * 0.45
 print(f" You are {convert} kilos")

elif bs_or_g.lower() == 'k':
  convert=  weight_lbs / 0.45 
  print(f" You are {convert} pounds")
 
 