print('=== Cálculo de Produtividade ===')
try:
   total_produzido = float(input('valor total da venda: '))
   funcionarios = int(input('Total de Funcionários: '))

   media_por_funcionario = total_produzido / funcionarios

   media_por_funcionario = total_produzido / funcionarios
   print(f'Média por funcionário: {media_por_funcionario:.2f}')


except Exception as e:
   print(f'Ops! Erros nos valores de entrada {e}')
except KeyboardInterrupt:
   print('Operação cancelada pelo usuário')
else:
   print(f'Media por funcionário: {media_por_funcionario:.2f}')

# Executa sempre. Com erro ou não, o bloco finally sempre irá executar
finally:
   print('Programa encerrado!')


