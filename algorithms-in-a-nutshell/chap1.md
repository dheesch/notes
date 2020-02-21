# Thinking in Algorithms
 
## Understand the Problem 
- understand the problem you want to solve 
- convex hull -  the smallest convex shape that fully encloses all points in a set of points 
  - a convex hull exists for any collection of three points or more 
-  here's some pseudocode for the naive solution 
```
slowHull (P)
  foreach p0 in P do
    foreach p1 in {P-p0} do
      foreach p2 in {P-p0-p1} do 1
        foreach p3 in {P-p0-p1-p2} do
          if p3 is contained within Triangle(p0,p1,p2) then
            mark p3 as internal 2

  create array A with all non-internal points in P
  determine leftmost point, left, in A
  sort A by angle formed with vertical line through left 3
  return A
```
- greedy solution 
  - remove from P its lowest point, low, 
  - sort remainint n - 1 points in descending order by the angle formed in relation to a vertical line through low 
    - these angles range from 
      - 90 degrees for points to the left of the line 
      - -90 degrees for points to the right of the line 
      - p[n-2] is the right most point 
      - p[0] is the left most point 
    - start with a partial convex hull formed from three point in this order {p[n-2], low, p[0]}
      - try to extend the hull by considering, in order, each of the point p[1] to p[n-2]
      - if the last three points of the partial hull ever turn left, the hull contains an incorrect point that must be removed 
    - once all points are considered, the partial hull completes 
- divide and conquer 
  - we can divide the problem in half if we first sort all points, p, left to right by x coordinate 
    - break ties by considering y coord
  - upper partial convex hull is computed considering points in order left to right prom p[0] to p[n-1]
  - lower partial convex hull is computed considering points in ourder right to left from p[n-1] to p[0]
- parallel
  - partition the initial points by x coordinate 
  - have each processor compute the convex hull for its subset of points 
  - stitch the hull together by merging neighboring parital solutions 
  - you still have to compute a hull on each processor, but it will be faster than other ways 
- generalization
  - voronoi diagram - geometric structure that divides a set of points in a plain into regions
    - each of which is anchored by one of the original points in the input set 
    - each region is the set of points in the plane closer to the anchor point p[i] than any other point in P
  - computing convex hull from a voronoi diagram 
    - compute the voronoi diagram for P
    - initialize the hull with the lowest point, low, in P
    - in clockwise fashion, visit the neighboring region that shares an infinitely long side 
    - add that region's anchor point to the hull
    - continue adding points until the original region is encountered
   