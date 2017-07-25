"""Generate WrightTools logo."""


### import ########################################################################################


import os

import numpy as np

import h5py

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects

import WrightTools as wt
wt.artists.apply_rcparams('publication')


### define ########################################################################################


here = os.path.abspath(os.path.dirname(__file__))

cmap = wt.artists.colormaps['default']


### logo ##########################################################################################


# get arrays
p = os.path.join(here, 'peak.h5')
h5 = h5py.File(p)
xi = np.array(h5['xi'])
yi = np.array(h5['yi'])
zi = np.array(h5['zi'])

# process
zi = np.log10(zi)
print(np.nanmin(zi), np.nanmax(zi))
zi = zi - np.nanmin(zi)
zi = zi / np.nanmax(zi)
print(np.nanmin(zi), np.nanmax(zi))
#zi[zi < 0.2] = np.nan
print(np.nanmin(zi), np.nanmax(zi))

# create figure
fig, gs = wt.artists.create_figure(width=5)
ax = plt.subplot(gs[0, 0])

# pcolor
X, Y, Z = wt.artists.pcolor_helper(xi, yi, zi)
plot = ax.pcolor(X, Y, Z, cmap=cmap, alpha=0.95, vmin = 0.4, vmax = np.nanmax(zi))
plot.cmap.set_under('k', alpha = 1)

# contour
xi, yi, zi = wt.kit.zoom2D(xi, yi, zi)
levels = np.linspace(np.nanmin(zi), np.nanmax(zi), 11)
ax.contour(xi, yi, zi, levels=levels, colors='k', lw=5, alpha=0.25, vmin = np.nanmin(zi), vmax = np.nanmax(zi))

# decorate
ax.set_xlim(np.nanmin(xi), np.nanmax(xi))
ax.set_ylim(np.nanmin(yi), np.nanmax(yi))
wt.artists.set_ax_spines(ax=ax, lw=0)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.text(7000, 7000, r'$\mathbf{\omega\tau}$', ha='center', va='center',
        fontsize=165, path_effects=[PathEffects.withStroke(linewidth=5, foreground="w")])

# save
plt.savefig('logo.png', dpi=300, bbox_inches='tight', pad_inches=0, transparent = True)
plt.savefig('logo.pdf', bbox_inches='tight', pad_inches=0)
plt.close(fig)


### favicon ######################################################################################


# create figure
fig, gs = wt.artists.create_figure(width=5)
ax = plt.subplot(gs[0, 0])

# decorate
ax.set_xlim(np.nanmin(xi), np.nanmax(xi))
ax.set_ylim(np.nanmin(yi), np.nanmax(yi))
wt.artists.set_ax_spines(ax=ax, lw=7, c='none')
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.text(7000, 7000, r'$\mathbf{\omega\tau}$', ha='center', va='center',
        fontsize=165, path_effects=[PathEffects.withStroke(linewidth=25, foreground="w")])

# save
plt.savefig('favicon.png', dpi=19, bbox_inches='tight', pad_inches=0, transparent=True)
plt.close(fig)
