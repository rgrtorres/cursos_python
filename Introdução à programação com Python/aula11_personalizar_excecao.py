try:
  x = 1
  elementos = ['terra', 'ar', 'fogo', 'agua']
  elementos.pop(x)
except:
  print('Elemento não encontrado')
else:
  print('Elemento {} removido.'.format(x))
finally:
  print('Busca completa')