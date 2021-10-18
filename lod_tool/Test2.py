import unreal
import csv
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


def get_tri_count(obj):
    inst = obj.create_static_mesh_description()
    poly_group = inst.create_polygon_group()
    polygons = inst.get_polygon_group_polygons(poly_group)
    num_of_polygons = inst.get_num_polygon_group_polygons(poly_group)
    tri_list = []

    for poly in polygons:
        triangles = inst.get_num_polygon_triangles(poly)
        tri_list.append(triangles)

    total_tris = num_of_polygons * sum(tri_list)
    print(f"Number of tris for this mesh: {total_tris}")
    return total_tris


def get_lod_triangles(static_mesh):
    lod_details = []

    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(static_mesh)

    for lod in range(lod_no):
        triangle_count = 0
        num_sections = static_mesh.get_num_sections(lod)
        for section_number in range(num_sections):
            section_data = unreal.ProceduralMeshLibrary.get_section_from_static_mesh(
                static_mesh, lod, section_number
            )
            triangle_count += len(section_data[1])
        lod_detail_dict = {"lod_number": lod, "triangle_count": triangle_count / 3}
        lod_details.append(lod_detail_dict)

    for lod_detail_dict in lod_details:
        print(
            f"LOD number {lod_detail_dict.get('lod_number')} has {lod_detail_dict.get('triangle_count')} triangles.\n"
        )
    return lod_details


def get_lod_screen_size(obj):
    lod_screen_size = unreal.EditorStaticMeshLibrary.get_lod_screen_sizes(obj)
    print(f"LOD screen size: {lod_screen_size}")
    return lod_screen_size


def get_bounding_box(obj):
    bounding_box = obj.get_bounding_box()

    print(f"Bounding box: {bounding_box.max}")
    print(f"Bounding box: {bounding_box.min}")
    return bounding_box


selected_assets = get_selected_asset()


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
        bounding_box = get_bounding_box(assets)
        # poly_count = get_tris(assets)
        # lod_settings = get_lod_info(assets)
        # tri_count = get_tri_count(assets)
        # poly_count = get_polygon_count(assets)
        # poly_count = get_asset_triangle_count(mesh)
        fucking_hell = get_lod_triangles(assets)
        mesh_info["mesh_name"] = mesh_name
        # mesh_info["bounding_box"] = bounding_box
        mesh_info["material_count"] = material_count
        mesh_info["lod_count"] = lod_count
        mesh_info["simple_collisions"] = simple_collission_count
        mesh_info["LOD_screen_size"] = lod_screen_size
        mesh_info["LOD_triangles"] = fucking_hell
        mesh_info["box_min"] = bounding_box.min
        mesh_info["box_max"] = bounding_box.max
        # mesh_info["LOD_settings"] = lod_settings
        # mesh_info["tri_count"] = tri_count
        # mesh_info["polygon_count"] = poly_count
        # mesh_info["LOD_screen_size"] = lod_screen_size
        # mesh_info["polygon_count"] = poly_count
        mesh_properties.append(mesh_info)

    keys = mesh_properties[0].keys()

    path = Path("I:/WIPs/LOD_tool_project/LODtool/Content")
    path.mkdir(parents=True, exist_ok=True)

    file_path = (path / "meshProperties").with_suffix(".csv")

    with file_path.open(mode="w+") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(mesh_properties)
