import pyglet as pg
from pyglet.window import key
from cubo_magico import Cubo

janela = pg.window.Window(930, 700, visible=False, resizable=True)

def criarCubo():
    global cubo, cor1, cor2, cor3, cor4, cor5, cor6

    cubo = Cubo()

    cor1 = pg.image.SolidColorImagePattern(color=cubo.cor1)
    cor2 = pg.image.SolidColorImagePattern(color=cubo.cor2)
    cor3 = pg.image.SolidColorImagePattern(color=cubo.cor3)
    cor4 = pg.image.SolidColorImagePattern(color=cubo.cor4)
    cor5 = pg.image.SolidColorImagePattern(color=cubo.cor5)
    cor6 = pg.image.SolidColorImagePattern(color=cubo.cor6)


def renderizar():
    cubo.renderizar()
    globals()["c1"] = globals()[f"{cubo.c1}"].create_image(70, 70)
    globals()["c2"] = globals()[f"{cubo.c2}"].create_image(70, 70)
    globals()["c3"] = globals()[f"{cubo.c3}"].create_image(70, 70)
    globals()["c4"] = globals()[f"{cubo.c4}"].create_image(70, 70)
    globals()["c5"] = globals()[f"{cubo.c5}"].create_image(70, 70)
    globals()["c6"] = globals()[f"{cubo.c6}"].create_image(70, 70)
    globals()["c7"] = globals()[f"{cubo.c7}"].create_image(70, 70)
    globals()["c8"] = globals()[f"{cubo.c8}"].create_image(70, 70)
    globals()["c9"] = globals()[f"{cubo.c9}"].create_image(70, 70)
    globals()["b1"] = globals()[f"{cubo.b1}"].create_image(70, 70)
    globals()["b2"] = globals()[f"{cubo.b2}"].create_image(70, 70)
    globals()["b3"] = globals()[f"{cubo.b3}"].create_image(70, 70)
    globals()["b4"] = globals()[f"{cubo.b4}"].create_image(70, 70)
    globals()["b5"] = globals()[f"{cubo.b5}"].create_image(70, 70)
    globals()["b6"] = globals()[f"{cubo.b6}"].create_image(70, 70)
    globals()["b7"] = globals()[f"{cubo.b7}"].create_image(70, 70)
    globals()["b8"] = globals()[f"{cubo.b8}"].create_image(70, 70)
    globals()["b9"] = globals()[f"{cubo.b9}"].create_image(70, 70)
    globals()["f1"] = globals()[f"{cubo.f1}"].create_image(70, 70)
    globals()["f2"] = globals()[f"{cubo.f2}"].create_image(70, 70)
    globals()["f3"] = globals()[f"{cubo.f3}"].create_image(70, 70)
    globals()["f4"] = globals()[f"{cubo.f4}"].create_image(70, 70)
    globals()["f5"] = globals()[f"{cubo.f5}"].create_image(70, 70)
    globals()["f6"] = globals()[f"{cubo.f6}"].create_image(70, 70)
    globals()["f7"] = globals()[f"{cubo.f7}"].create_image(70, 70)
    globals()["f8"] = globals()[f"{cubo.f8}"].create_image(70, 70)
    globals()["f9"] = globals()[f"{cubo.f9}"].create_image(70, 70)
    globals()["t1"] = globals()[f"{cubo.t1}"].create_image(70, 70)
    globals()["t2"] = globals()[f"{cubo.t2}"].create_image(70, 70)
    globals()["t3"] = globals()[f"{cubo.t3}"].create_image(70, 70)
    globals()["t4"] = globals()[f"{cubo.t4}"].create_image(70, 70)
    globals()["t5"] = globals()[f"{cubo.t5}"].create_image(70, 70)
    globals()["t6"] = globals()[f"{cubo.t6}"].create_image(70, 70)
    globals()["t7"] = globals()[f"{cubo.t7}"].create_image(70, 70)
    globals()["t8"] = globals()[f"{cubo.t8}"].create_image(70, 70)
    globals()["t9"] = globals()[f"{cubo.t9}"].create_image(70, 70)
    globals()["e1"] = globals()[f"{cubo.e1}"].create_image(70, 70)
    globals()["e2"] = globals()[f"{cubo.e2}"].create_image(70, 70)
    globals()["e3"] = globals()[f"{cubo.e3}"].create_image(70, 70)
    globals()["e4"] = globals()[f"{cubo.e4}"].create_image(70, 70)
    globals()["e5"] = globals()[f"{cubo.e5}"].create_image(70, 70)
    globals()["e6"] = globals()[f"{cubo.e6}"].create_image(70, 70)
    globals()["e7"] = globals()[f"{cubo.e7}"].create_image(70, 70)
    globals()["e8"] = globals()[f"{cubo.e8}"].create_image(70, 70)
    globals()["e9"] = globals()[f"{cubo.e9}"].create_image(70, 70)
    globals()["d1"] = globals()[f"{cubo.d1}"].create_image(70, 70)
    globals()["d2"] = globals()[f"{cubo.d2}"].create_image(70, 70)
    globals()["d3"] = globals()[f"{cubo.d3}"].create_image(70, 70)
    globals()["d4"] = globals()[f"{cubo.d4}"].create_image(70, 70)
    globals()["d5"] = globals()[f"{cubo.d5}"].create_image(70, 70)
    globals()["d6"] = globals()[f"{cubo.d6}"].create_image(70, 70)
    globals()["d7"] = globals()[f"{cubo.d7}"].create_image(70, 70)
    globals()["d8"] = globals()[f"{cubo.d8}"].create_image(70, 70)
    globals()["d9"] = globals()[f"{cubo.d9}"].create_image(70, 70)


