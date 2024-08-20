from modelos.avalicao import Avaliacao

class Restaurante:
    """
    Classe que representa um restaurante.
    """
    restaurantes = [] 

    def __init__(self, nome, categoria):
        """
        Inicializa uma nova instância de Restaurante.

        Args:
            nome (str): O nome do restaurante.
            categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """
        Retorna uma representação em string do restaurante.

        Returns:
            str: Nome e categoria do restaurante.
        """
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """
        Lista todos os restaurantes criados, mostrando nome, categoria, média de avaliação e status.
        """
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """
        Retorna o estado do restaurante.

        Returns:
            str: '✔️' se o restaurante estiver ativo, '❌' caso contrário.
        """
        return '✔️' if self._ativo else '❌'
    
    def alternar_estado(self):
        """
        Alterna o estado do restaurante entre ativo e inativo.
        """
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Recebe uma avaliação para o restaurante.

        Args:
            cliente (str): Nome do cliente que está avaliando.
            nota (int): Nota dada pelo cliente (deve ser entre 1 e 5).
        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        """
        Calcula e retorna a média das avaliações do restaurante.

        Returns:
            float: Média das avaliações, arredondada para uma casa decimal. Retorna "não avaliado" se não houver avaliações.
        """
        if not self._avaliacao:
            return "não avaliado"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media