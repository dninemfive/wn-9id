from dataclasses import dataclass
from model.ndf_base import NdfBase
from ndf_parse.model import List, MemberRow, Object
from typing import Self
from ndf_paths import DIVISIONS

@dataclass
class TDeckDivisionDescriptor(NdfBase):
    DescriptorId: str
    CfgName: str
    DivisionName: str
    DivisionPowerClassification: str
    DivisionNationalite: str
    DivisionTags: list[str]
    DescriptionHintTitleToken: str
    PackList: dict[str, int]
    MaxActivationPoints: int
    CostMatrix: dict[str, list[int]]
    EmblemTexture: str
    PortraitTexture: str
    TypeTexture: str
    CountryId: str

    def to_ndf(self: Self) -> Object:
        result = Object('TDeckDivisionDescriptor')
        result.add(MemberRow(self.DescriptorId, 'DescriptorId'))

    @staticmethod
    def from_ndf(ndf: dict[str, List]) -> Self:
        divisions: List = ndf[DIVISIONS]
