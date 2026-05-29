import omni.usd
from pxr import UsdGeom, Gf

stage = omni.usd.get_context().get_stage()

#create a cone at path /World/MyCone
cone = UsdGeom.Cone.Define(stage, "/World/MyCone")

# Option 1 - CreateAttr (your way) - preferred for new prims
cone.CreateHeightAttr(2.0)
cone.CreateRadiusAttr(1.0)

# Option 2 - GetAttr then Set - preferred when attribute already exists
cone.GetHeightAttr().Set(2.0)
cone.GetRadiusAttr().Set(1.0)

