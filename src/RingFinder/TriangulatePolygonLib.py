#                    GNU LESSER GENERAL PUBLIC LICENSE
#                        Version 3, 29 June 2007

#  Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
#  Everyone is permitted to copy and distribute verbatim copies
#  of this license document, but changing it is not allowed.


#   This version of the GNU Lesser General Public License incorporates
# the terms and conditions of version 3 of the GNU General Public
# License, supplemented by the additional permissions listed below.

#   0. Additional Definitions.

#   As used herein, "this License" refers to version 3 of the GNU Lesser
# General Public License, and the "GNU GPL" refers to version 3 of the GNU
# General Public License.

#   "The Library" refers to a covered work governed by this License,
# other than an Application or a Combined Work as defined below.

#   An "Application" is any work that makes use of an interface provided
# by the Library, but which is not otherwise based on the Library.
# Defining a subclass of a class defined by the Library is deemed a mode
# of using an interface provided by the Library.

#   A "Combined Work" is a work produced by combining or linking an
# Application with the Library.  The particular version of the Library
# with which the Combined Work was made is also called the "Linked
# Version".

#   The "Minimal Corresponding Source" for a Combined Work means the
# Corresponding Source for the Combined Work, excluding any source code
# for portions of the Combined Work that, considered in isolation, are
# based on the Application, and not on the Linked Version.

#   The "Corresponding Application Code" for a Combined Work means the
# object code and/or source code for the Application, including any data
# and utility programs needed for reproducing the Combined Work from the
# Application, but excluding the System Libraries of the Combined Work.

#   1. Exception to Section 3 of the GNU GPL.

#   You may convey a covered work under sections 3 and 4 of this License
# without being bound by section 3 of the GNU GPL.

#   2. Conveying Modified Versions.

#   If you modify a copy of the Library, and, in your modifications, a
# facility refers to a function or data to be supplied by an Application
# that uses the facility (other than as an argument passed when the
# facility is invoked), then you may convey a copy of the modified
# version:

#    a) under this License, provided that you make a good faith effort to
#    ensure that, in the event an Application does not supply the
#    function or data, the facility still operates, and performs
#    whatever part of its purpose remains meaningful, or

#    b) under the GNU GPL, with none of the additional permissions of
#    this License applicable to that copy.

#   3. Object Code Incorporating Material from Library Header Files.

#   The object code form of an Application may incorporate material from
# a header file that is part of the Library.  You may convey such object
# code under terms of your choice, provided that, if the incorporated
# material is not limited to numerical parameters, data structure
# layouts and accessors, or small macros, inline functions and templates
# (ten or fewer lines in length), you do both of the following:

#    a) Give prominent notice with each copy of the object code that the
#    Library is used in it and that the Library and its use are
#    covered by this License.

#    b) Accompany the object code with a copy of the GNU GPL and this license
#    document.

#   4. Combined Works.

#   You may convey a Combined Work under terms of your choice that,
# taken together, effectively do not restrict modification of the
# portions of the Library contained in the Combined Work and reverse
# engineering for debugging such modifications, if you also do each of
# the following:

#    a) Give prominent notice with each copy of the Combined Work that
#    the Library is used in it and that the Library and its use are
#    covered by this License.

#    b) Accompany the Combined Work with a copy of the GNU GPL and this license
#    document.

#    c) For a Combined Work that displays copyright notices during
#    execution, include the copyright notice for the Library among
#    these notices, as well as a reference directing the user to the
#    copies of the GNU GPL and this license document.

#    d) Do one of the following:

#        0) Convey the Minimal Corresponding Source under the terms of this
#        License, and the Corresponding Application Code in a form
#        suitable for, and under terms that permit, the user to
#        recombine or relink the Application with a modified version of
#        the Linked Version to produce a modified Combined Work, in the
#        manner specified by section 6 of the GNU GPL for conveying
#        Corresponding Source.

#        1) Use a suitable shared library mechanism for linking with the
#        Library.  A suitable mechanism is one that (a) uses at run time
#        a copy of the Library already present on the user's computer
#        system, and (b) will operate properly with a modified version
#        of the Library that is interface-compatible with the Linked
#        Version.

#    e) Provide Installation Information, but only if you would otherwise
#    be required to provide such information under section 6 of the
#    GNU GPL, and only to the extent that such information is
#    necessary to install and execute a modified version of the
#    Combined Work produced by recombining or relinking the
#    Application with a modified version of the Linked Version. (If
#    you use option 4d0, the Installation Information must accompany
#    the Minimal Corresponding Source and Corresponding Application
#    Code. If you use option 4d1, you must provide the Installation
#    Information in the manner specified by section 6 of the GNU GPL
#    for conveying Corresponding Source.)

