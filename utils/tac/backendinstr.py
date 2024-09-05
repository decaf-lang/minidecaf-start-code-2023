from utils.tac.reg import Reg
from utils.tac.temp import Temp
from .tacop import *
from utils.label.label import Label, LabelKind
from typing import Final, Optional

# Backend TAC instructions
class BackendInstr:
    def __init__(
        self,
        kind: InstrKind,
        dsts: list[Temp | Reg],
        srcs: list[Temp | Reg],
        label: Optional[Label],
    ) -> None:
        self.kind = kind
        self.dsts = dsts.copy()
        self.srcs = srcs.copy()
        self.label = label
    
    def isLabel(self) -> bool:
        return self.kind is InstrKind.LABEL
    
    def isSequential(self) -> bool:
        return self.kind == InstrKind.SEQ

    def isReturn(self) -> bool:
        return self.kind == InstrKind.RET
    
    def getRead(self) -> list[int]:
        return [src.index for src in self.srcs]

    def getWritten(self) -> list[int]:
        return [dst.index for dst in self.dsts]
    
    def fillRegs(self, dstRegs: list[Reg], srcRegs: list[Reg]) -> None:
        self.dsts = dstRegs
        self.srcs = srcRegs