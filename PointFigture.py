import matplotlib.pyplot as plt

BOX = 5
START = 365
changes = (8, -3, 4, -4, 12, -3, 7, -3, 5, -9, 3)

# one way to force dimensions is to set the figure size:
fig = plt.figure(figsize=(5, 10))

# another way is to control the axes dimensions
# for axes to have specific dimensions:
#                  [ x0,  y0,   w,   h]  in figure units, from 0 to 1
#ax = fig.add_axes([.15, .15, .7*.5, .7])
ax = fig.add_axes([.15, .15, .7, .7])

def sign(val):
    return val / abs(val)

pointChanges = []
for chg in changes:
    pointChanges += [sign(chg)] * abs(chg)

symbol = {-1:'o',1:'x'}

chgStart = START
for ichg, chg in enumerate(changes):
    x = [ichg+1] * abs(chg)
    y = [chgStart + i * BOX * sign(chg) for i in range(abs(chg))]
    chgStart += BOX * sign(chg) * (abs(chg)-2)
    ax.scatter(x, y,
               marker=symbol[sign(chg)],
               s=175)   #<----- control size of scatter symbol

ax.set_xlim(0, len(changes)+1)
# fig.savefig('pointandfigure.png')
fig.savefig('pointandfigure1.png')
plt.show()