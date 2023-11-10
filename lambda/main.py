sayHello = lambda name : print("selamat datang",name)

sayHello("wira")

#def addtition(num1,num2):
  #result = num1 + num2
  #print(result)

addition = lambda num1, num2 : print( num1+num2 )

addition(10,12)
#lambda tanpa argumen
(lambda : print("selamat datang"))()
#lambda dengan argumen
(lambda fruit : print("saya suka", fruit))("semangka")
#lambda dengan default argumen
(lambda name="" : print("selamat datang",name))("wira")