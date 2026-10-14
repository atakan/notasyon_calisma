x = x0 = 29.168032
y = y0 = 230.83658
dy = (y0-77.913063)/7
dx = (x0-182.06917)/7

for i in ("1", "2", "3", "4", "5", "6", "7", "8"):
    for j in ("a", "b", "c", "d", "e", "f", "g", "h"):
        print("""<text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:14.8167px;font-family:Trace;-inkscape-font-specification:Trace;text-align:center;writing-mode:lr-tb;direction:ltr;text-anchor:middle;fill:#241c1c;fill-opacity:1;stroke:#000000;stroke-width:0.154;stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1"
       x="%f"
       y="%f"
       id="text25"><tspan
         sodipodi:role="line"
         id="tspan25"
         style="stroke-width:0.154"
         x="%f"
         y="%f">%s%s</tspan></text>""" % (x, y, x, y, j, i))
        x -= dx
    x = x0
    y -= dy