#   5. Combined Libraries.

#   You may place library facilities that are a work based on the
# Library side by side in a single library together with other library
# facilities that are not Applications and are not covered by this
# License, and convey such a combined library under terms of your
# choice, if you do both of the following:

#    a) Accompany the combined library with a copy of the same work based
#    on the Library, uncombined with any other library facilities,
#    conveyed under the terms of this License.

#    b) Give prominent notice with the combined library that part of it
#    is a work based on the Library, and explaining where to find the
#    accompanying uncombined form of the same work.

#   6. Revised Versions of the GNU Lesser General Public License.

#   The Free Software Foundation may publish revised and/or new versions
# of the GNU Lesser General Public License from time to time. Such new
# versions will be similar in spirit to the present version, but may
# differ in detail to address new problems or concerns.

#   Each version is given a distinguishing version number. If the
# Library as you received it specifies that a certain numbered version
# of the GNU Lesser General Public License "or any later version"
# applies to it, you have the option of following the terms and
# conditions either of that published version or of any later version
# published by the Free Software Foundation. If the Library as you
# received it does not specify a version number of the GNU Lesser
# General Public License, you may choose any version of the GNU Lesser
# General Public License ever published by the Free Software Foundation.

#   If the Library as you received it specifies that a proxy can decide
# whether future versions of the GNU Lesser General Public License shall
# apply, that proxy's public statement of acceptance of any version is
# permanent authorization for you to choose that version for the
# Library.


# https://people.sc.fsu.edu/~jburkardt/py_src/polygon_triangulate/polygon_triangulate.py


def angle_degree(x1, y1, x2, y2, x3, y3):
    # *****************************************************************************80
    #
    ## angle_degree() returns the degree angle defined by three points.
    #
    #  Discussion:
    #
    #        P1
    #        /
    #       /
    #      /7
    #     /
    #    P2--------->P3
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real X1, Y1, X2, Y2, X3, Y3, the coordinates of the points
    #    P1, P2, P3.
    #
    #  Output:
    #
    #    real VALUE, the angle swept out by the rays, measured
    #    in degrees.  0 <= VALUE < 360.  If either ray has zero length,
    #    then VALUE is set to 0.
    #
    import numpy as np

    x = (x3 - x2) * (x1 - x2) + (y3 - y2) * (y1 - y2)

    y = (x3 - x2) * (y1 - y2) - (y3 - y2) * (x1 - x2)

    if x == 0.0 and y == 0.0:
        value = 0.0
        return value

    value = np.arctan2(y, x)

    if value < 0.0:
        value = value + 2.0 * np.pi

    value = 180.0 * value / np.pi

    return value


def between(xa, ya, xb, yb, xc, yc):
    # *****************************************************************************80
    #
    ## between() is TRUE if vertex C is between vertices A and B.
    #
    #  Discussion:
    #
    #    The points must be (numerically) collinear.
    #
    #    Given that condition, we take the greater of XA - XB and YA - YB
    #    as a "scale" and check where C's value lies.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 October 2015
    #
    #  Author:
    #
    #    Original C version by Joseph ORourke.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Input:
    #
    #    real XA, YA, XB, YB, XC, YC, the coordinates of
    #    the vertices.
    #
    #  Output:
    #
    #    bool VALUE, is TRUE if C is between A and B.
    #
    if not collinear(xa, ya, xb, yb, xc, yc):
        value = False
    elif abs(ya - yb) < abs(xa - xb):
        xmax = max(xa, xb)
        xmin = min(xa, xb)
        value = xmin <= xc and xc <= xmax
    else:
        ymax = max(ya, yb)
        ymin = min(ya, yb)
        value = ymin <= yc and yc <= ymax

    return value


def collinear(xa, ya, xb, yb, xc, yc):
    # *****************************************************************************80
    #
    ## collinear() returns a measure of collinearity for three points.
    #
    #  Discussion:
    #
    #    In order to deal with collinear points whose coordinates are not
    #    numerically exact, we compare the area of the largest square
    #    that can be created by the line segment between two of the points
    #    to (twice) the area of the triangle formed by the points.
    #
    #    If the points are collinear, their triangle has zero area.
    #    If the points are close to collinear, then the area of this triangle
    #    will be small relative to the square of the longest segment.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 September 2016
    #
    #  Author:
    #
    #    Original C version by Joseph ORourke.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Input:
    #
    #    real XA, YA, XB, YB, XC, YC, the coordinates of
    #    the vertices.
    #
    #  Output:
    #
    #    bool VALUE, is TRUE if the points are judged
    #    to be collinear.
    #
    r8_eps = 2.220446049250313e-016

    area = triangle_area(xa, ya, xb, yb, xc, yc)

    side_ab_sq = (xa - xb) ** 2 + (ya - yb) ** 2
    side_bc_sq = (xb - xc) ** 2 + (yb - yc) ** 2
    side_ca_sq = (xc - xa) ** 2 + (yc - ya) ** 2

    side_max_sq = max(side_ab_sq, max(side_bc_sq, side_ca_sq))

    if side_max_sq <= r8_eps:
        value = True
    elif 2.0 * abs(area) <= r8_eps * side_max_sq:
        value = True
    else:
        value = False

    return value


