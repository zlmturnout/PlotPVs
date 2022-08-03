from xml.etree import ElementTree as ET
import os,sys,json,re,time
sys.path.append('.')



if __name__ == '__main__':
    
    PVroot=ET.Element("SSRF-Eline")
    Beamline=ET.SubElement(PVroot,"eline20U2",attrib={"Name": "softBranch"})
    equipment_PGM1=ET.SubElement(Beamline,"PGM1",attrib={"Name": "Monochromator"})
    PGM1_energy_set=ET.SubElement(equipment_PGM1,"Energy_SET",attrib={"Name":"SetEnergy能量设定"})
    PGM1_energy_set.text="X20U:OP:PGM1:Soft_Energy.VAL"
    PGM1_energy_RBV=ET.SubElement(equipment_PGM1,"Energy_RBV",attrib={"Name":"EnergyReadBack"})
    PGM1_energy_RBV.text="X20U:OP:PGM1:Soft_Energy.RBV"
    DOM=ET.ElementTree(PVroot)
    DOM.write("SSRF-Eline.xml",encoding="utf-8",xml_declaration=True)
    DOMtree=ET.parse("SSRF-Eline.xml")
    root=DOMtree.getroot()
    # add new element to DOM tree
    PGM1_element=root.find("eline20U2/PGM1")
    PGM1_MR_set=ET.SubElement(PGM1_element,"Mirror_SET",attrib={"Name":"SetMirror能量设定"})
    PGM1_MR_set.text="X20U:OP:PGM1:MR.VAL"
    PGM1_MR_RBV=ET.SubElement(PGM1_element,"Mirror_RBV",attrib={"Name":"MirrorReadBack"})
    PGM1_MR_RBV.text="X20U:OP:PGM1:MR.RBV"
    DOMtree.write("SSRF-Eline.xml",encoding="utf-8",xml_declaration=True)

