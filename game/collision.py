#충돌처리 옮기기


def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.crush_box()
    left_b, bottom_b, right_b, top_b = b.crush_box()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True




def collide_floor(a,b):
    left_a, bottom_a, right_a, top_a = a.crush_box()
    left_b, bottom_b, right_b, top_b = b.crush_box()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    if (bottom_a < top_b) and (bottom_a > top_b - 10) and (top_a > top_b): return True



def collide_head(a,b):
    left_a, bottom_a, right_a, top_a = a.crush_box()
    left_b, bottom_b, right_b, top_b = b.crush_box()

    
    if left_a > right_b: return False
    elif right_a < left_b: return False
    elif top_a < bottom_b: return False
    elif bottom_a > top_b: return False

    if (bottom_a < top_b) and (top_a > top_b): return False

    elif top_a >= bottom_b: return True #머리 박기


def collide_side(a,b):
    left_a, bottom_a, right_a, top_a = a.crush_box()
    left_b, bottom_b, right_b, top_b = b.crush_box()

    
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False


    if (left_a < right_b) and (right_a > left_b) and (bottom_a < top_b): return True

    

def collide_monster(a,b):
    left_a, bottom_a, right_a, top_a = a.crush_box()
    left_b, bottom_b, right_b, top_b = b.crush_box()

    
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    #if bottom_a > top_b: return False


    return True

def collide_head_mon(a,b):
    left_a, bottom_a, right_a, top_a = a.crush_box()
    left_b, bottom_b, right_b, top_b = b.crush_box()

    
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False



    if (bottom_a < top_b) and (top_a > top_b): return True



   




