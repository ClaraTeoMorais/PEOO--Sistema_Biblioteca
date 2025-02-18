from datetime import datetime, timedelta

# Data de hoje
hoje = datetime.now()

# Soma 14 dias
data_futura = hoje + timedelta(days=14)

# Exibir no formato desejado
print(data_futura.strftime("%d/%m/%Y"))  # Exemplo de formatação: "22/02/2025"