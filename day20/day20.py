'''
--- Day 20: Jurassic Jigsaw ---

The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance! 
Since you have some spare time, you might as well see if there was anything interesting in the image the Mythical Information Bureau satellite captured.

After decoding the satellite messages, you discover that the data actually contains many small images created by the satellite's camera array. 
The camera array consists of many cameras; rather than produce a single square image, they produce many smaller square image tiles that need to be reassembled back into a single image.

Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles (your puzzle input) arrived in a random order.

Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random orientation. 
Your first task is to reassemble the original image by orienting the tiles so they fit together.

To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly with its adjacent tiles. 
All tiles have this border, and the border lines up exactly when the tiles are both oriented correctly. 
Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other tiles.

Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?


--- Part 2 ---
Now, you're ready to check the image for sea monsters.

The borders of each tile are not part of the actual image; start by removing them.

Remove the gaps to form the actual image

                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
When looking for this pattern in the image, the spaces can be anything; only the # need to match. 
Also, you might need to rotate or flip your image before it's oriented correctly to find sea monsters. 
In the above image, after flipping and rotating it to the appropriate orientation.
Determine how rough the waters are in the sea monsters' habitat by counting the number of # that are not part of a sea monster. In the above example, the habitat's water roughness is 273.

How many # are not part of a sea monster?
'''
import re
from collections import defaultdict
import math
from copy import deepcopy
import numpy as np

N = 0; E = 1; S = 2; W = 3
tmap = dict()       # map from (N,E,S,W) edge numbers to tile IDs
tile_imgs = dict()  # map from (N,E,S,W) edge numbers to tiles

# Sea monster as binary array
sea_monsters = """00000000000000000010 
        10000110000110000111
        01001001001001001000"""
sea_monsters = np.array([list(l.strip()) for l in sea_monsters.split("\n")]).astype(np.int)

# Process input
with open("day20/input.txt") as input_file:
    t_tiles = [tile.split("\n") for tile in input_file.read().split("\n\n")]
    tile_len = len(t_tiles[0][1].strip())
    for t_tile in t_tiles:
        tileID = int(re.match(r"Tile (\d+):", t_tile[0]).group(1))
        og_tile = np.array([list(line) for line in t_tile[1:]])
        og_tile[og_tile == "#"] = 1
        og_tile[og_tile == "."] = 0
        og_tile = og_tile.astype(np.int)

        # Perform all transformations on card, adding to dictionaries
        for i in range(2 * 2):
            tile = og_tile.copy()
            # Horizontal flip
            if i & 1 == 0:
                tile = np.flipud(tile)
            # Vertical flip
            if i & 2 == 0:
                tile = np.fliplr(tile)
            # Rotations
            for j in range(4):
                edges = (
                    int("".join(tile[0].astype(str)), 2),
                    int("".join(tile[:,-1].astype(str)), 2),
                    int("".join(tile[-1].astype(str)), 2),
                    int("".join(tile[:,0].astype(str)), 2)
                )
                tile_imgs[edges] = tile
                tmap[edges] = tileID
                tile = np.rot90(tile, -1)
    
# Count number of tile transformations that have each edge
occurences = defaultdict(int)
for tileT, tileID in tmap.items():
    for edge in tileT:
        occurences[edge] += 1
# Find edge numbers on the boundary
bound_edges = set()
for edge, n in occurences.items():
    if n == 4: # Must be 4 different transformations of the same tile
        bound_edges.add(edge)

# Grid of tile transforms
grid_len = int(math.sqrt(len(t_tiles)))

# Find corners
corners = []
for tileT, tileID in tmap.items():
    edges = [edge for edge in tileT if edge in bound_edges]
    if len(edges) == 2:
        corners.append((tileT, tileID))
        if len(edges) >= 3: print(tileT, tileID)
print("Part 1:", math.prod(list(set([i for _, i in corners]))))

# Find the top-left corner candidates
tl_corners = []
for tileT, tileID in corners:
    if tileT[N] in bound_edges and tileT[W] in bound_edges:
        tl_corners.append((tileT, tileID))

# Place the rest of the tiles, starting with top-left corner, for each possible top-left corner
# This will generate all possible transformations of the image!
for tl_corner in tl_corners:
    grid = [[None for _ in range(grid_len)] for _ in range(grid_len)]
    grid[0][0] = tl_corner
    tmap_copy = deepcopy(tmap)
    # Remove top-left corner from map
    for tileT, tileID in list(tmap_copy.items()):
        if tileID == tl_corner[1]:
            tmap_copy.pop(tileT)
    # Place the tiles
    for row in range(grid_len):
        for col in range(grid_len):
            if grid[row][col] != None:
                continue
            match = None
            for tileT, tileID in tmap_copy.items():
                # Check if neighbor's edges match this tile's edges
                for d, p in enumerate([(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]):
                    # Check neighbor for matching edge num
                    if 0 <= p[0] < grid_len and 0 <= p[1] < grid_len:
                        neighbor = grid[p[0]][p[1]]
                        # Empty neighbor should not be boundary
                        if neighbor == None:
                            continue
                        # Check that opposite edge of neighbor tile matches edge of current tile
                        elif neighbor[0][(d + 2) % 4] != tileT[d]:
                            break
                    # Ensure that if tile is on edge, edge sides are in boundary edges set
                    elif tileT[d] not in bound_edges:
                        break
                else:
                    match = (tileT, tileID)
                    break
            # Remove all the transforms for the found tile from the map
            for tileT, tileID in list(tmap_copy.items()):
                if tileID == match[1]:
                    tmap_copy.pop(tileT)
            # Set grid
            grid[row][col] = match

    # Place the tiles
    img_len = grid_len * (tile_len - 2)
    img = np.ndarray((img_len, img_len), dtype=np.int)
    for row in range(grid_len):
        for col in range(grid_len):
            # Place the transformed tile into the image without the borders
            img[row * (tile_len - 2):(row + 1) * (tile_len - 2),
                col * (tile_len - 2):(col + 1) * (tile_len - 2)] =\
                tile_imgs[grid[row][col][0]][1:-1,1:-1]

    # Find sea monsters
    sm_count = 0
    for row in range(img_len - sea_monsters.shape[0]):
        for col in range(img_len - sea_monsters.shape[1]):
            if np.all(img[row:row+sea_monsters.shape[0], col:col+sea_monsters.shape[1]] & sea_monsters == sea_monsters):
                sm_count += 1
    if sm_count > 0:
        print("Part 2:", np.sum(img) - (sm_count * np.sum(sea_monsters)))
        break