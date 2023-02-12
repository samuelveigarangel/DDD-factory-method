# Fazendo uso de singletons no nível de módulos

import aula03_modulo as mm
import aula03_modulo


print(f'O nome é {aula03_modulo.NOME}')


aula03_modulo.funcao1()


mm.funcao2()
