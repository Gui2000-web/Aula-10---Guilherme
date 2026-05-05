print('=== Cálculo de Produtividade ===')
try:
   total_produzido = float(input('valor total da venda: '))
   funcionarios = int(input('Total de Funcionários: '))

   media_por_funcionario = total_produzido / funcionarios

   media_por_funcionario = total_produzido / funcionarios
   print(f'Média por funcionário: {media_por_funcionario:.2f}')
except ValueError:
   print('Informe um número.')
except ZeroDivisonError:
   print('Funcionário não pode ser zero')
else:
   print(f'Media por funcionário: {media_por_funcionamento:.2f}')
finally:
   print('Programa encerrado!')