from vpython import *
#m ve n parametreleri belirlenir
m=2
n=5
r=3
#aynalar arasındaki mesafe hesaplanır
l=(10*((r*(1-cos((m*pi)/n)))/2))
#aynaların 3D görünümü temsil etmek için iki adet yatay silindir çizilir.
ayna1=cylinder(pos =vector(l-0.25,0,0),size=vector(0.25,3,3),axis=vector(1,0,0) )
ayna2=cylinder(pos =vector(-l,0,0),size=vector(0.25,3,3),axis=vector(1,0,0) )

side=l
thk=0.3
#gelecek olan ışının koordinatları belirlenir
x=-4
y=0
z=0
#ışını temsil etmesi için bir küre tasarlanır.
ball = sphere (pos =vector(x,y,z),color = color.green, radius = 0.1, make_trail=True)
attach_light(ball)
#ışının geliş yönüne göre ilk çarpacağı ayna hesaplanması için parametreler
if (x<0):
    c=0
    d=1
if (x > 0):
    c=1
    d=0
dt = 0.3
y=0.0015
i=0
side = side - thk*0.5 - ball.radius

print(side)
noktalar=[]
#ışının çarpacağı noktalar denklemler yardımı ile hesaplanır.
while (i<=n):
    if(i%2==c):
        a1=sphere(pos=vector(side,(sin(i*(m*pi/n))),(cos(i*(m*pi/n)))), color=color.red, radius=0.05, make_trail=True, retain=200)
        noktalar.append(a1.pos)
    if(i%2==d):
        a=sphere(pos=vector(-side, (sin(i*(m*pi/n))),(cos(i*(m*pi/n)))), color=color.red, radius=0.05, make_trail=True,
               retain=200)
        noktalar.append(a.pos)
    i = i + 1

print(noktalar)
#ışının ilerlemesi için ışına bulunanan noktaların yörüngesinde vektör eklenir
ball.p = vector (-(ball.pos.x)+noktalar[0].x, -(ball.pos.y)+(noktalar[0].y), -(ball.pos.z)+noktalar[0].z)/1000
def simulasyon():
    carpma = 0
    while True:
        rate(200)
        ball.pos = ball.pos + ball.p
        #ilk çarpmada ışın dışarıdan geleceği için ilk aynanın içinden geçer
        if (carpma==0):
            if ((ball.pos.x >side and c==0)or(ball.pos.x < -side and c==1)):
                ball.p.x = (noktalar[carpma + 1].x - noktalar[carpma].x) / 2000
                ball.p.y = (noktalar[carpma + 1].y - noktalar[carpma].y) / 2000
                ball.p.z = (noktalar[carpma + 1].z - noktalar[carpma].z) / 2000
                sphere(pos=ball.pos, color=color.red, radius=0.05, make_trail=True, retain=200)
                carpma = carpma + 1
        #sonraki çarpmalarda iki ayna arasında yansımalar gerçekleşir.
        if (carpma > 0):
            if not (side+0.05 > ball.pos.x > -side-0.05):

                ball.p.x = (noktalar[carpma + 1].x - noktalar[carpma].x) / 2000
                ball.p.y = (noktalar[carpma+1].y-noktalar[carpma].y)/2000
                ball.p.z=(noktalar[carpma+1].z-noktalar[carpma].z)/2000
                sphere(pos=ball.pos, color=color.red, radius=0.05, make_trail=True, retain=200)
                carpma=carpma+1
        #öçarpma sayısı "n" sayısı kadar olması durumunda simülasyon sonlanır.
        if carpma>=n+1:
            break


simulasyon()
