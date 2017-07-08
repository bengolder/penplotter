
# Inputs
#   pickle_file, a filepath string to import
# Outputs
#   crvs, a set of polyline curves
import Rhino
import cPickle as pickle



def plottable_to_rhino(geom):
    """Takes rhino polylines or point arrays
    and outputs plottable geometries resempling linestrings
    """
    return Rhino.Geometry.PolylineCurve([
        Rhino.Geometry.Point3d(*coord)
        for pt in geom
    ])

with open(pickle_file, 'rb') as pickle_file:
    crvs = [
        plottable_to_rhino(geom)
        for geom in pickle.load(pickle_file)]
