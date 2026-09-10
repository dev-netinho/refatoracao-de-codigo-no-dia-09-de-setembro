class ProcessadorVenda:
    def processar(self, cliente: str, valor: float, email_cliente: str):
        # 1. Regra de Negócio + Validação
        if valor <= 0:
            raise ValueError("O valor da venda deve ser maior que zero.")

if valor < 100:
    valor_com_desconto = valor * 0.9 
else:
    valor_com_desconto = valor

# 2. Persistência (Acesso a Dados)
    with open("vendas.txt", "a") as f:
    f.write(f"{cliente};{valor_com_desconto}\n")
    print(f"[BD] Venda registrada para o cliente {cliente}")

@abstractmethod
def enviar_email(self, destinatario: str, mensagem: str):