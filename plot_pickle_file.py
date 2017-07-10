program_description = """Preview and plot polylines from a pickle file.
"""
import sys
import cPickle as pickle
from pprint import pprint
from shapely.geometry import LineString
import argparse

from plotter import Drawing


def unpack_pickle_file_to_shapely(pickle_file):
    geoms = pickle.load(pickle_file)
    pickle_file.close()
    return [LineString(coords) for coords in geoms]


def run(infile, plot=False):
    drawing = Drawing()
    for line in unpack_pickle_file_to_shapely(infile):
        drawing.add(line)
    preview_path = drawing.preview()
    print("svg preview written to '{}'".format(preview_path))
    if plot:
        drawing.plot()
	



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=program_description)
    parser.add_argument(
        'filepath', type=argparse.FileType('rb'),
        help='path to a pickle-format input file')
    parser.add_argument(
        '-p', '--plot', action='store_true',
        help='send to the plotter (default is preview-only)')
    args = parser.parse_args()
    run(infile=args.filepath, plot=args.plot)

