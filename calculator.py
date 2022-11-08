def serie(switch, frontend, database):
  reliability = switch * frontend * database
  return reliability
def parallel(amount, reliability):
  unreliability = 1 - reliability
  reliability = 1 - (unreliability**amount)
  return reliability
print('Para o caso, nós temos os seguintes componentes: Switch, Front-end e Database.')
op = int(input('Switch está em série ou parelelo? 1-Série  2-Parelelo'))
if op == 1:
  switch = float(input('Informe a disponibilidade: '))
elif op ==2:
  amount = int(input('Qual a quantidade? '))
  switch = float(input('Informe a disponibilidade: '))
  switch = parallel(amount, switch)
op = int(input('Front-end está em série ou paralelo? 1-Série  2-Paralelo'))
if op == 1:
  frontend = float(input('Informe a disponibilidade: '))
elif op ==2:
  amount = int(input('Qual a quantidade? '))
  frontend = float(input('Informe a disponibilidade: '))
  frontend = parallel(amount, frontend)
op = int(input('Database está em série ou paralelo? 1-Série  2-Paralelo'))
if op == 1:
  database = float(input('Informe a disponibilidade: '))
elif op ==2:
  amount = int(input('Qual a quantidade? '))
  database = float(input('Informe a disponibilidade: '))
  database = parallel(amount, database)
print('A disponibilidade total é:', serie(switch, frontend, database))