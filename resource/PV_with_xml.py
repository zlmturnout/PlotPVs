from xml.etree import ElementTree as ET
import os,sys,json,re,time,traceback
import pandas as pd
sys.path.append('.')
from collections import namedtuple
PV_info=namedtuple("PVinfo",field_names=["Beamline","Equipment","PValias","PVname","PVvalue"])

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


def add_PV_to_xml(xml_file:str,new_PVinfo:PV_info)->bool:
    """add one pv to xml

    Args:
        xml_file (string): root of the xml element
        equipment (string)): equipment to be added
        pvname (string): name of the pv to be added
        value (string): value of the pv to be added
        beamline (str, optional): beamline name,Defaults to 'Eline20U2'.
    Returns:

    """
    beamline=new_PVinfo.Beamline
    equipment=new_PVinfo.Equipment
    pv_alias=new_PVinfo.PValias
    pv_name=new_PVinfo.PVname
    pv_value=new_PVinfo.PVvalue
    eq_element=None

    try:
        DOMtree=ET.parse(xml_file)
    except Exception as e:
        print(traceback.format_exc()+e)
    else:
        xml_root=DOMtree.getroot()
        beamline_element=xml_root.find(beamline)
        pv_element=xml_root.find(f'{beamline}/{equipment}/{pv_alias}')
        print(f'find element{pv_element}')
        if isinstance(pv_element,ET.Element):
            # modify this element
            print(f'find element{pv_element}')
            pv_element.set("Name",pv_value)
            if pv_value:
                pv_element.text=pv_value
            return True
        # no exist pv_alias found
        if beamline_element:
            eq_element = xml_root.find(f'{beamline}/{equipment}')
            if eq_element is None:
                # create a new equipment element
                eq_element=ET.SubElement(beamline_element,equipment,attrib={"Catgory":"Equipment"})
        else:
            # create a new beamline element
            new_Beamline=ET.SubElement(xml_root,beamline,attrib={"Catgory":"Beamline"})
            eq_element=ET.SubElement(new_Beamline,equipment,attrib={"Catgory":"Equipment"})
        #add the PV name
        pv_set=ET.SubElement(eq_element,pv_alias,attrib={"Name":pv_name})
        if pv_value:
            pv_set.text=pv_value
        pretty_xml(xml_root, '\t', '\n')
        DOMtree.write(xml_file,encoding="utf-8",xml_declaration=True)
        return True
        
        
def read_PV_XML(xml_file,beamline='Eline20U2')->list[PV_info]:
    """read a PV XML file to dict form
    Example:
   <SSRF-Eline>
	<Eline20U2 Catgory="Beamline">
		<PGM1 Catgory="Equipment">
			<Energy_SET Name="X20U:OP:PGM1:Soft_Energy.VAL">450</Energy_SET>
			<Energy_RBV Name="X20U:OP:PGM1:Soft_Energy.RBV">450</Energy_RBV>
			<Mirror_SET Name="X20U:OP:PGM1:MR.VAL">12450</Mirror_SET>
			<Mirror_RBV Name="X20U:OP:PGM1:MR.RBV">12450</Mirror_RBV>
			<GR_SET Name="X20U:OP:PGM1:GR.VAL" />
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
    # PV_info={}
    All_PV_info=[]
    try:
        DOMtree=ET.parse(xml_file)
    except Exception as e:
        print(traceback.format_exc()+e)
    else:
        xml_root=DOMtree.getroot()
        beamline = xml_root.find(f'{beamline}')
        for beamline in xml_root:
            if beamline:
                for equipment in beamline:
                    if equipment:
                        for pv_item in equipment:
                            pv_name=pv_item.attrib.get("Name",None)
                            pv_value=pv_item.text
                            All_PV_info.append(PV_info(beamline.tag,equipment.tag,pv_item.tag,pv_name,pv_value))
        return All_PV_info

def PVinfo_To_pd(pv_info_list:list[PV_info]) ->pd.DataFrame:
    """Convert a list of pv_info read from xml file into a DataFrame
    PV_info format:
    PV_info=namedtuple("PVinfo",field_names=["Beamline","Equipment","PValias","PVname","PVvalue"])
    """
    pd_PVdata=pd.DataFrame(columns=["Beamline","Equipment","PValias","PVname","PVvalue"])
    if pv_info_list:
        for idx,pv_info in enumerate(pv_info_list):
            pd_PVdata.loc[idx]=[pv_info.Beamline,pv_info.Equipment,pv_info.PValias,pv_info.PVname,pv_info.PVvalue]
        print(f'\n{pd_PVdata}')
        return pd_PVdata


        
if __name__ == '__main__':
    
    # PVroot=ET.Element("SSRF-Eline")
    # Beamline=ET.SubElement(PVroot,"Eline20U2",attrib={"Catgory": "Beamline"})
    # equipment_PGM1=ET.SubElement(Beamline,"PGM1",attrib={"Catgory": "Equipment"})
    # PGM1_energy_set=ET.SubElement(equipment_PGM1,"Energy_SET",attrib={"Name":"X20U:OP:PGM1:Soft_Energy.VAL"})
    # PGM1_energy_set.text='450'
    # PGM1_energy_RBV=ET.SubElement(equipment_PGM1,"Energy_RBV",attrib={"Name":"X20U:OP:PGM1:Soft_Energy.RBV"})
    # PGM1_energy_RBV.text='450'
    # DOM=ET.ElementTree(PVroot)
    # DOM.write("./resource/SSRF-Eline.xml",encoding="utf-8",xml_declaration=True)
    # DOMtree=ET.parse("./resource/SSRF-Eline.xml")
    # root=DOMtree.getroot()
    # # add new element to DOM tree
    # PGM1_element=root.find("Eline20U2/PGM1")
    # for subelement in PGM1_element:
    #     print(subelement.tag)
    # PGM1_MR_set=ET.SubElement(PGM1_element,"Mirror_SET",attrib={"Name":"X20U:OP:PGM1:MR.VAL"})
    # PGM1_MR_set.text='12450'
    # PGM1_MR_RBV=ET.SubElement(PGM1_element,"Mirror_RBV",attrib={"Name":"X20U:OP:PGM1:MR.RBV"})
    # PGM1_MR_RBV.text='12450'
    # pretty_xml(root, '\t', '\n')  # 执行美化方法
    # DOMtree.write("./resource/SSRF-Eline.xml",encoding="utf-8",xml_declaration=True)
    all_pv_info=read_PV_XML("./resource/SSRF-Eline.xml")
    print(all_pv_info)
    pd_pvdata=PVinfo_To_pd(all_pv_info)

