def posi_search(lst_of_tps):
    lst = []
    for tp in lst_of_tps:
        if tp[0] >= 30 and tp[0] <= 40:
            print(tp)
            lst.append(tp)
    return lst


locations = [
    (35.68, 139.76),   # 东京 (Tokyo)
    (35.01, 135.76),   # 京都 (Kyoto)
    (43.06, 141.35),   # 札幌 (Sapporo)
    (26.21, 127.68),   # 那霸 (Naha)
    (34.05, -118.24),  # 洛杉矶 (Los Angeles)
    (51.50, -0.12),    # 伦敦 (London)
    (30.0, 140.0),     # 边界情况1
    (40.0, 135.0),     # 边界情况2
    (40.1, 140.0),     # 边界情况3
]
print(posi_search(locations))

def translate_point(point, dx, dy):
  """Translates a 2D point by dx and dy."""
  x, y = point
  new_x = x + dx
  new_y = y + dy
  return new_x, new_y

original_point = (1, 2)
translated_point = translate_point(original_point, 3, 4)
print(f"Original point: {original_point}")
print(f"Translated point: {translated_point}")