
import gdb

class PointPrinter:
    """Pretty-printer for Point objects."""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        x = self.val['x']
        y = self.val['y']
        return f"Point(x={x}, y={y})"

def build_pretty_printer():
    # Crée une instance de PrettyPrinter
    pp = gdb.printing.RegexpCollectionPrettyPrinter("example")
    # Ajoute un pretty printer pour le type 'Point'
    pp.add_printer('Point', '^Point$', PointPrinter)
    return pp

# Enregistre le pretty printer pour l'objet actuellement chargé
gdb.printing.register_pretty_printer(gdb.current_objfile(), build_pretty_printer())
