# estado inicial das variaveis
produto = 1
while True:
 n = int(input())    # 2 -16 3 -1 2 4 0
if n == 0: break     # saia do laço
if n < 0: continue   # volte para o inicio do laço
produto = produto * n

# saida de dados
print(f"O produto dos positivos: {produto}")