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
