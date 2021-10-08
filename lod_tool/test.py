import unreal
import csv
import pathlib
from pathlib import Path

asset_path = "/Game/Meshes"

"""for material_index in range(0, static_mesh.get_num_sections(0)):
    material_name = static_mesh.get_material(material_index).get_name()"""

def get_mesh_name(static_mesh):
    mesh_name = static_mesh.get_name()
    print(f"Mesh name: {mesh_name}")
    return mesh_name

def check_lods(static_mesh):
    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(static_mesh)
    print(f"current LOD count: {lod_no}")
    return lod_no


"""def apply_lods(static_mesh):
    number_of_verts = unreal.EditorStaticMeshLibrary.get_number_verts(static_mesh, 0)
    if number_of_verts < 100:
        return
    print(f"Applying LODs to mesh {static_mesh.get_name()}")
    options = unreal.EditorScriptingMeshReductionOptions()
    options.reduction_settings = [
        unreal.EditorScriptingMeshReductionSettings(1.0, 1.0),
        unreal.EditorScriptingMeshReductionSettings(0.8, 0.75),
        unreal.EditorScriptingMeshReductionSettings(0.4, 0.2),
    ]

    options.auto_compute_lod_screen_size = False
    unreal.EditorStaticMeshLibrary.set_lods(static_mesh, options)
    unreal.EditorAssetLibrary.save_loaded_asset(static_mesh)

    print(f"New LOD count: {unreal.EditorStaticMeshLibrary.get_lod_count(static_mesh)}")"""


def get_material_count(static_mesh):
    sm_component = unreal.DatasmithMeshActorElement()
    material_count = sm_component.get_material_overrides_count()

    print(f"Current number of materials on this mesh: {material_count}")
    return material_count


if __name__ == "__main__":
    mesh_properties = []

    all_assets = unreal.EditorAssetLibrary.list_assets(asset_path)
    static_mesh = unreal.StaticMeshComponent.static_mesh

    all_assets_loaded = [unreal.EditorAssetLibrary.load_asset(a) for a in all_assets]

    static_mesh_assets = unreal.EditorFilterLibrary.by_class(
        all_assets_loaded, unreal.StaticMesh
    )

    list(map(check_lods, static_mesh_assets))
    """list(map(apply_lods, static_mesh_assets))"""

    for mesh in static_mesh_assets:
        mesh_info = {}
        mesh_name= get_mesh_name(mesh)
        lod_count = check_lods(mesh)
        material_count = get_material_count(mesh)
        mesh_info['mesh_name'] = mesh_name
        mesh_info["material_count"] = material_count
        mesh_info["lod_count"] = lod_count
        mesh_properties.append(mesh_info)

    keys = mesh_properties[0].keys()

    path = Path('H:/LODtool/Unreal/LOD_tryout/Content') 
    path.mkdir(parents=True, exist_ok=True)

    file_path = (path / 'meshProperties').with_suffix('.csv')

    with file_path.open(mode='w+') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(mesh_properties)
