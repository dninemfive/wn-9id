# https://realpython.com/primer-on-python-decorators/#fancy-decorators
from functools import wraps
from ndf_parse import Mod
from ndf_parse.model import List, ListRow, Map, MapRow, MemberRow, Object
from ndf_parse.model.abc import CellValue
from typing import Any, Callable, Generator
from message import Message, try_nest
import os
import shutil

MODULES_DESCRIPTORS = "ModulesDescriptors"

def get_modules_descriptors(unit: Object) -> List:
    return unit.by_member(MODULES_DESCRIPTORS).value

def get_row(unit: Object, type_or_name: str, by_name: bool) -> ListRow:
    result: ListRow | None = None
    if by_name:
        result = get_modules_descriptors(unit).by_name(type_or_name)
    else:
        for module in get_modules_descriptors(unit).match_pattern(f'{type_or_name}()'):
            result = module
            break
    if result is None:
        raise KeyError(f"Could not find module {type_or_name}{" by name" if by_name else ""} on unit {unit.by_member("ClassNameForDebug")}")
    return result

def get_module(unit: Object, module_type: str) -> ListRow | None:
    result: ListRow | None = None
    for module in unit.by_member("ModulesDescriptors").value.match_pattern(f'{module_type}()'):
        result = module
        break
    return result

def get_module_index(unit: Object, type_or_name: str, by_name: bool = False) -> int:
    return get_row(unit, type_or_name, by_name).index

def get_module(unit: Object, type_or_name: str, by_name: bool = False) -> Object:
    return get_row(unit, type_or_name, by_name).value

def replace_module(unit: Object, value: CellValue, type_or_name: str, by_name: bool = False) -> None:
    get_row(unit, type_or_name, by_name).value = value

def replace_module_from(dest_unit: Object, src_unit: Object, type_or_name: str, by_name: bool = False):
    replace_module(dest_unit, get_module(src_unit, type_or_name, by_name).copy(), type_or_name, by_name)

def append_module(dest_unit: Object, module: ListRow):
    get_modules_descriptors(dest_unit).add(module)

def append_module_from(dest_unit: Object, src_unit: Object, type_or_name: str, by_name: bool = False):
    append_module(dest_unit, get_row(src_unit, type_or_name, by_name))

def remove_module(target_unit: Object, type_or_name: str, by_name: bool = False):
    get_modules_descriptors(target_unit).remove(get_module_index(target_unit, type_or_name, by_name))

def remove_by_value(target_unit: Object, module: str):
    modules: List = get_modules_descriptors(target_unit)
    index = modules.find_by_cond(lambda x: x.value == module).index
    modules.remove(index)    

def collate_modules(ndf: List, primary_src: str, others: dict[str, list[str]]) -> List:
    raise NotImplemented
    result: List = List()
    reverse_dict = {}
    for k, l in others:
        for s in l:
            if s not in reverse_dict:
                reverse_dict[s] = k
    primary_obj = ndf.by_name(primary_src).value
    key_list: list[str] = []
    for module in get_modules_descriptors(primary_obj):
        pass