letras = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}





class Damas():
    def __init__(self):
        self.tablero = [['-', 'n', '-', 'n', '-', 'n', '-', 'n'],
           ['n', '-', 'n', '-', 'n', '-', 'n', '-'],
           ['-', 'n', '-', 'n', '-', 'n', '-', 'n'],
           ['-', '-', '-', '-', '-', '-', '-', '-'],
           ['-', '-', '-', '-', '-', '-', '-', '-'],
           ['b', '-', 'b', '-', 'b', '-', 'b', '-'],
           ['-', 'b', '-', 'b', '-', 'b', '-', 'b'],
           ['b', '-', 'b', '-', 'b', '-', 'b', '-']]
        self.jugador = 'b'

    def moValido(self, jugada, colorJugador):
        """
        Comprueba si la jugada es valida
        """
        if jugada[0].upper() not in letras:
            return False
        elif jugada[2].upper() not in letras:
            return False
        elif int (jugada[1]) > 8 or int (jugada[1]) < 1:
            return False
        elif int (jugada[3]) > 8 or int (jugada[3]) < 1:
            return False
        else:
            movOrigenRow=letras[jugada[0].upper()]
            movOrigenCol=int(jugada[1])-1
            movDestinoRow=letras[jugada[2].upper()]
            movDestinoCol=int(jugada[3])-1

            if self.tablero[movOrigenRow][movOrigenCol] == 0:
                return False

            ficha = self.tablero[movOrigenRow][movOrigenCol]

            if ficha.lower() != colorJugador:
                return False

            if (ficha == 'N') or (ficha == 'B'):
                #Logica de la Reina
                numCasillas = abs (movOrigenCol - movDestinoCol)

                if numCasillas == abs (movOrigenRow - movDestinoRow):

                    for i in range(numCasillas):

                        if movDestinoRow < movOrigenRow:
                            movInterRow = movOrigenRow - (i + 1)

                            if movDestinoCol < movOrigenCol:
                                movInterCol = movOrigenCol - (i + 1)

                            else:
                                movInterCol = movOrigenCol + (i + 1)

                        else:
                            movInterRow = movOrigenRow + (i + 1)

                            if movDestinoCol < movOrigenCol:
                                movInterCol = movOrigenCol - (i + 1)

                            else:
                                movInterCol = movOrigenCol + (i + 1)

                        if ((self.tablero[movInterRow][movInterCol] != '-' and movInterCol != movDestinoCol and movInterRow != movDestinoRow)
                            or (self.tablero[movDestinoRow][movDestinoCol] == colorJugador)):
                            return False

                    return True

                else:
                    return False

            else:
                #Logica de las fichas
                #Jugada adyacente
                if ((movDestinoRow == movOrigenRow + 1 and movDestinoCol == movOrigenCol + 1) or
                        (movDestinoRow == movOrigenRow + 1 and movDestinoCol == movOrigenCol - 1) or
                        (movDestinoRow == movOrigenRow - 1 and movDestinoCol == movOrigenCol + 1) or
                        (movDestinoRow == movOrigenRow - 1 and movDestinoCol == movOrigenCol - 1)):

                    fichaDestino = self.tablero[movDestinoRow][movDestinoCol]

                    if fichaDestino == ficha:
                        #print 7
                        return False

                    elif (fichaDestino != '-') and (movDestinoCol == 0 or movDestinoCol == 7 or
                        movDestinoRow == 0 or movDestinoRow == 7):
                        return False

                    return True

                else:
                    return False

    def convertirDama(self,coordenadas, ficha):
        """
        Convierte la ficha a Reina
        """

        if (coordenadas[0] == '7') and (ficha == 'n'):
            self.tablero[int(coordenadas[0])][int(coordenadas[1])] = 'N'
        elif (coordenadas[0] == '0') and (ficha == 'b'):
            self.tablero[int(coordenadas[0])][int(coordenadas[1])] = 'B'

    def moverFicha (self,jugada, colorJugada):
        """
        Mueve la ficha y come solo una ficha
        """
        movOrigenRow=letras[jugada[0].upper()]
        movOrigenCol=int(jugada[1])-1
        movDestinoRow=letras[jugada[2].upper()]
        movDestinoCol=int(jugada[3])-1
        coordenadasFicha = ''

        fichaOrigen = self.tablero[movOrigenRow][movOrigenCol]
        fichaDestino = self.tablero [movDestinoRow][movDestinoCol]

        if fichaDestino == '-':
            self.tablero[movDestinoRow][movDestinoCol] = fichaOrigen
            self.tablero[movOrigenRow][movOrigenCol] = '-'
            coordenadasFicha = str(movDestinoRow)+str(movDestinoCol)

        elif fichaDestino.lower() != colorJugada:


            self.tablero[movOrigenRow][movOrigenCol] = '-'
            self.tablero[movDestinoRow][movDestinoCol] = '-'
            if movDestinoRow < movOrigenRow:
                if movDestinoCol < movOrigenCol:
                    if self.tablero[movDestinoRow - 1][movDestinoCol - 1] == '-':
                        self.tablero[movDestinoRow - 1][movDestinoCol - 1] = fichaOrigen
                        coordenadasFicha = str(movDestinoRow - 1) + str(movDestinoCol - 1)
                    else:
                        return False

                else:
                    if self.tablero[movDestinoRow - 1][movDestinoCol + 1] == '-':
                        self.tablero[movDestinoRow - 1][movDestinoCol + 1] = fichaOrigen
                        coordenadasFicha = str(movDestinoRow - 1) + str(movDestinoCol + 1)
                    else:
                        return False

            else:
                if movDestinoCol < movOrigenCol:
                    if self.tablero[movDestinoRow + 1][movDestinoCol - 1] == '-':
                        self.tablero[movDestinoRow + 1][movDestinoCol - 1] = fichaOrigen
                        coordenadasFicha = str(movDestinoRow + 1) + str(movDestinoCol - 1)
                    else:
                        return False

                else:
                    if self.tablero[movDestinoRow + 1][movDestinoCol + 1] == '-':
                        self.tablero[movDestinoRow + 1][movDestinoCol + 1] = fichaOrigen
                        coordenadasFicha = str(movDestinoRow + 1)+str(movDestinoCol + 1)
                    else:
                        return False
        #print 'Estas son las coordenadas de la ficha: '+coordenadasFicha
        self.convertirDama(coordenadasFicha, fichaOrigen)
        return True

    def comprobarVictoria(self):
        """
        Comprueba si ha finalizado la partida
        """
        hayNegras = False
        hayBlancas = False
        for i in self.tablero:
            for x in i:
                if x.lower() == 'n':
                    hayNegras = True
                elif x.lower() == 'b':
                    hayBlancas = True

        if hayBlancas and hayNegras:
            return False
        else:
            return True

    def display_board(self):
        board = self.tablero
        print("  ", end="")
        print()
        print(" +" + "---+" * 8)
        for row in letras:
            print(row, end="|")
            for col in range(8):
                piece = board[letras[row]][col]
                if piece is not None:
                    print(f" {piece} |", end="")
                else:
                    print("   |", end="")
            print(f" {row}")
            print(" +" + "---+" * 8)
        print("  ", end="")
        print()

    def play(self):
        print('Bienvenidos al juego de las damas')
        print ('\n')
        self.display_board()

        victoria=False

        while not victoria:

            movValido=False
            while not movValido:
                if (self.jugador == 'b'):
                    movimiento = input('Mueven las blancas: ')
                else:
                    movimiento = input('Mueven las negras: ')

                if self.moValido(movimiento, self.jugador):
                    if self.moverFicha(movimiento, self.jugador):
                        self.display_board()
                        movValido=True
                        if (self.jugador == 'n'):
                            self.jugador = 'b'
                        else:
                            self.jugador = 'n'

                        if self.comprobarVictoria():
                            if self.jugador == 'n':
                                print( '¡Ganan las Negras!')
                                victoria=True
                            else:
                                victoria=True
                                print( '¡Ganana las Blancas!')
                    else:
                        movValido = False
                        print( 'Movimiento no válido')

                else:
                    movValido = False
                    print( 'Movimiento no válido')

juego=Damas()
juego.play()