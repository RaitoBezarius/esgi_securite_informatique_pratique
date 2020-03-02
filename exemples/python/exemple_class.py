class A:
    pass

class B:
    def que_suis_je(self):
        raise NotImplementedError("B ne pense pas, donc n'est pas!")

class C:
    pass

class VoiciUnExemple(A, B, C):
    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        self._un_arg = 3
        self.__deux_args = 5
        self.args = args
        self.kwargs = kwargs

    def que_suis_je(self):
        return 'Un exemple'

    def __add__(self, other):
        return VoiciUnExemple(2 + self.kwargs.get('ajoute', 5))

U = VoiciUnExemple(ajoute=3)
V = U + U
W = V + V

print(V.args[0])
