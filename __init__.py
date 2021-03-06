# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
from bpy.app.handlers import persistent
import os

@persistent
def load_handler(dummy):
    import os
    from bpy import context
    screen = context.screen
    for area in screen.areas:
        if area.type == 'FILE_BROWSER':
            space = area.spaces.active
            params = space.params
            params.use_filter_folder = True

    user_prefs = context.preferences
    user_prefs.edit.undo_steps = 100
    user_prefs.view.show_tooltips_python = True
    user_prefs.view.show_developer_ui = True

    path_to_script_dir = os.path.dirname(os.path.abspath(__file__))
    file_list = sorted(os.listdir(path_to_script_dir))

    script_list = []
    for item in file_list:
        if item.endswith(".zip"):
            script_list.append(item)
            print("Append: " + item)
    for file in script_list:
        path_to_file = os.path.join(path_to_script_dir, file)
        print("Installing: " + path_to_file)
        bpy.ops.preferences.addon_install(
            overwrite=True,
            target="DEFAULT",
            filepath=path_to_file,
            filter_folder=True,
            filter_python=False,
            filter_glob="*.py;*.zip",
        )
    enableTheseAddons = [ 
        "space_sequencer",    
        "Playback_controls_in_VSE_header",
        "VSE_Easy_Proxy",
        "push_to_talk",
        "VSE_Transform_Tools",
        "freesound",
        "import_edl",
        "ExportEDL",
        "Subsimport",
        "Bligify",
    ]

    for string in enableTheseAddons:
        name = enableTheseAddons
        bpy.ops.preferences.addon_enable(module=string)

def register():
    bpy.app.handlers.load_factory_startup_post.append(load_handler)


def unregister():
    bpy.app.handlers.load_factory_startup_post.remove(load_handler)
