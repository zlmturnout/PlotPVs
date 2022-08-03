from xml.etree import ElementTree as ET
import os,sys,json,re,time
sys.path.append('.')

if __name__ == '__main__':
    #DOMtree=ET.parse("as-ssd-benchSamsungSSD860EVO500GB.xml")
    
    PVroot=ET.Element("SSRF-Eline")
    Beamline=ET.SubElement(PVroot,"eline20U2",attrib={"Name": "softBranch"})
    equipment_PGM1=ET.SubElement(Beamline,"PGM1",attrib={"Name": "Monochromator"})
    PGM1_energy_set=ET.SubElement(equipment_PGM1,"Energy_SET",attrib={"Name":"SetEnergy能量设定"})
    PGM1_energy_set.text="X20U:OP:PGM1:MR.VAL"
    PGM1_energy_RBV=ET.SubElement(equipment_PGM1,"Energy_RBV",attrib={"Name":"EnergyReadBack"})
    PGM1_energy_RBV.text="X20U:OP:PGM1:MR.RBV"
    DOM=ET.ElementTree(PVroot)
    DOM.write("PVtree.xml",encoding="utf-8",xml_declaration=True)
    DOMtree=ET.parse("PVtree.xml")
    print(DOMtree)
    root=DOMtree.getroot()
    """
    #tag
    #attribute
    #text
    """
    print(root.tag,root.attrib)
    for child in root:
        for element in child:
            print(element.tag,element.attrib)
            for son in element:
                print(son.tag, son.text)
            
    
