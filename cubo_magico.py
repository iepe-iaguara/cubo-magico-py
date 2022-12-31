class Cubo:
    def __init__(s,
                c=(255, 255, 255, 1),
                b=(255, 210, 0, 1),
                f=(0, 180, 20, 1),
                t=(0, 70, 180, 1),
                e=(255, 70, 0, 1),
                d=(185, 0, 0, 1)):

## Cores, essas variáveis não mudam
        s.cor1 = c
        s.cor2 = b
        s.cor3 = f
        s.cor4 = t
        s.cor5 = e
        s.cor6 = d

## Variáveis para a renderização
        s.c1 = s.c2 = s.c3 = s.c4 = s.c5 = s.c6 = s.c7 = s.c8 = s.c9 = "cor1"
        s.b1 = s.b2 = s.b3 = s.b4 = s.b5 = s.b6 = s.b7 = s.b8 = s.b9 = "cor2"
        s.f1 = s.f2 = s.f3 = s.f4 = s.f5 = s.f6 = s.f7 = s.f8 = s.f9 = "cor3"
        s.t1 = s.t2 = s.t3 = s.t4 = s.t5 = s.t6 = s.t7 = s.t8 = s.t9 = "cor4"
        s.e1 = s.e2 = s.e3 = s.e4 = s.e5 = s.e6 = s.e7 = s.e8 = s.e9 = "cor5"
        s.d1 = s.d2 = s.d3 = s.d4 = s.d5 = s.d6 = s.d7 = s.d8 = s.d9 = "cor6"

### Posições

## Centros
        s.cima = "cor1"
        s.baixo = "cor2"
        s.frente = "cor3"
        s.tras = "cor4"
        s.esquerda = "cor5"
        s.direita = "cor6"

## Cantos ABC (cima ou baixo antes, e então sentido horário das faces)
## forma lista de cores em sentido horário do canto e o quarto item (index 3)
## diz o index de qual cor da lista está na face de cima/baixo.
## Usar a função cantos() para ajustar a orientação.
        s.ULB = [s.cima, s.esquerda, s.tras, 0]
        s.UBR = [s.cima, s.tras, s.direita, 0]
        s.URF = [s.cima, s.direita, s.frente, 0]
        s.UFL = [s.cima, s.frente, s.esquerda, 0]
        s.DLF = [s.baixo, s.esquerda, s.frente, 0]
        s.DFR = [s.baixo, s.frente, s.direita, 0]
        s.DRB = [s.baixo, s.direita, s.tras, 0]
        s.DBL = [s.baixo, s.tras, s.esquerda, 0]

## Meios AB (cima/baixo antes ou esquerda/direita depois)
## forma lista de duas cores no mesmo sentido. O terceiro item (2) diz
## qual cor (0 ou 1) fica com a face de cima/baixo ou da frente/tras.
## O quarto item (3) diz se a cor citada no outro item for com a de cima/baixo
## ou com a da frente/tras (1 para cima/baixo e 0 para frente/tras).
## Usar a função meios() para ajustar o terceiro item (2).
        s.UB = [s.cima, s.tras, 0, 1]
        s.UR = [s.cima, s.direita, 0, 1]
        s.UF = [s.cima, s.frente, 0, 1]
        s.UL = [s.cima, s.esquerda, 0, 1]
        s.DF = [s.baixo, s.frente, 0, 1]
        s.DR = [s.baixo, s.direita, 0, 1]
        s.DB = [s.baixo, s.tras, 0, 1]
        s.DL = [s.baixo, s.esquerda, 0, 1]
        s.BL = [s.tras, s.esquerda, 0, 0]
        s.BR = [s.tras, s.direita, 0, 0]
        s.FR = [s.frente, s.direita, 0, 0]
        s.FL = [s.frente, s.esquerda, 0, 0]


### Movimentos