def diagonal(im1, ip1, n, prev_node, next_node, x, y):
    # *****************************************************************************80
    #
    ## diagonal(): VERTEX(IM1) to VERTEX(IP1) is a proper internal diagonal.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 October 2015
    #
    #  Author:
    #
    #    Original C version by Joseph ORourke.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Input:
    #
    #    integer IM1, IP1, the indices of two vertices.
    #
    #    integer N, the number of vertices.
    #
    #    integer PREV_NODE(N), the previous neighbor of each vertex.
    #
    #    integer NEXT_NODE(N), the next neighbor of each vertex.
    #
    #    real X(N), Y(N), the coordinates of each vertex.
    #
    #  Output:
    #
    #    bool VALUE, the value of the test.
    #
    value1 = in_cone(im1, ip1, n, prev_node, next_node, x, y)
    value2 = in_cone(ip1, im1, n, prev_node, next_node, x, y)
    value3 = diagonalie(im1, ip1, n, next_node, x, y)

    value = value1 and value2 and value3

    return value


def diagonalie(im1, ip1, n, next_node, x, y):
    # *****************************************************************************80
    #
    ## diagonalie() is true if VERTEX(IM1):VERTEX(IP1) is a proper diagonal.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 October 2015
    #
    #  Author:
    #
    #    Original C version by Joseph ORourke.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Input:
    #
    #    integer IM1, IP1, the indices of two vertices.
    #
    #    integer N, the number of vertices.
    #
    #    integer NEXT_NODE(N), the next neighbor of each vertex.
    #
    #    real X(N), Y(N), the coordinates of each vertex.
    #
    #  Output:
    #
    #    bool VALUE, the value of the test.
    #
    first = im1
    j = first
    jp1 = next_node[first]

    value = True
    #
    #  For each edge VERTEX(J):VERTEX(JP1) of the polygon:
    #
    while True:
        #
        #  Skip any edge that includes vertex IM1 or IP1.
        #
        if j == im1 or j == ip1 or jp1 == im1 or jp1 == ip1:
            pass
        else:
            value2 = intersect(
                x[im1], y[im1], x[ip1], y[ip1], x[j], y[j], x[jp1], y[jp1]
            )

            if value2:
                value = False
                break

        j = jp1
        jp1 = next_node[j]

        if j == first:
            break

    return value


def in_cone(im1, ip1, n, prev_node, next_node, x, y):
    # *****************************************************************************80
    #
    ## in_cone() is TRUE if the diagonal VERTEX(IM1):VERTEX(IP1) is strictly internal.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 October 2015
    #
    #  Author:
    #
    #    Original C version by Joseph ORourke.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Input:
    #
    #    integer IM1, IP1, the indices of two vertices.
    #
    #    integer N, the number of vertices.
    #
    #    integer PREV_NODE(N), the previous neighbor of each vertex.
    #
    #    integer NEXT_NODE(N), the next neighbor of each vertex.
    #
    #    real X(N), Y(N), the coordinates of each vertex.
    #
    #  Output:
    #
    #    bool VALUE, the value of the test.
    #
    im2 = prev_node[im1]
    i = next_node[im1]

    t1 = triangle_area(x[im1], y[im1], x[i], y[i], x[im2], y[im2])

    if 0.0 <= t1:
        t2 = triangle_area(x[im1], y[im1], x[ip1], y[ip1], x[im2], y[im2])
        t3 = triangle_area(x[ip1], y[ip1], x[im1], y[im1], x[i], y[i])
        value = (0.0 < t2) and (0.0 < t3)

    else:
        t4 = triangle_area(x[im1], y[im1], x[ip1], y[ip1], x[i], y[i])
        t5 = triangle_area(x[ip1], y[ip1], x[im1], y[im1], x[im2], y[im2])
        value = not ((0.0 <= t4) and (0.0 <= t5))

    return value


