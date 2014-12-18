from math import factorial, floor
from sys import argv

def calculate_layer(current_layer, layers):
    layer = []

    for x in range(0, current_layer + 1):
        layer.append(floor(factorial(layers) / (factorial(current_layer - x) * factorial(layers - current_layer) * factorial(x))))

    return layer


def calculate_pyramid(input_layers):
    pyramid = []
    layers = int(input_layers) - 1

    for layer in range(0, layers + 1):
        new_layer = calculate_layer(layer, layers)
        pyramid.append(new_layer)

    return pyramid


def print_pyramid(pyramid):
    for layer in pyramid:
        print (' '.join(map(str, layer)))


script, input_layers = argv
pyramid = calculate_pyramid(input_layers)
print_pyramid(pyramid)