class Figura:
    # Función para calcular el área de un rectángulo
    def areaDelRectangulo(self, lado1, lado2):
        result = lado1 * lado2
        return result

    # Función para calcular el área de un triángulo
    def g(self, b, h):
        r = 0.5 * b * h
        return r

    # Función principalS
    def main(self):
        x = 4
        y = 6
        rect_area = self(x, y)
        print("Área del rectángulo:", areaDelRectangulo)

        base = 5
        altura = 8
        tri_area = self.g(base, altura)
        print("Área del triángulo:", tri_area)

if __name__ == '__main__':
    figura = Figura()
    figura.main()