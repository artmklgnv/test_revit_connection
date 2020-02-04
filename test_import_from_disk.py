import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

doc = DocumentManager.Instance.CurrentDBDocument
app = DocumentManager.Instance.CurrentUIApplication.Application
uiapp = DocumentManager.Instance.CurrentUIApplication
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

import sys
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System.Windows.Forms import Application, Form, Label
from System.Drawing import Size, Color, Point

class IForm(Form):
    def __init__(self):
        self.BackColor = Color.LightGray
        self.CenterToScreen()
        self.Text = 'Window_text'
        self.Size = Size(200, 200)

        self.label = Label()
        self.label.Parent = self
        self.label.Text = "HELLO"
        self.label.Location = Point(75, 75)
        self.label.Size = Size(200, 200)

Application.Run(IForm())

OUT = "rererere"