def intersect(xa, ya, xb, yb, xc, yc, xd, yd):
    # *****************************************************************************80
    #
    ## intersect() is true if lines VA:VB and VC:VD intersect.
    #
    #  Discussion:
    #
    #    Thanks to Gene Dial for correcting the call to intersect_prop(),
    #    08 September 2016.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 September 2016
    #
    #  Author:
    #
    #    Original C version by Joseph ORourke.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Input:
    #
    #    real XA, YA, XB, YB, XC, YC, XD, YD, the X and Y
    #    coordinates of the four vertices.
    #
    #  Output:
    #
    #    bool VALUE, the value of the test.
    #
    if intersect_prop(xa, ya, xb, yb, xc, yc, xd, yd):
        value = True
    elif between(xa, ya, xb, yb, xc, yc):
        value = True
    elif between(xa, ya, xb, yb, xd, yd):
        value = True
    elif between(xc, yc, xd, yd, xa, ya):
        value = True
    elif between(xc, yc, xd, yd, xb, yb):
        value = True
    else:
        value = False

    return value


def intersect_prop(xa, ya, xb, yb, xc, yc, xd, yd):
    # *****************************************************************************80
    #
    ## intersect_prop() is TRUE if lines VA:VB and VC:VD have a proper intersection.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 October 2015
    #
    #  Author:
    #
    #    Original C version by Joseph ORourke.
    #    FORTRAN90 version by John Burkardt.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Input:
    #
    #    real XA, YA, XB, YB, XC, YC, XD, YD, the X and Y
    #    coordinates of the four vertices.
    #
    #  Output:
    #
    #    bool VALUE, the result of the test.
    #
    if collinear(xa, ya, xb, yb, xc, yc):
        value = False
    elif collinear(xa, ya, xb, yb, xd, yd):
        value = False
    elif collinear(xc, yc, xd, yd, xa, ya):
        value = False
    elif collinear(xc, yc, xd, yd, xb, yb):
        value = False
    else:
        t1 = triangle_area(xa, ya, xb, yb, xc, yc)
        t2 = triangle_area(xa, ya, xb, yb, xd, yd)
        t3 = triangle_area(xc, yc, xd, yd, xa, ya)
        t4 = triangle_area(xc, yc, xd, yd, xb, yb)

        value1 = 0.0 < t1
        value2 = 0.0 < t2
        value3 = 0.0 < t3
        value4 = 0.0 < t4

        value = (l4_xor(value1, value2)) and (l4_xor(value3, value4))

    return value


def l4_xor(l1, l2):
    # *****************************************************************************80
    #
    ## l4_xor() returns the exclusive OR of two L4's.
    #
    #  Discussion:
    #
    #    An L4 is a logical value.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 October 2015
    #
    #  Author:
    #
    #   John Burkardt
    #
    #  Input:
    #
    #    bool L1, L2, two values whose exclusive OR
    #    is needed.
    #
    #  Output:
    #
    #    bool VALUE, the exclusive OR of L1 and L2.
    #
    value1 = l1 and (not l2)
    value2 = (not l1) and l2

    value = value1 or value2

    return value


def polygon_area(n, x, y):
    # *****************************************************************************80
    #
    ## polygon_area() returns the area of a polygon.
    #
    #  Discussion:
    #
    #    The vertices should be listed in counter-clockwise order so that
    #    the area will be positive.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 September 2016
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Input:
    #
    #    integer N, the number of vertices.
    #
    #    real X(N), Y(N), the vertex coordinates.
    #
    #  Output:
    #
    #    real AREA, the area of the polygon.
    #
    area = 0.0
    im1 = n - 1

    for i in range(0, n):
        area = area + x[im1] * y[i] - x[i] * y[im1]
        im1 = i

    area = 0.5 * area

    return area


