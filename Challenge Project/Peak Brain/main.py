import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

vertices1 = []
codes1 = []
vertices2 = []
codes2 = []
r = 10
z = ""

x = int(input("Input X = "))
y = int(input("Input Y = "))
if ((x>14 and x<26) and (y>4 and y<16)) :
    print("Your input ({},{}) = box with grey area and circle with grey area".format(x,y))
    z = "Your input ({},{}) = box with grey area and circle with grey area".format(x,y)
elif ((x>4 and x<26) and (y>4 and y<16)) :
    print("Your input ({},{}) = box with white area".format(x,y))
    z = "Your input ({},{}) = box with white area".format(x,y)
elif ((x>14 and x<36) and (y>4 and y<26)) :
    print("Your input ({},{}) = circle with white area".format(x,y))
    z = "Your input ({},{}) = circle with white area".format(x,y)
else :
    print("Your input ({},{}) = free area".format(x,y))
    z = "Your input ({},{}) = free area".format(x,y)

codes1 = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
vertices1 = [(5, 5), (5, 15), (25, 15), (25, 5), (0, 0)]
codes2 = [Path.MOVETO] + [Path.LINETO] + [Path.CURVE3]*2 + [Path.LINETO]
vertices2 = [(25, 15), (25, 5), (15, 5), (15, 15), (25, 15)]

path1 = Path(vertices1, codes1)
path2 = Path(vertices2, codes2)

pathpatch1 = PathPatch(path1, facecolor='none', edgecolor='black')
pathpatch2 = PathPatch(path2, facecolor='grey', edgecolor='black')

fig, ax = plt.subplots()
Drawing_colored_circle = plt.Circle((25, 15), r, fill = False, edgecolor='black')
ax.add_artist( Drawing_colored_circle )
ax.add_patch(pathpatch1)
ax.add_patch(pathpatch2)
ax.plot((25, 25), (15, 25), '--', lw=1, color='black', ms=1)
ax.plot(x, y, 'ro')
ax.text(26, 20, 'r = 10')
ax.text(5, 16, '5, 15')
ax.text(20, 16, '25, 15')
ax.text(x-3, y-2, 'Your Input', color='red')
ax.text(1, 1, z, color='red')

ax.autoscale_view()
ax.set_xlim(0, 50)
ax.set_ylim(0, 40)
plt.show()