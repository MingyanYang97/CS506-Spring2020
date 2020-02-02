def draw_tree():
    height=5
    if(height<=0):
        print("Trees not found")
        return

    print("   /\ ")
    print("  /  \ ")
    print(" /    \ ")
    print("/______\ ")
    for i in range(height-1):
        print("  |  |")
    print("  |__|")
    return
