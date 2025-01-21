from django.test import TestCase
from .models import (
    TypeAssets, SubtypeAssets, Departments, RiskType, Risk,
    Assets, AssetsDependence, AssetsValue, AssetsRisk,
    SafeguardsTypes, Safeguards, SafeguardsRisk
)
from Users.models import User, Workload

class ModelsTestCase(TestCase):
    def setUp(self):
        self.workload = Workload.objects.create(name="Workload 1")
        self.user = User.objects.create(username="testuser", password="password")
        
        self.type_asset = TypeAssets.objects.create(name="Hardware")
        self.subtype_asset = SubtypeAssets.objects.create(name="Laptop", type=self.type_asset)
        self.department = Departments.objects.create(name="IT", description="Technology Dept", workload=self.workload)
        self.risk_type = RiskType.objects.create(name="Cyber", description="Cyber security risk")
        self.risk = Risk.objects.create(type=self.risk_type, name="Hacking", dimention="High", description="Unauthorized access")
        
        self.asset = Assets.objects.create(
            code="A001", name="Laptop", ubicationType="Office", ubication="HQ",
            quantity=10, characteristic="Dell XPS", type=self.type_asset,
            responsableArea=self.department, responsableUser=self.user
        )
        
        self.asset_dependence = AssetsDependence.objects.create(
            percentaje=50, asset=self.asset, responsableUser=self.user, assetDepend=self.asset
        )
        
        self.asset_value = AssetsValue.objects.create(
            cuantityValue=1000, cualityValue="High", description="Laptop asset", dimentionValue="Physical", asset=self.asset
        )
        
        self.asset_risk = AssetsRisk.objects.create(
            risktype=self.risk_type, asset=self.asset, dimention="High"
        )
        self.asset_risk.risk.add(self.risk)
        
        self.safeguard_type = SafeguardsTypes.objects.create(name="Physical")
        self.safeguard = Safeguards.objects.create(type=self.safeguard_type, code="S001", name="CCTV")
        self.safeguard_risk = SafeguardsRisk.objects.create(risk=self.asset_risk)
        self.safeguard_risk.safeguard.add(self.safeguard)

    def test_type_assets_creation(self):
        self.assertEqual(self.type_asset.name, "Hardware")
    
    def test_subtype_assets_creation(self):
        self.assertEqual(self.subtype_asset.name, "Laptop")
        self.assertEqual(self.subtype_asset.type, self.type_asset)
    
    def test_department_creation(self):
        self.assertEqual(self.department.name, "IT")
    
    def test_asset_creation(self):
        self.assertEqual(self.asset.name, "Laptop")
        self.assertEqual(self.asset.quantity, 10)
    
    def test_assets_dependence(self):
        self.assertEqual(self.asset_dependence.percentaje, 50)

    def test_assets_value(self):
        self.assertEqual(self.asset_value.cualityValue, "High")
    
    def test_assets_risk(self):
        self.assertEqual(self.asset_risk.risktype.name, "Cyber")
        self.assertIn(self.risk, self.asset_risk.risk.all())

    def test_safeguards(self):
        self.assertEqual(self.safeguard.name, "CCTV")
        self.assertIn(self.safeguard, self.safeguard_risk.safeguard.all())
