from datetime import date, datetime, timedelta

STR_FORMATACAO = "%d/%m/%Y %H:%M:%S"
exame_realizado_em = datetime.now()
print(exame_realizado_em)
data_exame_str = exame_realizado_em.strftime(STR_FORMATACAO)
print(data_exame_str)
TEMPO_RESULTADO_EXAME = timedelta(days=2)
print(TEMPO_RESULTADO_EXAME)
previsao_resultado = exame_realizado_em + TEMPO_RESULTADO_EXAME
previsao_de_entrega_str = previsao_resultado.strftime(STR_FORMATACAO)
print(previsao_de_entrega_str)

print(f'Data de realização do exame:{data_exame_str}')
print(f'Previsão de entrega do resultado: {previsao_de_entrega_str}')

