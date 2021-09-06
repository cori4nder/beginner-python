# Montanh-Russa: verificar os participantes permitidos a ir no brinquedo

while True:
  try:
       n, minn, maxx = map(int, input().split())
       contar = 0
       for i in range(n):
         altura = int(input())
         if (altura >= minn and altura <= maxx): contar += 1
       print(contar)
  except EOFError:
      break
