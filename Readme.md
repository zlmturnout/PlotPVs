# Monitor PV names

## Basic strategy

1. python+pyepics+Qt6+matplotlib
2. one dialog for each pv name
3. monitor  pv value vs timestamp/changed Num
4. save all recorded data into multiple file types (xlsx,csv,txt,sqlitebase)

## XML support

**purpose:**

1. add PV names to XML file
2. Read XML file to acquire all stored PV names
3. Save all PV status according to XML file

xml structure

```xml
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
```
