def make_path(parts):
    if len(parts) == 0:
        return ""
    path = parts[0]
    for i in range (1, len(parts)):
        path = f"{path}/{parts[i]}"
    return path
