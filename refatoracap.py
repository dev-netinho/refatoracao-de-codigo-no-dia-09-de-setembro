from abc import ABC, abstractmethod

class ValidacaoVenda(ABC):
    @abstractmethod
    def validar(self, valor: float) -> None:
        pass

class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass

class RepositorioVendas(ABC):
    @abstractmethod
    def salvar(self, cliente: str, valor: float) -> None:
        pass

class Notificador(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, mensagem: str) -> None:
        pass

class ValidacaoVendaBasica(ValidacaoVenda):
    def validar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Valor Inválido: O valor deve ser maior que zero.")

class CalculadorDescontoPadrao(CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.9 if valor > 100 else valor

class RepositorioArquivo(RepositorioVendas):
    def salvar(self, cliente: str, valor: float) -> None:
        with open("vendas.txt", "a") as f:
            f.write(f"{cliente};{valor}\n")
        print(f"[BD] Venda salva no arquivo para {cliente}")

class EnviadorEmail(Notificador):
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"[E-MAIL] Enviando e-mail para {destinatario}: {mensagem}")

class ProcessadorVendas:
    def __init__(
        self,
        repository: RepositorioVendas,
        notificador: Notificador,
        validacao: ValidacaoVenda,
        calculador: CalculadorDesconto,
    ):
        self._repository = repository
        self._notificador = notificador
        self._validacao = validacao
        self._calculador = calculador

    def processar(self, cliente: str, valor: float, email_cliente: str) -> None:
        self._validacao.validar(valor)
        valor_com_desconto = self._calculador.calcular(valor)
        self._repository.salvar(cliente, valor_com_desconto)
        
        mensagem = f"Venda de R$ {valor_com_desconto:.2f} confirmada"
        self._notificador.enviar(email_cliente, mensagem)

if __name__ == "__main__":
    repositorio = RepositorioArquivo()
    notificador = EnviadorEmail()
    validacao = ValidacaoVendaBasica()
    calculador = CalculadorDescontoPadrao()

    processador = ProcessadorVendas(
        repository=repositorio,
        notificador=notificador,
        validacao=validacao,
        calculador=calculador
    )

    processador.processar("João Silva", 150.0, "joao@email.com")
    processador.processar("Maria Souza", 50.0, "maria@email.com")

    try:
        processador.processar("Erro", -10.0, "erro@email.com")
    except ValueError as e:
        print(f"[ERRO CAPTURADO] {e}")
