from lod_tool.test import check_lods, apply_lods, get_material_count
import unreal

asset_path = "/Game/Meshes"

if __name__ == "__main__":
    all_assets = unreal.EditorAssetLibrary.list_assets(asset_path)
    static_mesh = unreal.StaticMeshComponent.static_mesh

    all_assets_loaded = [unreal.EditorAssetLibrary.load_asset(a) for a in all_assets]

    static_mesh_assets = unreal.EditorFilterLibrary.by_class(
        all_assets_loaded, unreal.StaticMesh
    )

    list(map(check_lods, static_mesh_assets))
    list(map(apply_lods, static_mesh_assets))

    for mesh in static_mesh_assets:
        get_material_count(mesh)
