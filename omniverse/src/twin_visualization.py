from omni.isaac.kit import SimulationApp

from pxr import Usd, UsdGeom

# Initialize the Simulation App
simulation_app = SimulationApp({"headless": False})

class DigitalTwin:
    def __init__(self, model_path, prim_name):
        self.model_path = model_path
        self.prim_name = prim_name

    def load_model(self):
        # Open the USD file
        stage = Usd.Stage.Open(self.model_path)
        if not stage:
            raise FileNotFoundError(f"Could not open USD file: {self.model_path}")
        # Define the model in the scene
        UsdGeom.Xform.Define(stage, self.prim_name)
        print(f"Loaded model: {self.model_path} at {self.prim_name}")

# Load the Factory USD model
factory = DigitalTwin("templates/Factory.usd", "/World/Factory")
factory.load_model()

# Load the MarkingLines USD model
marking_lines = DigitalTwin("templates/MarkingLines.usd", "/World/MarkingLines")
marking_lines.load_model()

# Load the Warehouse USD model
warehouse = DigitalTwin("templates/Warehouse.usd", "/World/Warehouse")
warehouse.load_model()

# Update the simulation app
simulation_app.update()
