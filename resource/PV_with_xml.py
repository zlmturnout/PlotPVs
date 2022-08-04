from xml.etree import ElementTree as ET
import os,sys,json,re,time,traceback
sys.path.append('.')
from collections import namedtuple
from xml.etree import ElementTree  # 导入ElementTree模块


def pretty_xml(element, indent, newline, level=0):
    """pretty the given xml root
    # elemnt为传进来的Elment类root,参数indent用于缩进,newline用于换行
   
    """
    if element:  # 判断element是否有子元素    
        if (element.text is None) or element.text.isspace():  # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
            # else:  # 此处两行如果把注释去掉，Element的text也会另起一行
            # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
    temp = list(element)  # 将element转成list
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):  # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个    
            subelement.tail = newline + indent * level
        pretty_xml(subelement, indent, newline, level=level + 1)  # 对子元素进行递归操作





def add_PV_to_xml(xml_file:str,equipment:str,pv_alias:str,pv_name:str,pv_value=None,beamline='Eline20U2')->None:
    """add one pv to xml

    Args:
        xml_file (string): root of the xml element
        equipment (string)): equipment to be added
        pvname (string): name of the pv to be added
        value (string): value of the pv to be added
        beamline (str, optional): beamline name,Defaults to 'Eline20U2'.
    Returns:

    """
    eq_element=None
    try:
        DOMtree=ET.parse(xml_file)
    except Exception as e:
        print(traceback.format_exc()+e)
    else:
        xml_root=DOMtree.getroot()
        eq_element = xml_root.find(f'{beamline}/{equipment}')
    if eq_element is not None:
        pv_set=ET.SubElement(eq_element,pv_alias,attrib={"Name":pv_name})
        pv_set.text=pv_value
        pretty_xml(xml_root, '\t', '\n')
        DOMtree.write(xml_file,encoding="utf-8",xml_declaration=True)
        
def read_PV_XML(xml_file,beamline='Eline20U2')->dict:
    """read a PV XML file to dict form
    Example:
   <SSRF-Eline>
	<Eline20U2 Name="softBranch">
		<PGM1 Name="Monochromator">
			<Energy_SET Name="X20U:OP:PGM1:Soft_Energy.VAL">450</Energy_SET>
			<Energy_RBV Name="X20U:OP:PGM1:Soft_Energy.RBV">450</Energy_RBV>
			<Mirror_SET Name="X20U:OP:PGM1:MR.VAL">12450</Mirror_SET>
			<Mirror_RBV Name="X20U:OP:PGM1:MR.RBV">12450</Mirror_RBV>
		</PGM1>
	</Eline20U2>
    </SSRF-Eline>
    read to dict:
    Eline20U2={"PGM1":{
        "Energy_SET":{"Name":"X20U:OP:PGM1:Soft_Energy.VAL","Value":"450"}}}
    Args:
        xml_file (_type_): _description_

    Returns:
        dict: example: Eline20U2=("PGM1":{"Energy_SET":{"Name":"X20U:OP:PGM1:Soft_Energy.VAL","Value":"450"}})
    """
    PV_info={}
    try:
        DOMtree=ET.parse(xml_file)
    except Exception as e:
        print(traceback.format_exc()+e)
    else:
        xml_root=DOMtree.getroot()
        beamline = xml_root.find(f'{beamline}')
    if beamline:
        equipment_list=[equipment for equipment in beamline]
        print([equipment.tag for equipment in beamline])
        for equipment in beamline:
            for pv_item in equipment:
                pv_alias=pv_item.tag    # "Energy_SET"
                pv_name=pv_item.attrib.get("Name",None)     # "X20U:OP:PGM1:Soft_Energy.VAL"
                pv_value=pv_item.text   # "450"
                pv_alias_dict={}    # {"Energy_SET":{"Name":"X20U:OP:PGM1:Soft_Energy.VAL","Value":"450"}
                pv_alias_dict["Name"]=pv_name
                pv_alias_dict["Value"]=pv_value
                pv_item_dict={}     # "PGM1":{"Energy_SET":{"Name":"X20U:OP:PGM1:Soft_Energy.VAL","Value":"450"}}
                pv_item_dict[pv_alias]=pv_alias_dict
                equipment_name=equipment.tag # "PGM1"
                PV_info[equipment_name]=pv_item_dict # final dict info
        return PV_info
                
                
        



if __name__ == '__main__':
    
    PVroot=ET.Element("SSRF-Eline")
    Beamline=ET.SubElement(PVroot,"Eline20U2",attrib={"Name": "softBranch"})
    equipment_PGM1=ET.SubElement(Beamline,"PGM1",attrib={"Name": "Monochromator"})
    PGM1_energy_set=ET.SubElement(equipment_PGM1,"Energy_SET",attrib={"Name":"X20U:OP:PGM1:Soft_Energy.VAL"})
    PGM1_energy_set.text='450'
    PGM1_energy_RBV=ET.SubElement(equipment_PGM1,"Energy_RBV",attrib={"Name":"X20U:OP:PGM1:Soft_Energy.RBV"})
    PGM1_energy_RBV.text='450'
    DOM=ET.ElementTree(PVroot)
    DOM.write("SSRF-Eline.xml",encoding="utf-8",xml_declaration=True)
    DOMtree=ET.parse("SSRF-Eline.xml")
    root=DOMtree.getroot()
    # add new element to DOM tree
    PGM1_element=root.find("Eline20U2/PGM1")
    for subelement in PGM1_element:
        print(subelement.tag)
    PGM1_MR_set=ET.SubElement(PGM1_element,"Mirror_SET",attrib={"Name":"X20U:OP:PGM1:MR.VAL"})
    PGM1_MR_set.text='12450'
    PGM1_MR_RBV=ET.SubElement(PGM1_element,"Mirror_RBV",attrib={"Name":"X20U:OP:PGM1:MR.RBV"})
    PGM1_MR_RBV.text='12450'
    pretty_xml(root, '\t', '\n')  # 执行美化方法
    DOMtree.write("SSRF-Eline.xml",encoding="utf-8",xml_declaration=True)
    pv_info=read_PV_XML("SSRF-Eline.xml")
    print(pv_info)

