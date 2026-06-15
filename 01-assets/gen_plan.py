#!/usr/bin/env python3
# Terracotta - to-scale floor plan, authored as vector SVG.
# Model units = metres. Street at bottom of page, rear/BOH at top. North = up.
import math
S = 70.0          # px per metre
LEFT = 130.0      # left margin (dim line + labels)
TOP = 96.0        # top margin (title)
YMAX = 13.5       # model y at top of drawing (rear shell face)

def mx(x): return LEFT + (x + 0.2) * S
def my(y): return TOP + (YMAX - y) * S

W = int(LEFT + (7.2 + 0.2) * S + 60)
H = int(TOP + (YMAX + 0.2) * S + 232)

PAPER="#f4f1ea"; INK="#241f1a"; POCHE="#3a312a"; MUTED="#8a8178"
CLAY="#a9603e"; CLAYT="#a9603e22"; ZONE="#9c6b4322"; GLASS="#5b7d86"
WCFILL="#6b86902a"; SERV="#7a726833"

def rect(x0,y0,x1,y1,fill="none",stroke=INK,sw=1.0,dash=None,rx=0):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<rect x="{mx(x0):.1f}" y="{my(y1):.1f}" width="{(x1-x0)*S:.1f}" '
            f'height="{(y1-y0)*S:.1f}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{sw}"{d} rx="{rx}"/>')

