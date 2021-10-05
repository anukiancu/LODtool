import unreal

asset_path = "/Game/Meshes"
static_mesh = unreal.StaticMeshComponent.static_mesh


for material_index in range(0, static_mesh.get_num_sections(0)):
    material_name = static_mesh.get_material(material_index).get_name()


def check_lods(static_mesh):
    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(static_mesh)
    print(static_mesh.get_name())
    print(f"current LOD count: {lod_no}")


def get_material_count(static_mesh):
    material_count= unreal.DatasmithMeshActorElement.get_material_overrides_count()
    print(f'Current number of materials on this mesh: {material_count}')
    return


"""def get_poly_count():
    poly_count = unreal.EditableMesh.get_polygon_count()
    print(f"Mesh poly count: {poly_count}")"""


all_assets = unreal.EditorAssetLibrary.list_assets(asset_path)

all_assets_loaded = [unreal.EditorAssetLibrary.load_asset(a) for a in all_assets]

static_mesh_assets = unreal.EditorFilterLibrary.by_class(
    all_assets_loaded, unreal.StaticMesh
)

list(map(check_lods, static_mesh_assets))