## Rotações
    def x(s, i): # direção da direita
        if i == 0: # x
            s.M(1)
            s.L(1)
            s.R(0)
        elif i == 1: # x'
            s.M(0)
            s.L(0)
            s.R(1)
        elif i == 2: # x2
            s.M(2)
            s.L(2)
            s.R(2)
        else:
            print("Erro: Valor inserido à função x() é inválido.")

    def y(s, i): # direção de cima
        if i == 0: # y
            s.E(1)
            s.U(0)
            s.D(1)
        elif i == 1: # y'
            s.E(0)
            s.U(1)
            s.D(0)
        elif i == 2: # y2
            s.E(2)
            s.U(2)
            s.D(2)
        else:
            print("Erro: Valor inserido à função y() é inválido.")

    def z(s, i): # direção da frente
        if i == 0: # z
            s.S(0)
            s.F(0)
            s.B(1)
        elif i == 1: # z'
            s.S(1)
            s.F(1)
            s.B(0)
        elif i == 2: # z2
            s.S(2)
            s.F(2)
            s.B(2)
        else:
            print("Erro: Valor inserido à função z() é inválido.")


## Faces
    def U(s, i):
        if i == 0: # U
            s.ULB, s.UBR, s.URF, s.UFL = s.UFL, s.ULB, s.UBR, s.URF
            s.UB, s.UR, s.UF, s.UL = s.UL, s.UB, s.UR, s.UF
        elif i == 1: # U'
            s.ULB, s.UBR, s.URF, s.UFL = s.UBR, s.URF, s.UFL, s.ULB
            s.UB, s.UR, s.UF, s.UL = s.UR, s.UF, s.UL, s.UB
        elif i == 2: # U2
            s.ULB, s.UBR, s.URF, s.UFL = s.URF, s.UFL, s.ULB, s.UBR
            s.UB, s.UR, s.UF, s.UL = s.UF, s.UL, s.UB, s.UR
        elif i == 3: # Uw
            s.U(0)
            s.E(1)
        elif i == 4: # Uw'
            s.U(1)
            s.E(0)
        elif i == 5: # Uw2
            s.U(2)
            s.E(2)
        else:
            print("Erro: Valor inserido à função U() é inválido.")

    def D(s, i):
        if i == 0: # D
            s.DLF, s.DFR, s.DRB, s.DBL = s.DBL, s.DLF, s.DFR, s.DRB
            s.DF, s.DR, s.DB, s.DL = s.DL, s.DF, s.DR, s.DB
        elif i == 1: # D'
            s.DLF, s.DFR, s.DRB, s.DBL = s.DFR, s.DRB, s.DBL, s.DLF
            s.DF, s.DR, s.DB, s.DL = s.DR, s.DB, s.DL, s.DF
        elif i == 2: # D2
            s.DLF, s.DFR, s.DRB, s.DBL = s.DRB, s.DBL, s.DLF, s.DFR
            s.DF, s.DR, s.DB, s.DL = s.DB, s.DL, s.DF, s.DR
        elif i == 3: # Dw
            s.D(0)
            s.E(0)
        elif i == 4: # Dw'
            s.D(1)
            s.E(1)
        elif i == 5: # Dw2
            s.D(2)
            s.E(2)
        else:
            print("Erro: Valor inserido à função D() é inválido.")

    def F(s, i):
        if i == 0: # F
            s.UFL, s.URF, s.DFR, s.DLF = s.DLF, s.UFL, s.URF, s.DFR
            s.cantos(s.UFL, s.URF, s.DFR, s.DLF, 1, 2, 1, 2)
            s.UF, s.FR, s.DF, s.FL = s.FL, s.UF, s.FR, s.DF
            s.meios(s.UF, s.FR, s.DF, s.FL, 1, 1, 1, 1)
            s.UF[3], s.FR[3], s.DF[3], s.FL[3] = 1, 0, 1, 0
        elif i == 1: # F'
            s.UFL, s.URF, s.DFR, s.DLF = s.URF, s.DFR, s.DLF, s.UFL
            s.cantos(s.UFL, s.URF, s.DFR, s.DLF, 1, 2, 1, 2)
            s.UF, s.FR, s.DF, s.FL = s.FR, s.DF, s.FL, s.UF
            s.meios(s.UF, s.FR, s.DF, s.FL, 1, 1, 1, 1)
            s.UF[3], s.FR[3], s.DF[3], s.FL[3] = 1, 0, 1, 0
        elif i == 2: # F2
            s.UFL, s.URF, s.DFR, s.DLF = s.DFR, s.DLF, s.UFL, s.URF
            s.UF, s.FR, s.DF, s.FL = s.DF, s.FL, s.UF, s.FR
        elif i == 3: # Fw
            s.F(0)
            s.S(0)
        elif i == 4: # Fw'
            s.F(1)
            s.S(1)
        elif i == 5: # Fw2
            s.F(2)
            s.S(2)
        else:
            print("Erro: Valor inserido à função F() é inválido.")

    def B(s, i):
        if i == 0: # B
            s.UBR, s.ULB, s.DBL, s.DRB = s.DRB, s.UBR, s.ULB, s.DBL
            s.cantos(s.UBR, s.ULB, s.DBL, s.DRB, 1, 2, 1, 2)
            s.UB, s.BL, s.DB, s.BR = s.BR, s.UB, s.BL, s.DB
            s.meios(s.UB, s.BL, s.DB, s.BR, 1, 1, 1, 1)
            s.UB[3], s.BL[3], s.DB[3], s.BR[3] = 1, 0, 1, 0
        elif i == 1: # B'
            s.UBR, s.ULB, s.DBL, s.DRB = s.ULB, s.DBL, s.DRB, s.UBR
            s.cantos(s.UBR, s.ULB, s.DBL, s.DRB, 1, 2, 1, 2)
            s.UB, s.BL, s.DB, s.BR = s.BL, s.DB, s.BR, s.UB
            s.meios(s.UB, s.BL, s.DB, s.BR, 1, 1, 1, 1)
            s.UB[3], s.BL[3], s.DB[3], s.BR[3] = 1, 0, 1, 0
        elif i == 2: # B2
            s.UBR, s.ULB, s.DBL, s.DRB = s.DBL, s.DRB, s.UBR, s.ULB
            s.UB, s.BL, s.DB, s.BR = s.DB, s.BR, s.UB, s.BL
        elif i == 3: # Bw
            s.B(0)
            s.S(1)
        elif i == 4: # Bw'
            s.B(1)
            s.S(0)
        elif i == 5: # Bw2
            s.B(2)
            s.S(2)
        else:
            print("Erro: Valor inserido à função B() é inválido.")

    def L(s, i):
        if i == 0: # L
            s.ULB, s.UFL, s.DLF, s.DBL = s.DBL, s.ULB, s.UFL, s.DLF
            s.cantos(s.ULB, s.UFL, s.DLF, s.DBL, 1, 2, 1, 2)
            s.UL, s.FL, s.DL, s.BL = s.BL, s.UL, s.FL, s.DL
            s.UL[3], s.FL[3], s.DL[3], s.BL[3] = 1, 0, 1, 0
        elif i == 1: # L'
            s.ULB, s.UFL, s.DLF, s.DBL = s.UFL, s.DLF, s.DBL, s.ULB
            s.cantos(s.ULB, s.UFL, s.DLF, s.DBL, 1, 2, 1, 2)
            s.UL, s.FL, s.DL, s.BL = s.FL, s.DL, s.BL, s.UL
            s.UL[3], s.FL[3], s.DL[3], s.BL[3] = 1, 0, 1, 0
        elif i == 2: # L2
            s.ULB, s.UFL, s.DLF, s.DBL = s.DLF, s.DBL, s.ULB, s.UFL
            s.UL, s.FL, s.DL, s.BL = s.DL, s.BL, s.UL, s.FL
        elif i == 3: # Lw
            s.L(0)
            s.M(0)
        elif i == 4: # Lw'
            s.L(1)
            s.M(1)
        elif i == 5: # Lw2
            s.L(2)
            s.M(2)
        else:
            print("Erro: Valor inserido à função L() é inválido.")

    def R(s, i):
        if i == 0: # R
            s.URF, s.UBR, s.DRB, s.DFR = s.DFR, s.URF, s.UBR, s.DRB
            s.cantos(s.URF, s.UBR, s.DRB, s.DFR, 1, 2, 1, 2)
            s.UR, s.BR, s.DR, s.FR = s.FR, s.UR, s.BR, s.DR
            s.UR[3], s.BR[3], s.DR[3], s.FR[3] = 1, 0, 1, 0
        elif i == 1: # R'
            s.URF, s.UBR, s.DRB, s.DFR = s.UBR, s.DRB, s.DFR, s.URF
            s.cantos(s.URF, s.UBR, s.DRB, s.DFR, 1, 2, 1, 2)
            s.UR, s.BR, s.DR, s.FR = s.BR, s.DR, s.FR, s.UR
            s.UR[3], s.BR[3], s.DR[3], s.FR[3] = 1, 0, 1, 0
        elif i == 2: # R2
            s.URF, s.UBR, s.DRB, s.DFR = s.DRB, s.DFR, s.URF, s.UBR
            s.UR, s.BR, s.DR, s.FR = s.DR, s.FR, s.UR, s.BR
        elif i == 3: # Rw
            s.R(0)
            s.M(1)
        elif i == 4: # Rw'
            s.R(1)
            s.M(0)
        elif i == 5: # Rw2
            s.R(2)
            s.M(2)
        else:
            print("Erro: Valor inserido à função R() é inválido.")