movimento = [".", "."]
def mover(sentido, addmov=True):
    if movimento[0] == ".":
        print("# Insira antes um movimento válido.")
        return
    if movimento[1] == "w": sentido += 3
    if movimento[0] == "x": cubo.x(sentido)
    elif movimento[0] == "y": cubo.y(sentido)
    elif movimento[0] == "z": cubo.z(sentido)
    elif movimento[0] == "U": cubo.U(sentido)
    elif movimento[0] == "D": cubo.D(sentido)
    elif movimento[0] == "F": cubo.F(sentido)
    elif movimento[0] == "B": cubo.B(sentido)
    elif movimento[0] == "L": cubo.L(sentido)
    elif movimento[0] == "R": cubo.R(sentido)
    elif movimento[0] == "M": cubo.M(sentido)
    elif movimento[0] == "E": cubo.E(sentido)
    elif movimento[0] == "S": cubo.S(sentido)
    if addmov:
        mov = movimento[0]+movimento[1]+str(sentido)
        try:
            cubo.movimentos[(cubo.movimentos[0]+1)] = mov
            cubo.movimentos[0] += 1
            for n in range(cubo.movimentos[0]+1, len(cubo.movimentos)):
                cubo.movimentos.pop()
        except:
            cubo.movimentos.append(mov)
            cubo.movimentos[0] += 1
    globals()["movimento"] = [".", "."]
    print(cubo.movimentos)
    renderizar()


def voltar():
    n_mov = cubo.movimentos[0]
    if n_mov < 1:
        print("# Impossível voltar movimento.")
        return
    mov = cubo.movimentos[n_mov]
    globals()["movimento"][0] = mov[0]
    globals()["movimento"][1] = mov[1]
    mov_s = int(mov[2])
    if mov_s == 0 or mov_s == 1:
        mov_s = (mov_s + 1) % 2
    elif mov_s == 3 or mov_s == 4:
        mov_s -= 3
        mov_s = ((mov_s + 1) % 2) + 3
    cubo.movimentos[0] -= 1
    mover(mov_s, False)


