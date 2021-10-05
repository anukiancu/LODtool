import unreal

asset_path = "/Game/Meshes"
static_mesh = unreal.StaticMeshComponent.static_mesh


"""for material_index in range(0, static_mesh.get_num_sections(0)):
    material_name = static_mesh.get_material(material_index).get_name()"""


def check_lods(static_mesh):
    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(static_mesh)
    print(f"Mesh name: {static_mesh.get_name()}")
    print(f"current LOD count: {lod_no}")


def apply_lods(static_mesh):
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

    print(f"New LOD count: {unreal.EditorStaticMeshLibrary.get_lod_count(static_mesh)}")


def get_material_count(static_mesh):
    sm_component = unreal.DatasmithMeshActorElement()
    sm_component.get_mesh_element(static_mesh)
    material_count = unreal.DatasmithMeshActorElement.get_material_overrides_count(
        sm_component
    )
    return get_material_count
    """material_count = unreal.DatasmithMeshActorElement.get_material_overrides_count()
    return"""
    print(f"Current number of materials on this mesh: {material_count}")


"""def get_poly_count():
    poly_count = unreal.EditableMesh.get_polygon_count()
    print(f"Mesh poly count: {poly_count}")"""


all_assets = unreal.EditorAssetLibrary.list_assets(asset_path)

all_assets_loaded = [unreal.EditorAssetLibrary.load_asset(a) for a in all_assets]

static_mesh_assets = unreal.EditorFilterLibrary.by_class(
    all_assets_loaded, unreal.StaticMesh
)

list(map(check_lods, static_mesh_assets))
list(map(apply_lods, static_mesh_assets))
list(map(get_material_count, static_mesh_assets))
