
import lldb

class PointPrinter:
    """Pretty-printer for Point objects."""

    def __init__(self, valobj, internal_dict):
        self.valobj = valobj
        self.internal_dict = internal_dict

    def to_string(self):
        x = self.valobj.GetChildMemberWithName('x').GetValueAsSigned()
        y = self.valobj.GetChildMemberWithName('y').GetValueAsSigned()
        return f"Point(x={x}, y={y})"

def __lldb_init_module(debugger, internal_dict):
    print("Initializing pretty printer")
    debugger.HandleCommand('type summary add -F lldb_printer.PointPrinter Point')

