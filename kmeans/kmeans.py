import math
import random
from Point import *

def main(points, dimensions, lower, upper, num_clusters, opt_cutoff):

    listClusterPoints, clusterCentroids = kmeans(points, num_clusters, opt_cutoff, lower, upper, dimensions)

    i = 1
    for listPoints in listClusterPoints:
        print " Cluster", i, ": ", listPoints
        i +=1
    return listClusterPoints, clusterCentroids

def minClusterDistance(p, clusters):

    clusterCount = len(clusters)

    smallest_distance = p.getDistance(clusters[0])
    clusterIndex = 0

    for i in range(clusterCount - 1):
        distance = p.getDistance(clusters[i+1])
        if distance < smallest_distance:
            smallest_distance = distance
            clusterIndex = i+1

    return clusterIndex

def calculateCentroid(points):
    numPoints = len(points)
    coords = [p.coords for p in points]
    unzipped = zip(*coords)
    centroid_coords = [math.fsum(dList)/numPoints for dList in unzipped]
    return Point(centroid_coords)

def kmeans(points, clusterCount, cutoff, lower, upper, dimensions):

    clusters = [makeRandomPoint(dimensions, lower, upper) for i in xrange(clusterCount)]
    loopCounter = 0

    while True:
        lists = [ [] for c in clusters]

        loopCounter += 1
        for p in points:
            clusterIndex = minClusterDistance(p, clusters)
            lists[clusterIndex].append(p)

        biggest_shift = 0.0

        for i in range(clusterCount):
            if(len(lists[i]) > 0):
                old_centroid = clusters[i]
                clusters[i] = calculateCentroid(lists[i])
                shift = old_centroid.getDistance(clusters[i])
                biggest_shift = max(biggest_shift, shift)

        if biggest_shift < cutoff:
            print "Converged after %s iterations" % loopCounter
            break

    return lists, clusters

def makeRandomPoint(n, lower, upper):
    p = Point([random.uniform(lower, upper) for i in range(n)])
    return p

if __name__ == "__main__":

    num_points = 100
    dimensions = 2
    lower = 0
    upper = 1000
    num_clusters = 10
    opt_cutoff = 0.0001

    points = [makeRandomPoint(dimensions, lower, upper) for i in xrange(num_points)]

    main(points, dimensions, lower, upper, num_clusters, opt_cutoff)