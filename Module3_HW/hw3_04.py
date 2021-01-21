from math import sqrt


room_area = int(input("Please enter the room area: "))
scene_radius = int(input("Please enter the radius of a scene: "))
distance_from_scene_to_wall = int(input("Please enter the distance from scene to wall: "))

side_of_room = round(sqrt(room_area), 2)
if (side_of_room / 2 > scene_radius) and distance_from_scene_to_wall < ((side_of_room / 2) - scene_radius):
    print("The scene can be placed in this hall.")
else:
    print("The scene cannot be placed in this hall.")