## Slices
    def M(s, i): # direção da esquerda
        if i == 0: # M
            s.cima, s.frente, s.baixo, s.tras = s.tras, s.cima, s.frente, s.baixo
            s.UB, s.UF, s.DF, s.DB = s.UF, s.DF, s.DB, s.UB
            s.UB[2], s.UF[2], s.DF[2], s.DB[2] = 1, 1, 1, 1
        elif i == 1: # M'
            s.cima, s.frente, s.baixo, s.tras = s.frente, s.baixo, s.tras, s.cima
            s.UB, s.UF, s.DF, s.DB = s.DB, s.UB, s.UF, s.DF
            s.UB[2], s.UF[2], s.DF[2], s.DB[2] = 1, 1, 1, 1
        elif i == 2: # M2
            s.cima, s.frente, s.baixo, s.tras = s.baixo, s.tras, s.cima, s.frente
            s.UB, s.UF, s.DF, s.DB = s.DF, s.DB, s.UB, s.UF
        else:
            print("Erro: Valor inserido à função M() é inválido.")

    def E(s, i): # direção de baixo
        if i == 0: # E
            s.frente, s.direita, s.tras, s.esquerda = s.esquerda, s.frente, s.direita, s.tras
            s.FL, s.FR, s.BR, s.BL = s.BL, s.FL, s.FR, s.BR
            s.FL[2], s.FR[2], s.BR[2], s.BL[2] = 1, 1, 1, 1
        elif i == 1: # E'
            s.frente, s.direita, s.tras, s.esquerda = s.direita, s.tras, s.esquerda, s.frente
            s.FL, s.FR, s.BR, s.BL = s.FR, s.BR, s.BL, s.FL
            s.FL[2], s.FR[2], s.BR[2], s.BL[2] = 1, 1, 1, 1
        elif i == 2: # E2
            s.frente, s.direita, s.tras, s.esquerda = s.tras, s.esquerda, s.frente, s.direita
            s.FL, s.FR, s.BR, s.BL = s.BR, s.BL, s.FL, s.FR
        else:
            print("Erro: Valor inserido à função E() é inválido.")

    def S(s, i): # direção da frente
        if i == 0: # S
            s.cima, s.direita, s.baixo, s.esquerda = s.esquerda, s.cima, s.direita, s.baixo
            s.UL, s.UR, s.DR, s.DL = s.DL, s.UL, s.UR, s.DR
            s.UL[2], s.UR[2], s.DR[2], s.DL[2] = 1, 1, 1, 1
        elif i == 1: # S'
            s.cima, s.direita, s.baixo, s.esquerda = s.direita, s.baixo, s.esquerda, s.cima
            s.UL, s.UR, s.DR, s.DL = s.UR, s.DR, s.DL, s.UL
            s.UL[2], s.UR[2], s.DR[2], s.DL[2] = 1, 1, 1, 1
        elif i == 2: # S2
            s.cima, s.direita, s.baixo, s.esquerda = s.baixo, s.esquerda, s.cima, s.direita
            s.UL, s.UR, s.DR, s.DL = s.DR, s.DL, s.UL, s.UR
        else:
            print("Erro: Valor inserido à função S() é inválido.")