def avancar():
    n_mov = cubo.movimentos[0]
    try:
        mov = cubo.movimentos[n_mov + 1]
    except:
        print("# Impossível avançar.")
        return
    globals()["movimento"][0] = mov[0]
    globals()["movimento"][1] = mov[1]
    cubo.movimentos[0] += 1
    mover(int(mov[2]), False)


def resetar():
    del globals()["cubo"]
    criarCubo()
    globals()["movimento"] = [".", "."]
    renderizar()
    print("# Cubo resetado.")


def sair():
    print("# Saindo. (Pressionado 'ESC')")
    pg.app.exit()


@janela.event
def on_draw():
    janela.clear()

    c1.blit(240, 470)
    c2.blit(315, 470)
    c3.blit(390, 470)
    c4.blit(240, 545)
    c5.blit(315, 545)
    c6.blit(390, 545)
    c7.blit(240, 620)
    c8.blit(315, 620)
    c9.blit(390, 620)
    b1.blit(240, 10)
    b2.blit(315, 10)
    b3.blit(390, 10)
    b4.blit(240, 85)
    b5.blit(315, 85)
    b6.blit(390, 85)
    b7.blit(240, 160)
    b8.blit(315, 160)
    b9.blit(390, 160)
    f1.blit(240, 240)
    f2.blit(315, 240)
    f3.blit(390, 240)
    f4.blit(240, 315)
    f5.blit(315, 315)
    f6.blit(390, 315)
    f7.blit(240, 390)
    f8.blit(315, 390)
    f9.blit(390, 390)
    t1.blit(700, 240)
    t2.blit(775, 240)
    t3.blit(850, 240)
    t4.blit(700, 315)
    t5.blit(775, 315)
    t6.blit(850, 315)
    t7.blit(700, 390)
    t8.blit(775, 390)
    t9.blit(850, 390)
    e1.blit(10, 240)
    e2.blit(85, 240)
    e3.blit(160, 240)
    e4.blit(10, 315)
    e5.blit(85, 315)
    e6.blit(160, 315)
    e7.blit(10, 390)
    e8.blit(85, 390)
    e9.blit(160, 390)
    d1.blit(470, 240)
    d2.blit(545, 240)
    d3.blit(620, 240)
    d4.blit(470, 315)
    d5.blit(545, 315)
    d6.blit(620, 315)
    d7.blit(470, 390)
    d8.blit(545, 390)
    d9.blit(620, 390)


@janela.event
def on_key_press(symbol, modifiers):
    if symbol == key._0: mover(0)
    elif symbol == key._1: mover(1)
    elif symbol == key._2: mover(2)
    elif symbol == key.X: globals()["movimento"][0] = "x"
    elif symbol == key.Y: globals()["movimento"][0] = "y"
    elif symbol == key.Z: globals()["movimento"][0] = "z"
    elif symbol == key.U: globals()["movimento"][0] = "U"
    elif symbol == key.D: globals()["movimento"][0] = "D"
    elif symbol == key.F: globals()["movimento"][0] = "F"
    elif symbol == key.B: globals()["movimento"][0] = "B"
    elif symbol == key.L: globals()["movimento"][0] = "L"
    elif symbol == key.R: globals()["movimento"][0] = "R"
    elif symbol == key.M: globals()["movimento"][0] = "M"
    elif symbol == key.E: globals()["movimento"][0] = "E"
    elif symbol == key.S: globals()["movimento"][0] = "S"
    elif symbol == key.W: globals()["movimento"][0] = "w"
    elif symbol == key.MOTION_LEFT: voltar()
    elif symbol == key.MOTION_RIGHT: avancar()
    elif symbol == key.ESCAPE: sair()
    elif symbol == key.BACKSPACE: resetar()
    else: print("# Comando inválido")


if __name__ == "__main__":
    criarCubo()
    renderizar()
    janela.set_caption("Cubo Mágico - 2D")
    janela.set_minimum_size(930, 700)
    janela.set_visible()
    pg.app.run()
    
