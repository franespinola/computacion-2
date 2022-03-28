import argparse

parser = argparse.ArgumentParser(description="ejemplo parser")

parser.add_argument("-i", "--file", type=str, required=False, help="string")
parser.add_argument("-o", "--size", type=int, default=1024, help="numero")
args = parser.parse_args()