## Funções de orientação
# Os valores dos nX se adicionam ao index para que orientem de forma correta
# O módulo de três é usado pois os cantos têm três cores
    def cantos(s, canto0, canto1, canto2, canto3, n0, n1, n2, n3):
        canto0[3] = (canto0[3] + n0) % 3
        canto1[3] = (canto1[3] + n1) % 3
        canto2[3] = (canto2[3] + n2) % 3
        canto3[3] = (canto3[3] + n3) % 3

# Análogo aos cantos, o quarto item do meio é responsabilidade dos movimentos
    def meios(s, meio0, meio1, meio2, meio3, n0, n1, n2, n3):
        meio0[2] = (meio0[2] + n0) % 2
        meio1[2] = (meio1[2] + n1) % 2
        meio2[2] = (meio2[2] + n2) % 2
        meio3[2] = (meio3[2] + n3) % 2


## Função de renderização
    def renderizar(s):
        # Centros
        s.c5 = s.cima
        s.b5 = s.baixo
        s.f5 = s.frente
        s.t5 = s.tras
        s.e5 = s.esquerda
        s.d5 = s.direita

        # Cantos
        i = s.ULB[3]
        s.c7, s.e7, s.t9 = s.ULB[i], s.ULB[(i+1)%3], s.ULB[(i+2)%3]

        i = s.UBR[3]
        s.c9, s.t7, s.d9 = s.UBR[i], s.UBR[(i+1)%3], s.UBR[(i+2)%3]

        i = s.URF[3]
        s.c3, s.d7, s.f9 = s.URF[i], s.URF[(i+1)%3], s.URF[(i+2)%3]

        i = s.UFL[3]
        s.c1, s.f7, s.e9 = s.UFL[i], s.UFL[(i+1)%3], s.UFL[(i+2)%3]

        i = s.DLF[3]
        s.b7, s.e3, s.f1 = s.DLF[i], s.DLF[(i+1)%3], s.DLF[(i+2)%3]

        i = s.DFR[3]
        s.b9, s.f3, s.d1 = s.DFR[i], s.DFR[(i+1)%3], s.DFR[(i+2)%3]

        i = s.DRB[3]
        s.b3, s.d3, s.t1 = s.DRB[i], s.DRB[(i+1)%3], s.DRB[(i+2)%3]

        i = s.DBL[3]
        s.b1, s.t3, s.e1 = s.DBL[i], s.DBL[(i+1)%3], s.DBL[(i+2)%3]

        # Meios
        i, j = s.UB[2], s.UB[3]
        if j == 1:
            s.c8, s.t8 = s.UB[i], s.UB[(i+1)%2]
        else:
            s.c8, s.t8 = s.UB[(i+1)%2], s.UB[i]

        i = s.UR[2]
        s.c6, s.d8 = s.UR[i], s.UR[(i+1)%2]

        i, j = s.UF[2], s.UF[3]
        if j == 1:
            s.c2, s.f8 = s.UF[i], s.UF[(i+1)%2]
        else:
            s.c2, s.f8 = s.UF[(i+1)%2], s.UF[i]

        i = s.UL[2]
        s.c4, s.e8 = s.UL[i], s.UL[(i+1)%2]

        i, j = s.DF[2], s.DF[3]
        if j == 1:
            s.b8, s.f2 = s.DF[i], s.DF[(i+1)%2]
        else:
            s.b8, s.f2 = s.DF[(i+1)%2], s.DF[i]

        i = s.DR[2]
        s.b6, s.d2 = s.DR[i], s.DR[(i+1)%2]

        i, j = s.DB[2], s.DB[3]
        if j == 1:
            s.b2, s.t2 = s.DB[i], s.DB[(i+1)%2]
        else:
            s.b2, s.t2 = s.DB[(i+1)%2], s.DB[i]

        i = s.DL[2]
        s.b4, s.e2 = s.DL[i], s.DL[(i+1)%2]

        i = s.BL[2]
        s.t6, s.e4 = s.BL[i], s.BL[(i+1)%2]

        i = s.BR[2]
        s.t4, s.d6 = s.BR[i], s.BR[(i+1)%2]

        i = s.FR[2]
        s.f6, s.d4 = s.FR[i], s.FR[(i+1)%2]

        i = s.FL[2]
        s.f4, s.e6 = s.FL[i], s.FL[(i+1)%2]


### Rodar

def main():
    pass

if __name__ == "__main__":
    main()
