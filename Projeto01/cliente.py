from tipocliente  import TipoCliente

class Cliente():
    def __init__(self, id, nome, codigo, cnpjcpf, tipo):
        self._id = id
        self._nome = nome
        self._codigo = codigo
        self._cnpjcpf = cnpjcpf
        self._tipo = tipo
        
    def str(self):
        string="\nID= {4}\nCodigo= {3}\nNome= {2}\nCNPJ/CPF= {1}\nTipo= {0}\n".format(self._tipo, self._cnpjcpf, self._codigo, self._nome, self._id)
        return string
    
if __name__ == '__main__':
    cliente=Cliente(1, "Jose Maria", 100, '200.100.345-34', TipoCliente.PESSOA_FISICA)
    print(cliente.str())