# mapping text size from one reference to others

#select element
from Autodesk.Revit.DB import Transaction, Reference, FilteredElementCollector, TextNote
uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

selection = uidoc.Selection
elementId = selection.GetElementIds()

print(elementId[0])
element = doc.GetElement(elementId[0])
print(element)

box = element.get_BoundingBox(doc.ActiveView)
#elementId2 = ElementId(8688035)
elementId2 = doc.ActiveView.Id

print(elementId2)

print(box.Max)
print(box.Min)
newBoundsMin = XYZ(0,0,0)
newBoundsMax = XYZ(10,0,0)
box.Bounds[0] = newBoundsMin
box.Bounds[1] = newBoundsMax

print(box.Max)
print(box.Min)
typeId = element.GetTypeId()

print(typeId)

max_width = element.GetMaximumAllowedWidth()
print(max_width)
t = Transaction(doc)
t.Start('create text in current view')
newnote = TextNote.Create(doc,elementId2,XYZ(0,0,0),max_width,"new note",typeId)
t.Commit()