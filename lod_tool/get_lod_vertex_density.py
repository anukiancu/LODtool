import unreal

def get_vertex_density(obj):
    bounds = obj.get_bounds()
    radius = bounds.sphere_radius
    diameter = radius *2
    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(obj)
    for lod in range(lod_no):
        verts_no = unreal.EditorStaticMeshLibrary.get_number_verts(obj, lod)
        vertex_density = verts_no/diameter
        print(f"Vertex density for LOD {lod} : {vertex_density}")
    return vertex_density

if __name__ == "__main__":
    assets = unreal.EditorUtilityLibrary.get_selected_assets()
    for asset in assets:
        get_vertex_density(asset)