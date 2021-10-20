import unreal

def get_bounds(obj):
    bounds = obj.get_bounds()
    radius = bounds.sphere_radius
    diameter = radius *2
    print(f"Bounding sphere diameter of mesh {obj.get_name()}: {diameter}")
    return diameter

if __name__ == "__main__":
    assets = unreal.EditorUtilityLibrary.get_selected_assets()
    for asset in assets:
        get_bounds(asset)