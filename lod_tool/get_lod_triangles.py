import unreal

asset_path = "/Game/Meshes"

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
            f"LOD number {lod_detail_dict.get('lod_number')} of mesh {static_mesh.get_name()} has {lod_detail_dict.get('triangle_count')} triangles.\n"
        )

    return lod_details

assets = unreal.EditorUtilityLibrary.get_selected_assets()

if __name__ == "__main__":
    for asset in assets:
        get_lod_triangles(asset)