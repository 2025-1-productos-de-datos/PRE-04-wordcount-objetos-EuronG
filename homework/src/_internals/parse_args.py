import sys


class ParseArgsMixin:

    def parse_args(self):
        if len(sys.argv) != 3:
            print("Error args amount")
            sys.exit(1)

        self.input_folder = sys.argv[1]
        self.output_folder = sys.argv[2]
