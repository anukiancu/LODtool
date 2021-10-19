import unreal
import csv
from pathlib import Path

asset_path = "/Game/Meshes"


def check_lods(static_mesh):
    # Checks number of LODs for each mesh
    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(static_mesh)
    print(f"Current LOD count for this mesh: {lod_no}")
    return lod_no

def remove_lods(static_mesh):
    unreal.EditorStaticMeshLibrary.remove_lods(static_mesh)

def get_mesh_name(static_mesh):
    # Gets the name of the static mesh
    mesh_name = static_mesh.get_name()
    print(f"Mesh name: {mesh_name}")
    return mesh_name


def get_s_asset():
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

def get_verts(obj):
    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(obj)
    for lod in range(lod_no):
        verts_no = unreal.EditorStaticMeshLibrary.get_number_verts(obj, lod)
        print(f"Number of verts for LOD {lod}: {verts_no}")
    return verts_no

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
    unreal.EditorStaticMeshLibrary.set_allow_cpu_access(static_mesh, True)

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
    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(obj)
    lod_screen_sizes = []
    for lod in range(lod_no):
        lod_screen_size = unreal.EditorStaticMeshLibrary.get_lod_screen_sizes(obj)
        lod_screen_size_dict = {"lod_number": lod, "screen_size": lod_screen_size}
        lod_screen_sizes.append(lod_screen_size_dict)

    for lod_screen_size_dict in lod_screen_sizes:
        print(
            f"LOD number {lod_screen_size_dict.get('lod_number')} has a screen size of {lod_screen_size_dict.get('screen_size')}")
        
    return lod_screen_sizes

def get_bounds(obj):
    bounds = obj.get_bounds()
    radius = bounds.sphere_radius
    diameter = radius *2
    print(f"Bounding sphere diameter: {diameter}")
    return diameter

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


selected_assets = get_s_asset()
assets = unreal.EditorUtilityLibrary.get_selected_assets()



if __name__ == "__main__":
    mesh_properties = []
    for asset in assets:
        mesh_info = {}
        mesh_name = get_mesh_name(asset)
        lod_count = check_lods(asset)
        material_count = get_num_mesh_materials(asset)
        simple_collission_count = get_simple_collision_count(asset)
        lod_screen_size = get_lod_screen_size(asset)
        fucking_hell = get_lod_triangles(asset)
        vertex_density = get_vertex_density(asset)
        bounds = get_bounds(asset)
        mesh_info["mesh_name"] = mesh_name
        mesh_info["material_count"] = material_count
        mesh_info["lod_count"] = lod_count
        mesh_info["simple_collisions"] = simple_collission_count
        mesh_info["LOD_screen_size"] = lod_screen_size
        mesh_info["LOD_triangles"] = fucking_hell
        mesh_info["bounding_sphere_radius"] = bounds
        mesh_info["vertex_density"] = vertex_density
        mesh_properties.append(mesh_info)

    keys = mesh_properties[0].keys()

    path = Path("H:/LODtool/Unreal/LOD_tryout/Content")
    path.mkdir(parents=True, exist_ok=True)

    file_path = (path / "meshProperties").with_suffix(".csv")

    with file_path.open(mode="w+") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(mesh_properties)
