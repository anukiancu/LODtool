import unreal
import csv
import pathlib
from pathlib import Path

asset_path = "/Game/Meshes"


def check_lods(static_mesh):
    # Checks number of LODs for each mesh
    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(static_mesh)
    print(f"Current LOD count for this mesh: {lod_no}")
    return lod_no


def get_mesh_name(static_mesh):
    # Gets the name of the static mesh
    mesh_name = static_mesh.get_name()
    print(f"Mesh name: {mesh_name}")
    return mesh_name


def get_selected_asset():
    all_assets = unreal.EditorAssetLibrary.list_assets(asset_path)
    all_assets_loaded = [unreal.EditorAssetLibrary.load_asset(a) for a in all_assets]
    static_mesh_assets = unreal.EditorFilterLibrary.by_class(
        all_assets_loaded, unreal.StaticMesh
    )
    return static_mesh_assets


def get_num_mesh_materials(obj):
    num_of_materials = unreal.EditorStaticMeshLibrary.get_number_materials(obj)
    print(f"Current number of materials for this mesh {num_of_materials}")
    return num_of_materials


def get_simple_collision_count(obj):
    collision_count = unreal.EditorStaticMeshLibrary.get_simple_collision_count(obj)
    print(f"Number of simple collisions present on this mesh: {collision_count}")
    return collision_count


"""def get_lod_info(obj):
    build_settings = unreal.EditorStaticMeshLibrary.get_lod_build_settings(obj, 1)
    print(f"LOD build settings: {build_settings}")
    return build_settings"""


"""def get_polygon_count(obj):
    editable_mesh = unreal.EditableMeshFactory.make_editable_mesh(obj, 0)
    poly_count = unreal.EditableMesh.get_polygon_count(editable_mesh)
    print(f"Polygon count for this mesh: {poly_count}")
    return poly_count"""


def get_tri_count(obj):
    inst = unreal.MeshDescriptionBase()
    poly_group = inst.create_polygon_group()
    polygons = inst.get_polygon_group_polygons(poly_group)
    num_of_polygons = inst.get_num_polygon_group_polygons(poly_group)
    tri_list = []

    for poly in polygons:
        triangles = unreal.MeshDescriptionBase.get_num_polygon_triangles(poly)
        tri_list.append(triangles)

    total_tris = num_of_polygons * sum(tri_list)
    print(f"Number of tris for this mesh: {total_tris}")
    return total_tris

def get_lod_screen_size(obj):
    lod_screen_size = unreal.EditorStaticMeshLibrary.get_lod_screen_sizes(obj)
    print(f"LOD screen size: {lod_screen_size}")
    return lod_screen_size

def get_tris(obj):
    mesh_factory = unreal.EditableMeshFactory()
    editable_mesh = unreal.EditableMesh()
    make_editable_mesh = mesh_factory.make_editable_mesh(obj, 0)
    # poly_group = instt.create_polygon_groups(polygon_group_attributes = [[]], original_polygon_group_id=[])
    poly_count = editable_mesh.get_polygon_count(make_editable_mesh)
    print(f"Polygon count: {poly_count}")
    return poly_count


selected_assets = get_selected_asset()

"""for asset in selected_assets:
    #asset_name = get_mesh_name(asset)
    num_of_mats = get_num_mesh_materials(asset)
    #lod_no = check_lods(asset)
    print(f"Current number of materials: {num_of_mats}")"""


if __name__ == "__main__":
    mesh_properties = []
    for assets in selected_assets:
        mesh_info = {}
        mesh_name = get_mesh_name(assets)
        # bounding_box = get_bounding_box(assets)
        # lod_screen_size = get_lod_screen_size(mesh)
        lod_count = check_lods(assets)
        material_count = get_num_mesh_materials(assets)
        simple_collission_count = get_simple_collision_count(assets)
        lod_screen_size = get_lod_screen_size(assets)
        #poly_count = get_tris(assets)
        # lod_settings = get_lod_info(assets)
        # tri_count = get_tri_count(assets)
        # poly_count = get_polygon_count(assets)
        # poly_count = get_asset_triangle_count(mesh)
        mesh_info["mesh_name"] = mesh_name
        # mesh_info["bounding_box"] = bounding_box
        mesh_info["material_count"] = material_count
        mesh_info["lod_count"] = lod_count
        mesh_info["simple_collisions"] = simple_collission_count
        mesh_info['LOD_screen_size'] = lod_screen_size
        # mesh_info["LOD_settings"] = lod_settings
        # mesh_info["tri_count"] = tri_count
        # mesh_info["polygon_count"] = poly_count
        # mesh_info["LOD_screen_size"] = lod_screen_size
        # mesh_info["polygon_count"] = poly_count
        mesh_properties.append(mesh_info)

    keys = mesh_properties[0].keys()

    path = Path("H:/LODtool/Unreal/LOD_tryout/Content")
    path.mkdir(parents=True, exist_ok=True)

    file_path = (path / "meshProperties").with_suffix(".csv")

    with file_path.open(mode="w+") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(mesh_properties)
