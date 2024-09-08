from utils.tac.backendinstr import BackendInstr

"""
Loc: line of code
"""


class Loc:
    def __init__(self, instr: BackendInstr) -> None:
        self.instr = instr
        self.liveIn: set[int] = set()
        self.liveOut: set[int] = set()
