from typing import Optional

from utils.label.label import Label
from utils.tac.reg import Reg

from .tacop import InstrKind


class AsmInstr:
    def __init__(
        self,
        kind: InstrKind,
        instrString: Optional[str] = None,
    ) -> None:
        self.kind = kind
        self.instrString = instrString

    def __str__(self) -> str:
        assert self.instrString is not None
        return self.instrString

    def isLabel(self) -> bool:
        return self.kind == InstrKind.LABEL

    def isSequential(self) -> bool:
        return self.kind == InstrKind.SEQ

    def isReturn(self) -> bool:
        return self.kind == InstrKind.RET
