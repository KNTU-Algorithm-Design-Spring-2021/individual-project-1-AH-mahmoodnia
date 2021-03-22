from math import sqrt
import closest_pair_2D


def distance(p1, p2):
    return sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)+((p1[2]-p2[2])**2))


def brute_force(p, n):
    min_value = float('inf')
    for i in range(n - 1):
        for j in range(i + 1, n):
            if distance(p[i], p[j]) < min_value:
                min_value = distance(p[i], p[j])
    return min_value


def closest_pair_2d(x_list, y_list, n):
    if n <= 3:
        return brute_force(x_list, n)
    mid = n//2
    left = closest_pair_2d(x_list[:mid], y_list, mid)
    right = closest_pair_2d(x_list[mid:], y_list, n-mid)
    landa = min(left, right)
    strip = []
    for i in range(n):
        if abs(y_list[i][0]-y_list[mid][0]) < landa:
            strip.append(y_list[i])
    strip_size = len(strip)
    min_value = landa
    for i in range(strip_size):
        j = i+1
        while j < strip_size and abs(strip[j][1]-strip[i][1]) < landa:
            min_value = distance(strip[i], strip[j])
            j += 1
    return min(landa, min_value)


def closest_pair(x_list, y_list, z_list, n):
    if n <= 3:
        return brute_force(x_list, n)
    mid = n//2
    left = closest_pair(x_list[:mid], y_list, z_list, mid)
    right = closest_pair(x_list[mid:], y_list, z_list, n-mid)
    landa = min(left, right)
    strip = []
    for k in range(n):
        if abs(x_list[k][0] - x_list[mid][0]) < landa:
            strip.append(x_list[k])
    strip_size = len(strip)
    min_value = landa
    for k in range(strip_size):
        m = k + 1
        while m < strip_size and closest_pair_2d(y_list, z_list, n) < landa:
            min_value = distance(strip[k], strip[m])
            m += 1
    return min(min_value, landa)


if __name__ == "__main__":
    points = [(92.34, 12.64, 23.242), (17.62, 16.2, 42.34),
              (64, 13, 98.32), (19.33, 112.43, 12.32), (37, 45, 76.131), (26, 140, 42)]
    x_coordinates = sorted(points, key=lambda x: x[0])
    y_coordinates = sorted(points, key=lambda x: x[1])
    z_coordinates = sorted(points, key=lambda x: x[2])
    print(closest_pair(x_coordinates, y_coordinates, z_coordinates, len(points)))
    print(brute_force(points, len(points)))
