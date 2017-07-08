
# Inputs
#   folder, a filepath string. Possibly includes a filename that would need to be removed
#   filename, a string that would serve as the basename for the output files.
#   geometry_tree, a data tree of geometry. Each branch should become a separate plot
#   write_files, a boolean trigger that causes all the files to be written

# Outputs
#   output_file_names

import cPickle as pickle
import os
import shutil


def rhino_to_plottable(rhino_geom):
    """Takes rhino polylines or point arrays
    and outputs plottable geometries resempling linestrings
    """
    return [
        (rhino_geom.Point(i).X, rhino_geom.Point(i).Y)
        for i in range(rhino_geom.PointCount) 
    ]


def clean_folder_path(raw_folder_path):
    return os.path.dirname(raw_folder_path)


def overwrite_directory(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)


def export(tree, folder_path, filename):
    """
    Make a folder based on filename
    For branch in tree:
        make filename for individual plot run
        convert items to plottable geometries
        pickle plottable geometries to filename with filename in folder
    """
    new_folder_path = os.path.join(
        clean_folder_path(folder_path), filename)
    overwrite_directory(new_folder_path)
    output_files = []
    for i in range(tree.BranchCount):
        basename = filename + '-plot-' + str(i) + '.pkl'
        output_path = os.path.join(new_folder_path, basename)
        polylines = tree.Branch(i)
        geoms = [rhino_to_plottable(line) for line in polylines]
        output_files.append(output_path)
        with open(output_path, 'wb') as output_file:
            pickle.dump(geoms, output_file)
    return output_files


if write_files:
    output_file_names = export(geometry_tree, folder, filename)