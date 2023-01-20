import argparse

def main():
    # Configuration de l'analyseur d'arguments
    parser = argparse.ArgumentParser(description='Ce programme calcule la somme de deux nombres.')
    parser.add_argument('a', type=int, help='Premier nombre')
    parser.add_argument('b', type=int, help='Deuxième nombre')
    args = parser.parse_args()

    # Calcul de la somme
    result = args.a + args.b

    # Affichage du résultat
    print(f'La somme de {args.a} et {args.b} est {result}.')

if __name__ == '__main__':
    main()