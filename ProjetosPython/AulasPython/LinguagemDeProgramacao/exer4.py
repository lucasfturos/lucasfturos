# Faça um programa, em linguagem Python, para calcular a área e o perímetro de um hexágo-
# no. O programa deve implementar uma função chamada calc_hexa que calcula a área e o perí-
# metro de um hexágono regular de lado L. O programa deve solicitar ao usuário o lado do polí-
# gono, calcular e imprimir a área e o perímetro do polígono. O programa termina quando for
# digitado um valor negativo qualquer para o lado. A função deve obedecer ao seguinte protóti-
# po:
# void calc_hexa(float L, float *area, float *perimetro);
# Lembrando que a área e o perímetro de um hexágono regular são dados por:
import math as m


def calc_hexa(l):
    perimetro = 6 * l
    area = (3 * l**2 * m.sqrt(3)) / 2
    return area, perimetro


lado = float(input("Informe o valor do lado do Hexágono: "))
area, perimetro = calc_hexa(lado)
print("O hexagono tem de area : %.2f e de perimetro: %.2f\n" % (area, perimetro))
