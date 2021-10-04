import unreal

asset_path = "/Game/Meshes"


def check_lods(static_mesh):
    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(static_mesh)
    print(static_mesh.get_name())
    print(f"current LOD count: {lod_no}")


"""def get_poly_count():
    poly_count = unreal.EditableMesh.get_polygon_count()
    print(f"Mesh poly count: {poly_count}")"""


all_assets = unreal.EditorAssetLibrary.list_assets(asset_path)

all_assets_loaded = [unreal.EditorAssetLibrary.load_asset(a) for a in all_assets]

static_mesh_assets = unreal.EditorFilterLibrary.by_class(
    all_assets_loaded, unreal.StaticMesh
)

list(map(check_lods, static_mesh_assets))