def line(x0,y0,x1,y1,stroke=INK,sw=1.0,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{mx(x0):.1f}" y1="{my(y0):.1f}" x2="{mx(x1):.1f}" '
            f'y2="{my(y1):.1f}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

def txt(x,y,s,size=12,fill=INK,anchor="middle",weight="400",ff="DejaVu Sans",
        rot=None,ls="0"):
    tr=f' transform="rotate({rot} {mx(x):.1f} {my(y):.1f})"' if rot is not None else ''
    return (f'<text x="{mx(x):.1f}" y="{my(y):.1f}" font-family="{ff}" '
            f'font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
            f'font-weight="{weight}" letter-spacing="{ls}"{tr}>{s}</text>')

def circ(x,y,r,fill="none",stroke=INK,sw=1.0):
    return f'<circle cx="{mx(x):.1f}" cy="{my(y):.1f}" r="{r*S:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

el=[]
el.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{PAPER}"/>')

# ---- wall poché ----
ox0,oy0,ox1,oy1=-0.2,-0.2,7.2,13.5
def P(x,y): return f'{mx(x):.1f} {my(y):.1f}'
poche=(f'<path fill="{POCHE}" fill-rule="evenodd" stroke="none" d="'
       f'M {P(ox0,oy0)} L {P(ox1,oy0)} L {P(ox1,oy1)} L {P(ox0,oy1)} Z '
       f'M {P(0,0)} L {P(7,0)} L {P(7,11)} L {P(0,11)} Z '
       f'M {P(0,11.2)} L {P(7,11.2)} L {P(7,13.3)} L {P(0,13.3)} Z "/>')
el.append(poche)

# ---- shopfront glazing ----
el.append(rect(1.3,-0.2,7.0,0.0,fill=PAPER,stroke="none"))
el.append(line(1.3,-0.05,7.0,-0.05,stroke=GLASS,sw=2.2))
el.append(line(1.3,-0.15,7.0,-0.15,stroke=GLASS,sw=1.2))
for gx in [2.0,2.85,3.7,4.55,5.4,6.25]:
    el.append(line(gx,-0.2,gx,0.0,stroke=GLASS,sw=1.2))
el.append(txt(4.15,-0.45,"STEEL-FRAMED SHOPFRONT GLAZING TO LANEWAY",
              9,MUTED,anchor="middle",ls="0.5"))

# ---- entry door ----
el.append(rect(0.4,-0.2,1.3,0.0,fill=PAPER,stroke="none"))
el.append(line(0.4,0,0.4,1.0,stroke=INK,sw=1.4))
el.append(f'<path d="M {mx(0.4)} {my(1.0):.1f} A {0.9*S:.1f} {0.9*S:.1f} 0 0 1 {mx(1.3):.1f} {my(0.0):.1f}" fill="none" stroke="{MUTED}" stroke-width="0.8" stroke-dasharray="3 3"/>')
el.append(txt(0.85,0.18,"ENTRY",9,MUTED))

# espresso back joinery
el.append(rect(0.0,2.0,0.6,8.5,fill=ZONE,stroke=INK,sw=1.0))
el.append(txt(0.3,5.25,"BACK BENCH / WINE WALL",8,MUTED,rot=90))
el.append(txt(1.0,5.25,"staff",8,MUTED,rot=90))
# clay bar counter (HERO)
el.append(rect(1.4,1.6,2.1,8.5,fill=CLAYT,stroke=CLAY,sw=1.8))
el.append(txt(1.75,5.0,"CLAY ESPRESSO BAR  ·  HERO",9,CLAY,rot=90,weight="600"))
for sy in [2.2,3.0,3.8]:
    el.append(circ(2.45,sy,0.18,fill=PAPER,stroke=INK,sw=0.9))
el.append(txt(2.66,2.0,"perch stools",8,MUTED,anchor="start",rot=90))
# circulation spine
el.append(line(2.85,0.2,2.85,10.6,stroke=MUTED,sw=0.6,dash="2 5"))
el.append(txt(3.15,9.6,"circulation",8,MUTED,rot=90))
# standing nooks
el.append(rect(3.6,0.0,7.0,3.4,fill="none",stroke=MUTED,sw=0.7,dash="4 4"))
el.append(txt(5.3,3.08,"STANDING NOOKS",9,INK,weight="600"))
el.append(txt(5.3,2.8,"lean rail + window perch",8,MUTED))
el.append(rect(3.7,0.0,6.9,0.35,fill=ZONE,stroke=INK,sw=0.9))
for px in [4.5,6.0]:
    el.append(circ(px,1.7,0.32,fill=PAPER,stroke=INK,sw=0.9))
    for a in range(0,360,90):
        ax=px+0.5*math.cos(math.radians(a)); ay=1.7+0.5*math.sin(math.radians(a))
        el.append(circ(ax,ay,0.13,fill=PAPER,stroke=MUTED,sw=0.7))
# banquette
el.append(rect(6.4,4.5,7.0,9.2,fill=CLAYT,stroke=CLAY,sw=1.6))
el.append(txt(6.7,6.85,"CLAY BANQUETTE",8,CLAY,rot=90,weight="600"))
for ty in [5.2,6.6,8.0]:
    el.append(rect(5.55,ty-0.35,6.25,ty+0.35,fill=PAPER,stroke=INK,sw=0.9))
    el.append(circ(5.15,ty,0.2,fill=PAPER,stroke=MUTED,sw=0.7))
el.append(txt(4.9,9.0,"BANQUETTE SEATING",9,INK,weight="600"))
# rear screen
el.append(line(0,11.0,2.7,11.0,stroke=CLAY,sw=2.4))
el.append(line(3.9,11.0,7,11.0,stroke=CLAY,sw=2.4))
el.append(txt(5.0,10.75,"low clay screen",8,MUTED))
el.append(f'<path d="M {mx(2.7)} {my(11.0):.1f} A {1.0*S:.1f} {1.0*S:.1f} 0 0 0 {mx(2.7):.1f} {my(12.0):.1f}" fill="none" stroke="{MUTED}" stroke-width="0.8" stroke-dasharray="3 3"/>')
el.append(line(2.7,11.0,2.7,12.0,stroke=INK,sw=1.2))

# services band
el.append(txt(3.5,13.15,"BACK OF HOUSE  ·  SERVICES",9,MUTED,weight="600",ls="0.5"))
el.append(rect(0.0,11.2,2.0,13.3,fill=WCFILL,stroke=INK,sw=1.0))
el.append(circ(1.0,12.0,0.35,fill="none",stroke=MUTED,sw=0.8))
el.append(rect(1.55,11.35,1.95,11.75,fill="none",stroke=MUTED,sw=0.7))
el.append(txt(1.0,12.9,"ACCESSIBLE WC",8,INK,weight="600"))
el.append(txt(1.0,12.62,"1900 x 2300 clr",7,MUTED))
el.append(line(2.0,12.4,2.0,13.1,stroke=PAPER,sw=3))
el.append(line(2.0,12.4,2.0,13.1,stroke=INK,sw=1.2))
el.append(rect(2.0,11.2,4.6,13.3,fill=SERV,stroke=INK,sw=1.0))
el.append(txt(3.3,12.5,"DRY STORE",8,INK))
el.append(txt(3.3,12.25,"+ UNDERCOUNTER COOL",7,MUTED))
el.append(rect(4.6,11.2,7.0,13.3,fill=SERV,stroke=INK,sw=1.0))
el.append(txt(5.8,12.98,"SERVICES RISER",8,INK,weight="600"))
for i,lbl in enumerate(["Water in / out","Waste + grease trap","Power board","Mech. extraction"]):
    el.append(txt(4.75,12.58-i*0.28,"• "+lbl,7,"#52483f",anchor="start"))

# dimensions
def dim_v(x,y0,y1,label):
    out=[line(x,y0,x,y1,stroke=INK,sw=0.6)]
    for yy in (y0,y1):
        out.append(line(x-0.08,yy,x+0.08,yy,stroke=INK,sw=0.8))
    out.append(txt(x-0.18,(y0+y1)/2,label,9,INK,rot=90))
    return out
def dim_h(y,x0,x1,label):
    out=[line(x0,y,x1,y,stroke=INK,sw=0.6)]
    for xx in (x0,x1):
        out.append(line(xx,y-0.08,xx,y+0.08,stroke=INK,sw=0.8))
    out.append(txt((x0+x1)/2,y+0.12,label,9,INK))
    return out
el+=dim_h(13.78,0,7,"7000")
el+=dim_v(-0.55,0,11.0,"MAIN ROOM 11000")
el+=dim_v(-0.55,11.2,13.3,"SERVICES 2100")
el.append(txt(3.5,-0.78,"LANEWAY FRONTAGE",10,INK,weight="600",ls="1"))

# north arrow
el.append(f'<g transform="translate({mx(6.75):.1f} {my(0.7):.1f})">'
          f'<path d="M0,-22 L7,10 L0,4 L-7,10 Z" fill="{INK}"/>'
          f'<text x="0" y="-28" font-family="DejaVu Sans" font-size="11" '
          f'fill="{INK}" text-anchor="middle" font-weight="600">N</text></g>')

# scale bar
sbx, sby = mx(0.0), H-92
el.append(f'<text x="{sbx:.1f}" y="{sby-8:.1f}" font-family="DejaVu Sans" font-size="9" fill="{MUTED}">SCALE 1:50 (indicative) · metres</text>')
for i in range(5):
    fill = INK if i%2==0 else PAPER
    el.append(f'<rect x="{sbx+i*S:.1f}" y="{sby:.1f}" width="{S:.1f}" height="8" fill="{fill}" stroke="{INK}" stroke-width="0.8"/>')
for i in range(6):
    el.append(f'<text x="{sbx+i*S:.1f}" y="{sby+22:.1f}" font-family="DejaVu Sans" font-size="8" fill="{INK}" text-anchor="middle">{i}</text>')

# title block
tbx, tby, tbw, tbh = W-300, H-86, 280, 70
el.append(f'<rect x="{tbx}" y="{tby}" width="{tbw}" height="{tbh}" fill="none" stroke="{INK}" stroke-width="1.1"/>')
el.append(f'<line x1="{tbx}" y1="{tby+26}" x2="{tbx+tbw}" y2="{tby+26}" stroke="{INK}" stroke-width="0.8"/>')
el.append(f'<text x="{tbx+12}" y="{tby+18}" font-family="DejaVu Serif" font-size="15" fill="{INK}" font-weight="600">TERRACOTTA</text>')
el.append(f'<text x="{tbx+tbw-12}" y="{tby+18}" font-family="DejaVu Sans" font-size="9" fill="{MUTED}" text-anchor="end">DWG A-01</text>')
el.append(f'<text x="{tbx+12}" y="{tby+44}" font-family="DejaVu Sans" font-size="11" fill="{INK}">Floor Plan · clay-and-earth espresso + wine bar</text>')
el.append(f'<text x="{tbx+12}" y="{tby+60}" font-family="DejaVu Sans" font-size="8.5" fill="{MUTED}">VOC08 · Dip. Interior Design · Sydney Design School · 03/06/2026</text>')

el.append(f'<text x="{LEFT}" y="40" font-family="DejaVu Serif" font-size="22" fill="{INK}" font-weight="600">Terracotta — Floor Plan</text>')
el.append(f'<text x="{LEFT}" y="60" font-family="DejaVu Sans" font-size="11" fill="{MUTED}">A single warm volume, dawn to dusk · coffee by day, wine by night</text>')

svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'+''.join(el)+'</svg>'
open("/sessions/awesome-kind-faraday/mnt/outputs/plan.svg","w").write(svg)
import cairosvg
cairosvg.svg2png(url="/sessions/awesome-kind-faraday/mnt/outputs/plan.svg",
                 write_to="/sessions/awesome-kind-faraday/mnt/outputs/plan.png", scale=1.6)
print("plan written", W, H)
