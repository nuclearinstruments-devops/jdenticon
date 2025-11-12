"""
Shape definitions for Jdenticon
"""


def center_shape(index, g, cell, position_index):
    """
    Renders center shapes.
    
    Args:
        index: Shape index
        g: Graphics object
        cell: Cell size
        position_index: Position index
    """
    index = index % 14
    
    if index == 0:
        k = cell * 0.42
        g.add_polygon([
            0, 0,
            cell, 0,
            cell, cell - k * 2,
            cell - k, cell,
            0, cell
        ])
    
    elif index == 1:
        w = int(cell * 0.5)
        h = int(cell * 0.8)
        g.add_triangle(cell - w, 0, w, h, 2)
    
    elif index == 2:
        w = int(cell / 3)
        g.add_rectangle(w, w, cell - w, cell - w)
    
    elif index == 3:
        inner = cell * 0.1
        # Use fixed outer border widths in small icons
        if cell < 6:
            outer = 1
        elif cell < 8:
            outer = 2
        else:
            outer = int(cell * 0.25)
        
        if inner > 1:
            inner = int(inner)  # large icon => truncate decimals
        elif inner > 0.5:
            inner = 1  # medium size icon => fixed width
        # else: small icon => anti-aliased border (keep float)
        
        g.add_rectangle(outer, outer, cell - inner - outer, cell - inner - outer)
    
    elif index == 4:
        m = int(cell * 0.15)
        w = int(cell * 0.5)
        g.add_circle(cell - w - m, cell - w - m, w)
    
    elif index == 5:
        inner = cell * 0.1
        outer = inner * 4
        
        # Align edge to nearest pixel in large icons
        if outer > 3:
            outer = int(outer)
        
        g.add_rectangle(0, 0, cell, cell)
        g.add_polygon([
            outer, outer,
            cell - inner, outer,
            outer + (cell - outer - inner) / 2, cell - inner
        ], True)
    
    elif index == 6:
        g.add_polygon([
            0, 0,
            cell, 0,
            cell, cell * 0.7,
            cell * 0.4, cell * 0.4,
            cell * 0.7, cell,
            0, cell
        ])
    
    elif index == 7:
        g.add_triangle(cell / 2, cell / 2, cell / 2, cell / 2, 3)
    
    elif index == 8:
        g.add_rectangle(0, 0, cell, cell / 2)
        g.add_rectangle(0, cell / 2, cell / 2, cell / 2)
        g.add_triangle(cell / 2, cell / 2, cell / 2, cell / 2, 1)
    
    elif index == 9:
        inner = cell * 0.14
        # Use fixed outer border widths in small icons
        if cell < 4:
            outer = 1
        elif cell < 6:
            outer = 2
        else:
            outer = int(cell * 0.35)
        
        if cell < 8:
            pass  # small icon => anti-aliased border (keep float)
        else:
            inner = int(inner)  # large icon => truncate decimals
        
        g.add_rectangle(0, 0, cell, cell)
        g.add_rectangle(outer, outer, cell - outer - inner, cell - outer - inner, True)
    
    elif index == 10:
        inner = cell * 0.12
        outer = inner * 3
        
        g.add_rectangle(0, 0, cell, cell)
        g.add_circle(outer, outer, cell - inner - outer, True)
    
    elif index == 11:
        g.add_triangle(cell / 2, cell / 2, cell / 2, cell / 2, 3)
    
    elif index == 12:
        m = cell * 0.25
        g.add_rectangle(0, 0, cell, cell)
        g.add_rhombus(m, m, cell - m, cell - m, True)
    
    else:  # index == 13
        if position_index == 0:
            m = cell * 0.4
            w = cell * 1.2
            g.add_circle(m, m, w)


def outer_shape(index, g, cell, position_index=0):
    """
    Renders outer shapes.
    
    Args:
        index: Shape index
        g: Graphics object
        cell: Cell size
        position_index: Position index (unused, for compatibility)
    """
    index = index % 4
    
    if index == 0:
        g.add_triangle(0, 0, cell, cell, 0)
    elif index == 1:
        g.add_triangle(0, cell / 2, cell, cell / 2, 0)
    elif index == 2:
        g.add_rhombus(0, 0, cell, cell)
    else:  # index == 3
        m = cell / 6
        g.add_circle(m, m, cell - 2 * m)
