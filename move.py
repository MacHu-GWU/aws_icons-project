# -*- coding: utf-8 -*-

import shutil
from pathlib import Path

dir_icons = Path(__file__).absolute().parent.joinpath("icons")
dir_asset = Path("/Users/sanhehu/Downloads/Asset-Package_01312023.d59bb3e1bf7860fb55d4d737779e7c6fce1e35ae")
dir_service =[path for path in dir_asset.iterdir() if path.name.startswith("Architecture-Service")][0]
dir_category =[path for path in dir_asset.iterdir() if path.name.startswith("Category")][0]
dir_resource =[path for path in dir_asset.iterdir() if path.name.startswith("Resource")][0]


for dir, folder in [
    (dir_service, "Service"),
    (dir_category, "Category"),
]:
    for path_src in dir.glob("**/*64.png"):
        path_dst = dir_icons.joinpath(folder, path_src.relative_to(dir))
        path_dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(path_src, path_dst)


for path_src in dir_resource.glob("**/*.png"):
    path_dst = dir_icons.joinpath("Resource", path_src.relative_to(dir_resource))
    path_dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(path_src, path_dst)
