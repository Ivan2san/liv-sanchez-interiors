#!/usr/bin/env python3
# Terracotta - long section A-A, cut on the circulation spine looking west toward
# the espresso bar. Carries the dawn-to-dusk light story. Model units = metres.
# x = depth (0 = laneway front, 13.3 = rear BOH). y = height (0 floor up).
import cairosvg
S = 78.0
LEFT = 90.0
BASE = 470.0      # y-pixel of floor (FFL)
W = int(LEFT + 13.5*S + 230)
H = int(BASE + 150)

PAPER="#f4f1ea"; INK="#241f1a"; POCHE="#3a312a"; MUTED="#8a8178"
CLAY="#a9603e"; CLAYT="#a9603e33"; RENDER="#e7dcc7"; GROUND="#cfc4b0"
SKY="#eef0ee"; GLASS="#5b7d86"; SUN="#d8943f"; DUSK="#9c5a86"

def mx(x): return LEFT + x*S
def my(h): return BASE - h*S

def line(x0,h0,x1,h1,stroke=INK,sw=1.0,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{mx(x0):.1f}" y1="{my(h0):.1f}" x2="{mx(x1):.1f}" y2="{my(h1):.1f}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def txt(x,h,s,size=11,fill=INK,anchor="middle",weight="400",ff="DejaVu Sans",rot=None,ls="0"):
    tr=f' transform="rotate({rot} {mx(x):.1f} {my(h):.1f})"' if rot is not None else ''
    return f'<text x="{mx(x):.1f}" y="{my(h):.1f}" font-family="{ff}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" letter-spacing="{ls}"{tr}>{s}</text>'
def rect(x0,h0,x1,h1,fill="none",stroke="none",sw=1.0,rx=0):
    return f'<rect x="{mx(x0):.1f}" y="{my(h1):.1f}" width="{(x1-x0)*S:.1f}" height="{(h1-h0)*S:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" rx="{rx}"/>'

el=[f'<rect x="0" y="0" width="{W}" height="{H}" fill="{PAPER}"/>']

# ceiling profile (gentle barrel vault in lime render): front 3.6 -> apex 4.1 -> rear drop to 2.9
# control points along depth
def ceil_h(x):
    if x<=0.4: return 3.6
    if x<=6.0:
        t=(x-0.4)/(6.0-0.4); return 3.6+ (4.1-3.6)* (1-(2*t-1)**2)*0.9 + 0.0  # bulge
    if x<=11.0:
        t=(x-6.0)/(11.0-6.0); return 4.1-(4.1-3.3)*t
    return 2.9
pts=[(x/10.0, ceil_h(x/10.0)) for x in range(0,135)]
# interior fill (room volume) front 0 to rear wall 13.3, floor to ceiling
vol=f'<path fill="{SKY}" stroke="none" d="M {mx(0):.1f} {my(0):.1f} '
for x,h in pts: vol+=f'L {mx(x):.1f} {my(h):.1f} '
vol+=f'L {mx(13.3):.1f} {my(0):.1f} Z"/>'
el.append(vol)

# clerestory slot at apex (~ x 4.8-5.6) - cut a notch and show light
el.append(rect(4.8,4.05,5.6,4.35,fill="#ffffff",stroke=INK,sw=0.8))
el.append(txt(5.2,4.5,"clerestory slot",8,MUTED))

# ceiling line (lime render)
cl=f'<path fill="none" stroke="{INK}" stroke-width="1.6" d="M {mx(0):.1f} {my(3.6):.1f} '
for x,h in pts: cl+=f'L {mx(x):.1f} {my(h):.1f} '
cl+='"/>'
el.append(cl)
el.append(txt(2.6,3.95,"vaulted lime-render ceiling",9,MUTED,rot=-4))

# floor / ground
el.append(rect(-0.2,-0.45,13.5,0.0,fill=GROUND,stroke="none"))
el.append(line(-0.2,0,13.5,0,stroke=INK,sw=2.0))
el.append(txt(7.0,-0.28,"polished raw-clay / terracotta floor — FFL 0",9,"#52483f"))

# front shopfront glazing (depth 0), full height to 3.6
el.append(line(0,0,0,3.6,stroke=GLASS,sw=3))
el.append(line(0.08,0.0,0.08,3.5,stroke=GLASS,sw=1.0))
for gh in [1.0,2.0,3.0]:
    el.append(line(-0.05,gh,0.13,gh,stroke=GLASS,sw=1.0))
el.append(txt(0.05,3.85,"tall shopfront",8,GLASS,anchor="start"))
# rear wall + lower BOH ceiling
el.append(line(13.3,0,13.3,2.9,stroke=POCHE,sw=4))
el.append(line(11.0,0,11.0,2.7,stroke=CLAY,sw=2.4))  # low clay screen elevation
el.append(txt(11.0,2.95,"clay screen",8,CLAY))
el.append(rect(11.0,0,13.3,0.0,fill="none"))
el.append(txt(12.15,1.4,"BOH",9,MUTED))
el.append(txt(12.15,1.1,"services",8,MUTED))

# espresso bar elevation (beyond cut, along west wall) - clay counter + back joinery
el.append(rect(1.6,0,8.5,1.05,fill=CLAYT,stroke=CLAY,sw=1.6))
el.append(txt(5.0,0.5,"CLAY ESPRESSO BAR (elevation beyond)",9,CLAY,weight="600"))
# back wine wall shelving to 2.3
el.append(rect(1.6,1.05,8.5,2.3,fill="none",stroke=MUTED,sw=0.8))
for sh in [1.5,1.9]:
    el.append(line(1.6,sh,8.5,sh,stroke=MUTED,sw=0.6,dash="4 3"))
el.append(txt(5.0,2.05,"aged-brass + oiled-timber wine wall",8,MUTED))

# pendant lights (aged brass) over banquette zone (beyond), evening mood
for px in [6.4,8.2,9.8]:
    el.append(line(px,ceil_h(px),px,1.9,stroke="#7a6a52",sw=1.2))
    el.append(f'<circle cx="{mx(px):.1f}" cy="{my(1.78):.1f}" r="7" fill="#b5863f" stroke="{INK}" stroke-width="0.8"/>')
el.append(txt(8.2,1.45,"low aged-brass pendants",8,MUTED))

# ---- LIGHT STORY arrows ----
# Dawn: low east light raking in through shopfront
for i in range(4):
    y0=3.2-i*0.18
    el.append(line(-0.0,y0+0.0,3.4+i*0.2,0.25,stroke=SUN,sw=1.6))
el.append(f'<circle cx="{mx(-0.0):.1f}" cy="{my(3.3):.1f}" r="9" fill="{SUN}"/>')
el.append(txt(2.0,3.25,"DAWN — low light rakes across the clay counter",8.5,SUN,anchor="start",weight="600",rot=-9))
# Midday: shaft through clerestory
el.append(f'<path d="M {mx(4.85):.1f} {my(4.3):.1f} L {mx(4.5):.1f} {my(0.05):.1f} L {mx(5.9):.1f} {my(0.05):.1f} L {mx(5.55):.1f} {my(4.3):.1f} Z" fill="{SUN}" opacity="0.16"/>')
el.append(txt(5.2,2.7,"MIDDAY",8.5,"#b07a2e",weight="600"))
el.append(txt(5.2,2.45,"shaft of",8,MUTED))
el.append(txt(5.2,2.22,"top light",8,MUTED))
# Dusk: glow from pendants, glazing dark
el.append(txt(9.6,3.05,"DUSK — pendants warm, glazing turns dark, room turns inward",8.5,DUSK,anchor="middle",weight="600"))
for px in [6.4,8.2,9.8]:
    el.append(f'<circle cx="{mx(px):.1f}" cy="{my(1.78):.1f}" r="16" fill="{SUN}" opacity="0.12"/>')

# ---- height dimensions ----
def dimv(x,h0,h1,label):
    out=[line(x,h0,x,h1,stroke=INK,sw=0.6)]
    for hh in (h0,h1):
        out.append(line(x-0.07,hh,x+0.07,hh,stroke=INK,sw=0.8))
    out.append(txt(x-0.16,(h0+h1)/2,label,8.5,INK,rot=90))
    return out
el+=dimv(0.0-0.0,0,3.6,"3600")
el+=dimv(3.7,0,ceil_h(3.7),"4050")
el+=dimv(13.05,0,2.9,"2900")
# move first dim slightly outside front
el=[e.replace(f'x="{mx(0):.1f}"','x="%.1f"'%(mx(0)-0)) for e in el]  # no-op guard

# depth scale bar
sbx, sby = mx(0.0), H-46
el.append(f'<text x="{sbx:.1f}" y="{sby-8:.1f}" font-family="DejaVu Sans" font-size="9" fill="{MUTED}">SCALE 1:50 (indicative) · metres</text>')
for i in range(6):
    fill = INK if i%2==0 else PAPER
    el.append(f'<rect x="{sbx+i*S:.1f}" y="{sby:.1f}" width="{S:.1f}" height="8" fill="{fill}" stroke="{INK}" stroke-width="0.8"/>')
for i in range(7):
    el.append(f'<text x="{sbx+i*S:.1f}" y="{sby+22:.1f}" font-family="DejaVu Sans" font-size="8" fill="{INK}" text-anchor="middle">{i}</text>')

# titles
el.append(f'<text x="{LEFT}" y="40" font-family="DejaVu Serif" font-size="22" fill="{INK}" font-weight="600">Terracotta — Long Section A-A</text>')
el.append(f'<text x="{LEFT}" y="60" font-family="DejaVu Sans" font-size="11" fill="{MUTED}">One room, two moods: how the light works from dawn to dusk · looking toward the espresso bar</text>')
# front/rear labels
el.append(txt(0.0,-0.62,"LANEWAY",9,INK,weight="600",anchor="start"))
el.append(txt(13.3,-0.62,"REAR / BOH",9,INK,weight="600",anchor="end"))

# title block
tbx, tby, tbw, tbh = W-300, H-86, 280, 70
el.append(f'<rect x="{tbx}" y="{tby}" width="{tbw}" height="{tbh}" fill="none" stroke="{INK}" stroke-width="1.1"/>')
el.append(f'<line x1="{tbx}" y1="{tby+26}" x2="{tbx+tbw}" y2="{tby+26}" stroke="{INK}" stroke-width="0.8"/>')
el.append(f'<text x="{tbx+12}" y="{tby+18}" font-family="DejaVu Serif" font-size="15" fill="{INK}" font-weight="600">TERRACOTTA</text>')
el.append(f'<text x="{tbx+tbw-12}" y="{tby+18}" font-family="DejaVu Sans" font-size="9" fill="{MUTED}" text-anchor="end">DWG A-02</text>')
el.append(f'<text x="{tbx+12}" y="{tby+44}" font-family="DejaVu Sans" font-size="11" fill="{INK}">Long Section · the dawn-to-dusk light story</text>')
el.append(f'<text x="{tbx+12}" y="{tby+60}" font-family="DejaVu Sans" font-size="8.5" fill="{MUTED}">VOC08 · Dip. Interior Design · Sydney Design School · 03/06/2026</text>')

svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'+''.join(el)+'</svg>'
open("/sessions/awesome-kind-faraday/mnt/outputs/section.svg","w").write(svg)
cairosvg.svg2png(url="/sessions/awesome-kind-faraday/mnt/outputs/section.svg",
                 write_to="/sessions/awesome-kind-faraday/mnt/outputs/section.png", scale=1.6)
print("section written", W, H)