def polygon_triangulate(n, x, y):
    # ******************************************************************************/
    #
    ## polygon_triangulate() determines a triangulation of a polygon.
    #
    #  Discussion:
    #
    #    There are N-3 triangles in the triangulation.
    #
    #    For the first N-2 triangles, the first edge listed is always an
    #    internal diagonal.
    #
    #    Thanks to Gene Dial for pointing out a mistake in the area calculation,
    #    10 September 2016.
    #
    #    Thanks to Gene Dial for suggesting that the next() array should be
    #    renamed next_node() to avoid the Python keyword next, 22 September 2016.
    #
    #    Gene Dial requested an angle tolerance of about 1 millionth radian or
    #    5.7E-05 degrees, 26 June 2018.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 June 2018
    #
    #  Author:
    #
    #    Original C version by Joseph ORourke.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Input:
    #
    #    integer N, the number of vertices.
    #
    #    real X[N], Y[N], the coordinates of each vertex.
    #
    #  Output:
    #
    #    integer TRIANGLES[N-2,3], the triangles.
    #
    import numpy as np

    angle_tol = 5.7e-05
    #
    #  We must have at least 3 vertices.
    #
    if n < 3:
        # print("")
        # print("polygon_triangulate - Fatal error!")
        # print("  N < 3")
        raise Exception("polygon_triangulate - Fatal error!")
    #
    #  Consecutive vertices cannot be equal.
    #
    node_m1 = n - 1
    for node in range(0, n):
        if x[node_m1] == x[node] and y[node_m1] == y[node]:
            # print("")
            # print("polygon_triangulate - Fatal error!")
            # print("  Two consecutive nodes are identical.")
            raise Exception("polygon_triangulate - Fatal error!")

        node_m1 = node
    #
    #  No node can be the vertex of an angle less than 1 degree
    #  in absolute value.
    #
    node1 = n - 1

    for node2 in range(0, n):
        node3 = (node2 + 1) % n

        angle = angle_degree(x[node1], y[node1], x[node2], y[node2], x[node3], y[node3])

        if abs(angle) <= angle_tol:
            # print("")
            # print("polygon_triangulate - Fatal error!")
            # print(
            #     "  Polygon has an angle %g smaller than %g degrees."
            #     % (angle, angle_tol)
            # )
            # print("  occurring at node %d" % (node2))
            raise Exception("polygon_triangulate - Fatal error!")

        node1 = node2
    #
    #  Area must be positive.
    #
    area = polygon_area(n, x, y)

    if area <= 0.0:
        # print("")
        # print("polygon_triangulate - Fatal error!")
        # print("  Polygon has zero or negative area.")
        raise Exception("polygon_triangulate - Fatal error!")

    triangles = np.zeros([n - 2, 3], dtype=np.int32)
    #
    #  PREV_NODE and NEXT_NODE point to the previous and next nodes.
    #
    prev_node = np.zeros(n, dtype=np.int32)
    next_node = np.zeros(n, dtype=np.int32)

    i = 0
    prev_node[i] = n - 1
    next_node[i] = i + 1

    for i in range(1, n - 1):
        prev_node[i] = i - 1
        next_node[i] = i + 1

    i = n - 1
    prev_node[i] = i - 1
    next_node[i] = 0
    #
    #  EAR indicates whether the node and its immediate neighbors form an ear
    #  that can be sliced off immediately.
    #
    ear = np.zeros(n, dtype=bool)
    for i in range(0, n):
        ear[i] = diagonal(prev_node[i], next_node[i], n, prev_node, next_node, x, y)

    triangle_num = 0

    i2 = 0

    while triangle_num < n - 3:
        #
        #  If I2 is an ear, gather information necessary to carry out
        #  the slicing operation and subsequent "healing".
        #
        if ear[i2]:
            i3 = next_node[i2]
            i4 = next_node[i3]
            i1 = prev_node[i2]
            i0 = prev_node[i1]
            #
            #  Make vertex I2 disappear.
            #
            next_node[i1] = i3
            prev_node[i3] = i1
            #
            #  Update the earity of I1 and I3, because I2 disappeared.
            #
            ear[i1] = diagonal(i0, i3, n, prev_node, next_node, x, y)
            ear[i3] = diagonal(i1, i4, n, prev_node, next_node, x, y)
            #
            #  Add the diagonal [I3, I1, I2] to the list.
            #
            triangles[triangle_num, 0] = i3
            triangles[triangle_num, 1] = i1
            triangles[triangle_num, 2] = i2
            triangle_num = triangle_num + 1
        #
        #  Try the next vertex.
        #
        i2 = next_node[i2]
    #
    #  The last triangle is formed from the three remaining vertices.
    #
    i3 = next_node[i2]
    i1 = prev_node[i2]

    triangles[triangle_num, 0] = i3
    triangles[triangle_num, 1] = i1
    triangles[triangle_num, 2] = i2
    triangle_num = triangle_num + 1

    return triangles


def triangle_area(xa, ya, xb, yb, xc, yc):
    # *****************************************************************************80
    #
    ## triangle_area() computes the signed area of a triangle.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real XA, YA, XB, YB, XC, YC, the coordinates of
    #    the vertices of the triangle, given in counterclockwise order.
    #
    #  Output:
    #
    #    real VALUE, the signed area of the triangle.
    #
    value = 0.5 * ((xb - xa) * (yc - ya) - (xc - xa) * (yb - ya))

    return value
