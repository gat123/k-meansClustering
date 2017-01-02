
import nose.tools as nt  # contains testing tools like ok_, eq_, etc.

from kmeans import kmeans

import math

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_distancePointFromCentroid():

    num_points = 100
    dimensions = 10
    lower = 0
    upper = 30
    num_clusters = 50
    opt_cutoff = 0.00001

    points = [kmeans.makeRandomPoint(dimensions, lower, upper) for i in xrange(num_points)]

    clusterPointList, centroids = kmeans.main(points, dimensions, lower, upper, num_clusters, opt_cutoff)

    for clusterPoints, centroid in zip(clusterPointList, centroids):
        if len(clusterPoints) > 0:
            for clusterPoint in clusterPoints:
                for otherCentroid in centroids:
                    if not centroid.equals(otherCentroid):
                        assert(clusterPoint.getDistance(centroid) <= clusterPoint.getDistance(otherCentroid))

def test_internalClusterDistance():

    num_points = 10
    dimensions = 2
    lower = 0
    upper = 9
    num_clusters = 2
    opt_cutoff = 0.00001

    points =[]
    x = 0
    for i in xrange(0, num_points/2):
        points += [kmeans.Point([x, x])]
        x = x+0.5

    x = 7
    for i in xrange(0, num_points/2):
        points += [kmeans.Point([x, x])]
        x = x+0.5

    clusterPointList, centroids = kmeans.main(points, dimensions, lower, upper, num_clusters, opt_cutoff)

    print clusterPointList, centroids
    for clusterPoints, centroid in zip(clusterPointList, centroids):
        if len(clusterPoints) > 0:
            for clusterPoint in clusterPoints:
                assert(clusterPoint.getDistance(centroid) <= math.sqrt(2))
