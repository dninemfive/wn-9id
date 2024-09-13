from context.module_context import ModuleContext
from context.unit_creation_context import UnitCreationContext
from metadata.division_unit_registry import UnitInfo
from ndf_parse.model import List, ListRow, Object
from utils.ndf.misc import dict_to_map, to_List
import ndf_paths as paths

def create(ctx: UnitCreationContext) -> UnitInfo | None:
    # ✪ M1010 TC3V
    with ctx.create_unit("#CMD M1010 TC3V", "US", "M35_trans_US") as m1010_tc3v: # 🏳️‍⚧️
        # acknow type = cmd
        with m1010_tc3v.module_context("TTypeUnitModuleDescriptor") as unit_type_module:
            unit_type_module.edit_members(AcknowUnitType="~/TAcknowUnitType_Command",
                                          TypeUnitFormation="'Supply'")
        # add command tags:
        #   AllowedForMissileRoE
        #   Commandant
        #   InfmapCommander
        #   Vehicule_CMD
        m1010_tc3v.add_tags("AllowedForMissileRoE", "Commandant", "InfmapCommander", "Vehicule_CMD")
        # remove "Vehicule_Transport"
        m1010_tc3v.remove_tag("Vehicule_Transport")
        vlra = ctx.ndf[paths.UNITE_DESCRIPTOR].by_name("Descriptor_Unit_VLRA_trans_FR").value
        # model of VLRA
        m1010_tc3v.replace_module_from(vlra, "ApparenceModel", by_name=True)
        m1010_tc3v.replace_module_from(vlra, 'TCadavreGeneratorModuleDescriptor')
        # damage of VLRA
        m1010_tc3v.replace_module_from(vlra, "TBaseDamageModuleDescriptor")
        # add command module
        # TODO: larger command radius than usual
        m1010_tc3v.append_module(ListRow(Object('TCommanderModuleDescriptor')))
        # remove capturable module
        # m1010_tc3v.remove_module_by_value("~/CapturableModuleDescriptor")
        m1025_cmd = ctx.ndf[paths.UNITE_DESCRIPTOR].by_name("Descriptor_Unit_M1025_Humvee_CMD_US").value
        # scanner from M1025 CMD
        m1010_tc3v.replace_module_from(m1025_cmd, 'TScannerConfigurationDescriptor')
        # remove transporter module
        m1010_tc3v.remove_module('Transporter', by_name=True)
        with m1010_tc3v.module_context('TProductionModuleDescriptor') as production_module:
            production_module.edit_members(Factory="EDefaultFactories/Logistic", 
                                           ProductionRessourcesNeeded=dict_to_map({"$/GFX/Resources/Resource_CommandPoints": str(85),
                                                                                   "$/GFX/Resources/Resource_Tickets":       str(1)}))
        # m1010_tc3v.remove_module_by_value('~/InfluenceDataModuleDescriptor')
        m1010_tc3v.append_module_from(m1025_cmd, 'TZoneInfluenceMapModuleDescriptor')
        m1010_tc3v.append_module(ListRow(Object('TInfluenceScoutModuleDescriptor')))
        m1010_tc3v.append_module(ListRow('~/InfluenceDataModuleDescriptor'))
        m1010_tc3v.replace_module_from(m1025_cmd, 'TCubeActionModuleDescriptor')
        # TODO: automatically generate new order descriptor for units
        m1010_tc3v.replace_module_from(m1025_cmd, 'TOrderConfigModuleDescriptor')
        m1010_tc3v.replace_module_from(m1025_cmd, 'TOrderableModuleDescriptor')
        m1010_tc3v.replace_module_from(m1025_cmd, 'TTacticalLabelModuleDescriptor')
        # TODO: remove last TModuleSelector (where Default = TSellModuleDescriptor())
        # TODO: upgrades from ✪ M1025 AGL
        # m1075_pls.edit_ui_module(UpgradeFromUnit="Descriptor_Unit_d9_CMD_M1025_AGL_CMD_US")
        with m1010_tc3v.module_context('TUnitUIModuleDescriptor') as ui_module:
            ui_module.remove_member('UpgradeFromUnit')
        m1010_tc3v.edit_ui_module(UnitRole="'tank_B'",
                                  SpecialtiesList=to_List("'hq_veh'", "'_leader'"),
                                  InfoPanelConfigurationToken="'Default'",
                                  MenuIconTexture="'Texture_RTS_H_CMD_veh'",
                                  TypeStrategicCount='ETypeStrategicDetailedCount/CMD_Veh',
                                  ButtonTexture="'Texture_Button_Unit_VLRA_trans_FR'")
        return UnitInfo(m1010_tc3v, 1, [0, 3, 2, 0])