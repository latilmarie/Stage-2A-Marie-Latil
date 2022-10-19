# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:13:14 2022

@author: baumontm
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import nilearn
from nilearn.plotting import plot_glass_brain
import numpy as np
import scipy.stats as st

#%% COMMENTS

# fig = plt.figure(figsize=(10, 6)) for the size of the figure displayed (can be adapted in order to separate the title from the brain image)


#####   SIMPLE PLOTTING   #####
# plot_glass_brain(img,                      # image to display (.nii)
#                  title='...', 
#                  display_mode='...',       # ‘ortho’, ‘x’, ‘y’, ‘z’, ‘xz’, ‘yx’, ‘yz’, ‘l’, ‘r’, ‘lr’, ‘lzr’, ‘lyr’, ‘lzry’, ‘lyrz’
#                  colorbar=True,            # to display the colorbar on the right of the plot, if not wanted, put None instead
#                  cmap='...',               # the name of the colormap, given on https://nilearn.github.io/stable/plotting/index.html#available-colormaps
#                  vmax=...,                 # the max value of the colorbar, in order to have the same scale of color for each image (vmin can also be added)
#                  figure = fig)             # to put the display on the figure number 'fig', useful if you want to superpose several images on the same figure



#####   PLOT WITH CONTOURS   #####
# display = plot_glass_brain(None,                      
#                            display_mode='...',        # ‘ortho’, ‘x’, ‘y’, ‘z’, ‘xz’, ‘yx’, ‘yz’, ‘l’, ‘r’, ‘lr’, ‘lzr’, ‘lyr’, ‘lzry’, ‘lyrz’
#                            figure = fig)              # to put the display on the figure number 'fig', useful if you want to superpose several images on the same figure
#
# display.add_contours(img, 
#                      levels=[1.],                     # level of the zone detection (when level increases, the zone detected for contours is smaller)
#                      colors='...',                    # colour of the contour, given on https://i.stack.imgur.com/lFZum.png
#                      linewidths=3)
#
# To add legend
# ldg = Rectangle((1, 1), 1, 1, fc="...(colour)")
# plt.legend([lgd],
#            ["..."],                                   # the legend name
#            fontsize=17,                               # the size of the text
#            bbox_to_anchor=(-0.5,-0.1, 1, 1))          # the position of the legend on the figure



#####   HISTOGRAMS   #####
# plt.tick_params(right = False, labelbottom = False, bottom = False, left=False, labelleft=False)    # to delete number on axes on the right, the left and the bottom
#
# plt.bar(x,                        # coordonate of the bars
#         height = y,               # heights of the bars
#         width = 1,                # widths of the bars
#         color = '...',            # color of the bars
#         linewidth = 2, 
#         yerr = error,             # vertical error bar (xerr can also be added)
#         ecolor = '...',           # colour of the error bar
#         capsize = 5)              # length of the error bar caps 
#
# plt.annotate(str(mean),           # text string of characters - str(mean) convert the int mean into a string
#              xy=(2.3,mean+0.01),  # coordinates of the legend
#              fontsize=14)         # size of the text


#%% 

# all the images have been thresholded on spm before loaded here

# Norm
fig = plt.figure(figsize=(10, 6))
norm_thresh = nilearn.image.load_img('E:/Manip_IRM/spm_2ndLvlOutputs_trial_AROMA/demean_3PM_cumulativeError/norm/spm_thresholded.nii') # image loaded
plot_glass_brain(norm_thresh, title='norm',display_mode='yz',  colorbar=True, cmap='ocean_hot', vmax=21, figure=fig)
plt.savefig('E:/Manip_IRM/Nilearn/norm.png', dpi=300, bbox_inches='tight') # image saved

# Rdmrot
fig = plt.figure(figsize=(10, 6))
rdm_thresh = nilearn.image.load_img('E:/Manip_IRM/spm_2ndLvlOutputs_trial_AROMA/demean_3PM_cumulativeError/rdmrot/spm_thresholded.nii')
plot_glass_brain(rdm_thresh, title='rdm',display_mode='yz', colorbar=True, cmap='ocean_hot', vmax=21, figure=fig)
plt.savefig('E:/Manip_IRM/Nilearn/rdmrot.png', dpi=300, bbox_inches='tight')

# Adapt day1
fig = plt.figure(figsize=(10, 6))
adapt1_thresh = nilearn.image.load_img('E:/Manip_IRM/spm_2ndLvlOutputs_trial_AROMA/demean_3PM_cumulativeError/adapt-day1/spm_thresholded.nii')
plot_glass_brain(adapt1_thresh, title='adapt-day1',display_mode='yz', colorbar=True, cmap='ocean_hot', vmax=21, figure=fig)
plt.savefig('E:/Manip_IRM/Nilearn/adapt-day1.png', dpi=300, bbox_inches='tight')

# Adapt day2
fig = plt.figure(figsize=(10, 6))
adapt2_thresh = nilearn.image.load_img('E:/Manip_IRM/spm_2ndLvlOutputs_trial_AROMA/demean_3PM_cumulativeError/adapt-day2/spm_thresholded.nii')
plot_glass_brain(adapt2_thresh, title='adapt-day2',display_mode='yz', colorbar=True, cmap='ocean_hot', vmax=21, figure=fig)
plt.savefig('E:/Manip_IRM/Nilearn/adapt-day2.png', dpi=300, bbox_inches='tight')

# Adapt day1 EM+
fig = plt.figure(figsize=(10, 6))
adapt1_EM_thresh = nilearn.image.load_img('E:/Manip_IRM/spm_2ndLvlOutputs_trial_AROMA/demean_3PM_cumulativeError/adapt-day1_EM+/spm_thresholded.nii')
plot_glass_brain(adapt1_EM_thresh, title='adapt-day1_EM+',display_mode='yz', colorbar=True, cmap='ocean_hot', vmax=8.5, figure=fig)
plt.savefig('E:/Manip_IRM/Nilearn/adapt-day1_EM+.png', dpi=300, bbox_inches='tight')

# Adapt day2 EM+
fig = plt.figure(figsize=(10, 6))
adapt2_EM_thresh = nilearn.image.load_img('E:/Manip_IRM/spm_2ndLvlOutputs_trial_AROMA/demean_3PM_cumulativeError/adapt-day2_EM+/spm_thresholded.nii')
plot_glass_brain(adapt2_EM_thresh, title='adapt-day2_EM+',display_mode='yz', colorbar=True, cmap='ocean_hot', vmax=8.5, figure=fig)
plt.savefig('E:/Manip_IRM/Nilearn/adapt-day2_EM+.png', dpi=300, bbox_inches='tight')

# Adapt day2 larger than day1 EM+
fig = plt.figure(figsize=(10, 6))
adapt2_larger_adapt1_EM_thresh = nilearn.image.load_img('E:/Manip_IRM/spm_2ndLvlOutputs_trial_AROMA/demean_3PM_cumulativeError/adapt-day2_EM+_LargerThan_adapt-day1_EM+/spm_thresholded.nii')
plot_glass_brain(adapt2_larger_adapt1_EM_thresh, title='adapt-day2_EM+_LargerThan_adapt-day1_EM+',display_mode='yz', colorbar=True, cmap='ocean_hot', vmax=8.5, figure=fig)
plt.savefig('E:/Manip_IRM/Nilearn/adapt-day2_EM+_LargerThan_adapt-day1_EM+.png', dpi=300, bbox_inches='tight')



#%% Increase and decrease of cumulative error

####   Increase   ####         primMotor, preMot dorsal, VisMotor, VisualSec, SupramargGyr

# PrimMot
fig = plt.figure(figsize=(7, 4))
primmot = nilearn.image.load_img('E:/Manip_IRM/spm_2ndLvlOutputs_separated_trials_AROMA/demean_3PM_cumulativeError/adapt_day1_vs_adapt_day2_Motor_prim_EM/spm_thresh.nii')
display=plot_glass_brain(None, display_mode='yz', figure=fig)
display.add_contours(primmot, levels=[1.], colors='r',linewidths=3)
red = Rectangle((1, 1), 1, 1, fc="r")
plt.legend([red],["PrimMotor (4)"], fontsize=17, bbox_to_anchor=(-0.5,-0.1, 1, 1))
plt.savefig('E:/Manip_IRM/Nilearn/PrimMot.png', dpi=300, bbox_inches='tight')

#PreMot dorsal
fig = plt.figure(figsize=(7, 4))
premot1 = nilearn.image.load_img('E:/Manip_IRM/spm_2ndLvlOutputs_separated_trials_AROMA/demean_3PM_cumulativeError/adapt_day1_vs_adapt_day2_Motor_premot_dorsal_EM/spm_thresh.nii')
display=plot_glass_brain(None, display_mode='yz', figure=fig)
display.add_contours(premot1, levels=[1.], colors='orange',linewidths=3)
orange = Rectangle((0, 0), 1, 1, fc="orange")
plt.legend([orange],["PreMot dorsal (6)"], fontsize=17, bbox_to_anchor=(-0.6,-0.1,1,1))
plt.savefig('E:/Manip_IRM/Nilearn/PreMotDorsal.png', dpi=300, bbox_inches='tight')

# PreMot dorsal 2
#fig = plt.figure(figsize=(7, 4))
#premot2 = nilearn.image.load_img('E:/Manip_IRM/spm_2ndLvlOutputs_separated_trials_AROMA/demean_3PM_cumulativeError/adapt_day1_vs_adapt_day2_Parietal_ba6_EM/spm_thresh.nii')
#display=plot_glass_brain(None, display_mode='yz', figure=fig) # image thresholded on spm before
#display.add_contours(premot2, levels=[1.], colors='peru',linewidths=3)
#peru = Rectangle((0, 0), 1, 1, fc="peru")
#plt.legend([peru],["PreMot dorsal #2"], fontsize=17, bbox_to_anchor=(-0.25,-0.1, 1, 1))
#plt.savefig('E:/Manip_IRM/Nilearn/PreMotDorsal2.png', dpi=300, bbox_inches='tight')

# VisMotot
fig = plt.figure(figsize=(7, 4))
vismotor = nilearn.image.load_img('E:/Manip_IRM/spm_2ndLvlOutputs_separated_trials_AROMA/demean_3PM_cumulativeError/adapt_day1_vs_adapt_day2_Parietal_ba7_EM/spm_thresh.nii')
display=plot_glass_brain(None, display_mode='yz', figure=fig)
display.add_contours(vismotor, levels=[1.], colors='saddlebrown',linewidths=3)
saddlebrown = Rectangle((0, 0), 1, 1, fc="saddlebrown")
plt.legend([saddlebrown],["VisMotor (7)"], fontsize=17, bbox_to_anchor=(-0.5,-0.1, 1, 1))
plt.savefig('E:/Manip_IRM/Nilearn/VisMotor.png', dpi=300, bbox_inches='tight')

# Visual sec
fig = plt.figure(figsize=(7, 4))
vissec = nilearn.image.load_img('E:/Manip_IRM/spm_2ndLvlOutputs_separated_trials_AROMA/demean_3PM_cumulativeError/adapt_day1_vs_adapt_day2_Visual_sec_EM/spm_thresh.nii')
display=plot_glass_brain(None, display_mode='yz', figure=fig)
display.add_contours(vissec, levels=[1.], colors='darkcyan',linewidths=3)
darkcyan = Rectangle((0, 0), 1, 1, fc="darkcyan")
plt.legend([darkcyan],["SecVisual (18)"], fontsize=17, bbox_to_anchor=(-0.6,-0.1,1,1))
plt.savefig('E:/Manip_IRM/Nilearn/SecVisual.png', dpi=300, bbox_inches='tight')

# SupremargGyr 1
fig = plt.figure(figsize=(7, 4))
supragyr1 = nilearn.image.load_img('E:/Manip_IRM/spm_2ndLvlOutputs_separated_trials_AROMA/demean_3PM_cumulativeError/adapt_day1_vs_adapt_day2_ba40_2_EM/spm_thresh.nii')
display=plot_glass_brain(None, display_mode='yz', figure=fig)
display.add_contours(supragyr1, levels=[1.], colors='purple',linewidths=3)
purple = Rectangle((0, 0), 1, 1, fc="purple")
plt.legend([purple],["SupramargGyr (40)"], fontsize=17, bbox_to_anchor=(-0.6,-0.1, 1, 1))
plt.savefig('E:/Manip_IRM/Nilearn/SupramargGyr1.png', dpi=300, bbox_inches='tight')

####   Decrease   ####             
# cerebellum VI
fig = plt.figure(figsize=(7, 4))
crbllm = nilearn.image.load_img('E:/Manip_IRM/spm_2ndLvlOutputs_separated_trials_AROMA/demean_3PM_cumulativeError/adapt_day1_vs_adapt_day2_Cerebellum_EM/spm_threshold.nii')
display=plot_glass_brain(None, display_mode='yz', figure=fig)
display.add_contours(crbllm, levels=[1.], colors='y',linewidths=3)
yellow = Rectangle((0, 0), 1, 1, fc="y")
plt.legend([yellow],["Crbllm_VI"], fontsize=17, bbox_to_anchor=(-0.5,-0.12, 1, 1))
plt.savefig('E:/Manip_IRM/Nilearn/Crbllm_VI.png', dpi=300, bbox_inches='tight')

#%% All subject pre1_post2 for ba40 AND readapt pre2_post2 for ba40_old and SMA

# ba40 old for pre1_post2
fig = plt.figure(figsize=(10, 6))
m1 = nilearn.image.load_img('E:/Manip_IRM/conn_X_static/results/secondlevel/SBC_01/AllSubjects/pre1(-1).post2(1)/atlas_rois.left_ba40/M1.img')
plot_glass_brain(m1, display_mode='yz', title='SupramargGyr(40) #1', colorbar=True, cmap='ocean_hot', vmax=8.5, figure=fig)
plt.savefig('E:/Manip_IRM/Nilearn/supramargyr_1.png', dpi=300, bbox_inches='tight')

# ba40 readapt for pre2_post2
fig = plt.figure(figsize=(7, 4))
s1 = nilearn.image.load_img('E:/Manip_IRM/conn_X_static/results/secondlevel/SBC_01/AllSubjects(0).Readapt(1)/post2(1).pre2(-1)/atlas_rois.left_ba40/S1_2.img')
display=plot_glass_brain(None, display_mode='yz', figure=fig)
display.add_contours(s1, levels=[1.], colors='violet',linewidths=3)
violet = Rectangle((0, 0), 1, 1, fc="violet")
plt.legend([violet],["SupramargGyr(40) #1"], fontsize=17, bbox_to_anchor=(-0.6,-0.12, 1, 1))
plt.savefig('E:/Manip_IRM/Nilearn/S1.png', dpi=300, bbox_inches='tight')

# SMA readapt for pre2_post2
fig = plt.figure(figsize=(7, 4))
s1 = nilearn.image.load_img('E:/Manip_IRM/conn_X_static/results/secondlevel/SBC_01/AllSubjects(0).Readapt(1)/post2(1).pre2(-1)/atlas_rois.left_SMA/S1.img')
display=plot_glass_brain(None, display_mode='yz', figure=fig)
display.add_contours(s1, levels=[1.], colors='black',linewidths=3)
black = Rectangle((0, 0), 1, 1, fc="black")
plt.legend([black],["SMA"], fontsize=17, bbox_to_anchor=(-0.3,-0.1, 1, 1))
plt.savefig('E:/Manip_IRM/Nilearn/S1_2.png', dpi=300, bbox_inches='tight')

#%% Rois represntation

fig = plt.figure(figsize=(8, 8))

# Load all the ROIs
crbllm = nilearn.image.load_img('E:/Manip_IRM/spm_1stLvlOutputs_separated_trials_AROMA/ROIs_conn/Cerebellum.nii')
crbllm2 = nilearn.image.load_img('E:/Manip_IRM/spm_1stLvlOutputs_separated_trials_AROMA/ROIs_conn/Crbllm_rightVIII.nii')
premot1 = nilearn.image.load_img('E:/Manip_IRM/spm_1stLvlOutputs_separated_trials_AROMA/ROIs_conn/Motor_premot_dorsal.nii')
#premot2 = nilearn.image.load_img('E:/Manip_IRM/spm_1stLvlOutputs_separated_trials_AROMA/ROIs_conn/Parietal_ba6.nii')
primmot = nilearn.image.load_img('E:/Manip_IRM/spm_1stLvlOutputs_separated_trials_AROMA/ROIs_conn/Motor_prim.nii')
primsensory = nilearn.image.load_img('E:/Manip_IRM/spm_1stLvlOutputs_separated_trials_AROMA/ROIs_conn/Motor_S1.nii')
#supragyr1 = nilearn.image.load_img('E:/Manip_IRM/spm_1stLvlOutputs_separated_trials_AROMA/ROIs_conn/Parietal_ba40.nii')
supragyr2 = nilearn.image.load_img('E:/Manip_IRM/spm_1stLvlOutputs_separated_trials_AROMA/ROIs_conn/ba40_2.nii')
visprim = nilearn.image.load_img('E:/Manip_IRM/spm_1stLvlOutputs_separated_trials_AROMA/ROIs_conn/Visual_prim.nii')
vissec = nilearn.image.load_img('E:/Manip_IRM/spm_1stLvlOutputs_separated_trials_AROMA/ROIs_conn/Visual_sec.nii')
visassoc = nilearn.image.load_img('E:/Manip_IRM/spm_1stLvlOutputs_separated_trials_AROMA/ROIs_conn/Visual_assoc.nii')
sma = nilearn.image.load_img('E:/Manip_IRM/spm_1stLvlOutputs_separated_trials_AROMA/ROIs_conn/Motor_SMA.nii')
vismotor = nilearn.image.load_img('E:/Manip_IRM/spm_1stLvlOutputs_separated_trials_AROMA/ROIs_conn/Parietal_ba7.nii')
putamen = nilearn.image.load_img('E:/Manip_IRM/spm_1stLvlOutputs_separated_trials_AROMA/ROIs_conn/left_putamen.nii')

# Display the ROIs on the same figure
display=plot_glass_brain(None, display_mode='yz', figure=fig)
display.add_contours(crbllm, colors='y', filled=True, linewidths=1)
display.add_contours(crbllm2, colors='g', filled=True, linewidths=1)
display.add_contours(premot1, colors='orange', filled=True, linewidths=1)
#display.add_contours(premot2, colors='peru', filled=True, linewidths=1)
display.add_contours(primmot, colors='r', filled=True, linewidths=1)
display.add_contours(primsensory, colors='pink', filled=True, linewidths=1)
#display.add_contours(supragyr1, colors='violet', filled=True, linewidths=1)
display.add_contours(supragyr2, colors='purple', filled=True, linewidths=1)
display.add_contours(visprim, colors='cyan', filled=True, linewidths=1)
display.add_contours(vissec, colors='darkcyan', filled=True, linewidths=1)
display.add_contours(visassoc, colors='royalblue', filled=True, linewidths=1)
display.add_contours(sma, colors='black', filled=True, linewidths=1)
display.add_contours(vismotor, colors='saddlebrown', filled=True, linewidths=1)
display.add_contours(putamen, colors='grey', filled=True, linewidths=1)

# Add legend
yellow = Rectangle((0, 0), 1, 1, fc="y")
green = Rectangle((0, 0), 1, 1, fc="g")
orange = Rectangle((0, 0), 1, 1, fc="orange")
#peru = Rectangle((0, 0), 1, 1, fc="peru")
red = Rectangle((0, 0), 1, 1, fc="r")
pink = Rectangle((0, 0), 1, 1, fc="pink")
#violet = Rectangle((0, 0), 1, 1, fc="violet")
purple = Rectangle((0, 0), 1, 1, fc="purple")
cyan = Rectangle((0, 0), 1, 1, fc="cyan")
darkcyan = Rectangle((0, 0), 1, 1, fc="darkcyan")
royalblue = Rectangle((0, 0), 1, 1, fc="royalblue")
black = Rectangle((0, 0), 1, 1, fc="black")
saddlebrown = Rectangle((0, 0), 1, 1, fc="saddlebrown")
grey = Rectangle((0, 0), 1, 1, fc="grey")
plt.legend([yellow, green, orange, red, pink, purple, cyan, darkcyan, royalblue, black, saddlebrown, grey],["Crbllm_VI", "Crbllm_VIIIb", \
           "PreMot dorsal (6)", "PrimMotor (4)", "PrimSensory (1)",  "SupramargGyr (40)", \
           "PrimVisual (17)", "SecVisual (18)", "VisualAssoc (19)", "SMA (6)", "VisMotor (7)", "Putamen",], fontsize=10, bbox_to_anchor=(1,0), ncol=4)

plt.savefig('E:/Manip_IRM/Nilearn/rois3.png', dpi=300, bbox_inches='tight')


#%% Histograms

# 'mean' and 'interval' values are coming from spm contrast estimates

x=[1, 2, 3] # abscisse

# PrimMotor
fig = plt.figure(figsize=(2,4))
mean = 1.32
interval = 1.5343
y=[0, mean, 0]
error=[0, interval/2, 0]
label=[round(mean+interval/2,2), round(mean-interval/2,2)]
plt.tick_params(right = False, labelbottom = False, bottom = False, left=False, labelleft=False)
plt.bar(x, height=y, width = 1, color = 'r', linewidth = 2, yerr = error, ecolor = 'black', capsize = 5)
plt.ylabel('CE', fontsize=14)
plt.annotate(str(mean),xy=(2.3,mean+0.01), fontsize=14)
plt.annotate(str(label[0]),xy=(2.3,label[0]-0.05), fontsize=14)
plt.annotate(str(label[1]),xy=(2.3,label[1]-0.05), fontsize=14)
plt.savefig('E:/Manip_IRM/Nilearn/hist_M1.png', dpi=300, bbox_inches='tight')

# PreMot dorsal
fig = plt.figure(figsize=(2,4))
mean = 1.44
interval = 1.6042
y=[0, mean, 0]
error=[0, interval/2, 0]
label=[round(mean+interval/2,2), round(mean-interval/2,2)]
plt.tick_params(right = False, labelbottom = False, bottom = False, left=False, labelleft=False)
plt.bar(x, height=y, width = 1, color = 'orange', linewidth = 2, yerr = error, ecolor = 'black', capsize = 5)
plt.ylabel('CE', fontsize=14)
plt.annotate(str(mean),xy=(2.3,mean+0.01), fontsize=14)
plt.annotate(str(label[0]),xy=(2.3,label[0]-0.05), fontsize=14)
plt.annotate(str(label[1]),xy=(2.3,label[1]-0.05), fontsize=14)
plt.savefig('E:/Manip_IRM/Nilearn/hist_dorsal.png', dpi=300, bbox_inches='tight')

# SupramarGyr
fig = plt.figure(figsize=(2,4))
mean = 0.75
interval = 0.7040
y=[0, mean, 0]
error=[0, interval/2, 0]
label=[round(mean+interval/2,2), round(mean-interval/2,2)]
plt.tick_params(right = False, labelbottom = False, bottom = False, left=False, labelleft=False)
plt.bar(x, height=y, width = 1, color = 'purple', linewidth = 2, yerr = error, ecolor = 'black', capsize = 5)
plt.ylabel('CE', fontsize=14)
plt.annotate(str(mean),xy=(2.3,mean+0.01), fontsize=14)
plt.annotate(str(label[0]),xy=(2.3,label[0]-0.05), fontsize=14)
plt.annotate(str(label[1]),xy=(2.3,label[1]-0.05), fontsize=14)
plt.savefig('E:/Manip_IRM/Nilearn/hist_supramargyr.png', dpi=300, bbox_inches='tight')

# VisMotor
fig = plt.figure(figsize=(2,4))
mean = 1.44
interval = 1.5665
y=[0, mean, 0]
error=[0, interval/2, 0]
label=[round(mean+interval/2,2), round(mean-interval/2,2)]
plt.tick_params(right = False, labelbottom = False, bottom = False, left=False, labelleft=False)
plt.bar(x, height=y, width = 1, color = 'saddlebrown', linewidth = 2, yerr = error, ecolor = 'black', capsize = 5)
plt.ylabel('CE', fontsize=14)
plt.annotate(str(mean),xy=(2.3,mean+0.01), fontsize=14)
plt.annotate(str(label[0]),xy=(2.3,label[0]-0.05), fontsize=14)
plt.annotate(str(label[1]),xy=(2.3,label[1]-0.05), fontsize=14)
plt.savefig('E:/Manip_IRM/Nilearn/hist_vismotor.png', dpi=300, bbox_inches='tight')

# SecVisual
fig = plt.figure(figsize=(2,4))
mean = 1.45
interval = 1.5135
y=[0, mean, 0]
error=[0, interval/2, 0]
label=[round(mean+interval/2,2), round(mean-interval/2,2)]
plt.tick_params(right = False, labelbottom = False, bottom = False, left=False, labelleft=False)
plt.bar(x, height=y, width = 1, color = 'darkcyan', linewidth = 2, yerr = error, ecolor = 'black', capsize = 5)
plt.ylabel('CE', fontsize=14)
plt.annotate(str(mean),xy=(2.3,mean+0.01), fontsize=14)
plt.annotate(str(label[0]),xy=(2.3,label[0]-0.05), fontsize=14)
plt.annotate(str(label[1]),xy=(2.3,label[1]-0.05), fontsize=14)
plt.savefig('E:/Manip_IRM/Nilearn/hist_secvisual.png', dpi=300, bbox_inches='tight')

# Crbllm VI
fig = plt.figure(figsize=(2,4))
mean = -1.23
interval = 1.3821
y=[0, mean, 0]
error=[0, interval/2, 0]
label=[round(mean+interval/2,2), round(mean-interval/2,2)]
plt.tick_params(right = False, labelbottom = False, bottom = False, left=False, labelleft=False)
plt.bar(x, height=y, width = 1, color = 'y', linewidth = 2, yerr = error, ecolor = 'black', capsize = 5)
plt.ylabel('CE', fontsize=14)
plt.annotate(str(mean),xy=(2.3,mean+0.01), fontsize=14)
plt.annotate(str(label[0]),xy=(2.3,label[0]-0.05), fontsize=14)
plt.annotate(str(label[1]),xy=(2.3,label[1]-0.05), fontsize=14)
plt.savefig('E:/Manip_IRM/Nilearn/hist_crbllm.png', dpi=300, bbox_inches='tight')


# Histogram with pre2 and post2 for ba40 and SMA
# the values of pre2 and post2 come from conn results explorer import values

# ba40
x=[1, 2]
fig = plt.figure(figsize=(4,5))
pre2 = [-0.0982133, -0.0133183, -0.0804602, 0.318071, 0.253344, 0.120609, -0.131553, 0.138624, 0.0384581, 0.180899, 0.0658724, 0.241766, 0.189133, 0.209855, 0.418303, 0.367656, 0.395243, 0.0623531, 0.00557256, 0.197533, 0.242981, 0.0888484, -0.0434017, 0.142826]
post2 = [0.12886, 0.116628, 0.405559, -0.0277835, 0.258197, 0.0333533, 0.0634676, 0.195874, 0.0300786, 0.422126, 0.0334564, 0.152145, 0.286293, 0.0195684, 0.31184, 0.312046, 0.214435, 0.127311, 0.127017, 0.0733048, 0.0861501, 0.305365, 0.303374, 0.0903723]
mean_pre2 = round(np.mean(pre2),2)
mean_post2 = round(np.mean(post2),2)
y = [mean_pre2, mean_post2]
interval_pre2 = st.t.interval(alpha=0.95, df=len(pre2)-1, loc=np.mean(pre2), scale=st.sem(pre2)) # returns a tuple (min, max) of the confidence interval
interval_pre2 = interval_pre2[1]-interval_pre2[0] # distance of the confidence interval
interval_post2 = st.t.interval(alpha=0.95, df=len(post2)-1, loc=np.mean(post2), scale=st.sem(post2))
interval_post2 = interval_post2[1]-interval_post2[0]
error = [interval_pre2/2, interval_post2/2]
label_pre2 = [round(mean_pre2+interval_pre2/2,2), round(mean_pre2-interval_pre2/2,2)]
label_post2 = [round(mean_post2+interval_post2/2,2), round(mean_post2-interval_post2/2,2)]
plt.tick_params(right = False, bottom = False, left=False, labelleft=False)
plt.bar(x, height=y, width = 0.8, color = 'violet', linewidth = 2, yerr = error, ecolor = 'black', capsize = 5)
plt.ylabel('CE', fontsize=14)
plt.xticks([1, 2], ['pre2', 'post2'], fontsize=14) 
plt.annotate(str(mean_pre2),xy=(1.05,mean_pre2+0.005), fontsize=14)
plt.annotate(str(mean_post2),xy=(2.05,mean_post2+0.005), fontsize=14)
plt.annotate(str(label_pre2[0]),xy=(1.05,label_pre2[0]), fontsize=14)
plt.annotate(str(label_pre2[1]),xy=(1.05,label_pre2[1]), fontsize=14)
plt.annotate(str(label_post2[0]),xy=(2.05,label_post2[0]), fontsize=14)
plt.annotate(str(label_post2[1]),xy=(2.05,label_post2[1]), fontsize=14)
plt.savefig('E:/Manip_IRM/Nilearn/hist_supramargyr_1.png', dpi=300, bbox_inches='tight')

# SMA
x=[1, 2]
fig = plt.figure(figsize=(4,5))
pre2 = [-0.01939792, 0.08677806, 0.2221149, 0.1861468, 0.581609, 0.6003602, 0.3187778, 0.1756316, 0.293006, 0.8703499, 0.1784654, 0.3757375, 0.4117182, 1.041513, 1.223635, 1.078396, 1.287471, 0.9656171, 0.2251019, 0.7784938, 0.3055213, 0.5510055, 0.4410167, 0.370882]
post2 = [0.692316, 0.3298524, 0.7750978, -0.2148003, 0.4721827, 0.6228466, 0.5186367, 0.2608877, 0.7871181, 0.994553, 0.4044947, 0.5028513, 0.5518883, 0.4704521, 1.169719, 0.9523677, 1.168622, 1.231058, 0.4621864, 0.776305, 0.3417213, 0.823197, 0.5079684, 0.352776]
mean_pre2 = round(np.mean(pre2),2)
mean_post2 = round(np.mean(post2),2)
y = [mean_pre2, mean_post2]
interval_pre2 = st.t.interval(alpha=0.95, df=len(pre2)-1, loc=np.mean(pre2), scale=st.sem(pre2))
interval_pre2 = interval_pre2[1]-interval_pre2[0]
interval_post2 = st.t.interval(alpha=0.95, df=len(post2)-1, loc=np.mean(post2), scale=st.sem(post2))
interval_post2 = interval_post2[1]-interval_post2[0]
error = [interval_pre2/2, interval_post2/2]
label_pre2 = [round(mean_pre2+interval_pre2/2,2), round(mean_pre2-interval_pre2/2,2)]
label_post2 = [round(mean_post2+interval_post2/2,2), round(mean_post2-interval_post2/2,2)]
plt.tick_params(right = False, bottom = False, left=False, labelleft=False)
plt.bar(x, height=y, width = 0.8, color = 'black', linewidth = 2, yerr = error, ecolor = 'gray', capsize = 5)
plt.ylabel('CE', fontsize=14)
plt.xticks([1, 2], ['pre2', 'post2'], fontsize=14) 
plt.annotate(str(mean_pre2),xy=(1.05,mean_pre2+0.005), fontsize=14)
plt.annotate(str(mean_post2),xy=(2.05,mean_post2+0.005), fontsize=14)
plt.annotate(str(label_pre2[0]),xy=(1.05,label_pre2[0]), fontsize=14)
plt.annotate(str(label_pre2[1]),xy=(1.05,label_pre2[1]), fontsize=14, color='silver')
plt.annotate(str(label_post2[0]),xy=(2.05,label_post2[0]), fontsize=14)
plt.annotate(str(label_post2[1]),xy=(2.05,label_post2[1]), fontsize=14, color='silver')
plt.savefig('E:/Manip_IRM/Nilearn/hist_sma_1.png', dpi=300, bbox_inches='tight')


#%% Atlas de HMAT

# Load the Rois (begin with a 'l' is left, begin with a 'r' is right)
lm1 = nilearn.image.load_img('E:/Manip_IRM/Atlas_HMAT/HMAT_Left_M1.nii')
lpmd = nilearn.image.load_img('E:/Manip_IRM/Atlas_HMAT/HMAT_Left_PMd.nii')
lpmv = nilearn.image.load_img('E:/Manip_IRM/Atlas_HMAT/HMAT_Left_PMv.nii')
lpresma = nilearn.image.load_img('E:/Manip_IRM/Atlas_HMAT/HMAT_Left_preSMA.nii')
ls1 = nilearn.image.load_img('E:/Manip_IRM/Atlas_HMAT/HMAT_Left_S1.nii')
lsma = nilearn.image.load_img('E:/Manip_IRM/Atlas_HMAT/HMAT_Left_SMA.nii')
rm1 = nilearn.image.load_img('E:/Manip_IRM/Atlas_HMAT/HMAT_Right_M1.nii')
rpmd = nilearn.image.load_img('E:/Manip_IRM/Atlas_HMAT/HMAT_Right_PMd.nii')
rpmv = nilearn.image.load_img('E:/Manip_IRM/Atlas_HMAT/HMAT_Right_PMv.nii')
rpresma = nilearn.image.load_img('E:/Manip_IRM/Atlas_HMAT/HMAT_Right_preSMA.nii')
rs1 = nilearn.image.load_img('E:/Manip_IRM/Atlas_HMAT/HMAT_Right_S1.nii')
rsma = nilearn.image.load_img('E:/Manip_IRM/Atlas_HMAT/HMAT_Right_SMA.nii')

# Display each ROI on a different figure (left and right on the same one)

# M1
fig = plt.figure(figsize=(6, 6))
display = plot_glass_brain(None, display_mode='yz', figure=fig, title='M1')
display.add_contours(lm1, colors='r', filled=True, linewidths=1)
display.add_contours(rm1, colors='r', filled=True, linewidths=1)
plt.savefig('E:/Manip_IRM/Nilearn/Atlas_HMAT_images_nilearn/M1.png', dpi=300, bbox_inches='tight')

# PMd
fig = plt.figure(figsize=(6, 6))
display = plot_glass_brain(None, display_mode='yz', figure=fig, title='PMd')
display.add_contours(lpmd, colors='orange', filled=True, linewidths=1)
display.add_contours(rpmd, colors='orange', filled=True, linewidths=1)
plt.savefig('E:/Manip_IRM/Nilearn/Atlas_HMAT_images_nilearn/PMd.png', dpi=300, bbox_inches='tight')

# PMv
fig = plt.figure(figsize=(6, 6))
display = plot_glass_brain(None, display_mode='yz', figure=fig, title='PMv')
display.add_contours(lpmv, colors='peru', filled=True, linewidths=1)
display.add_contours(rpmv, colors='peru', filled=True, linewidths=1)
plt.savefig('E:/Manip_IRM/Nilearn/Atlas_HMAT_images_nilearn/PMv.png', dpi=300, bbox_inches='tight')

# preSMA
fig = plt.figure(figsize=(6, 6))
display = plot_glass_brain(None, display_mode='yz', figure=fig, title='preSMA')
display.add_contours(lpresma, colors='dimgrey', filled=True, linewidths=1)
display.add_contours(rpresma, colors='dimgrey', filled=True, linewidths=1)
plt.savefig('E:/Manip_IRM/Nilearn/Atlas_HMAT_images_nilearn/preSMA.png', dpi=300, bbox_inches='tight')

# S1
fig = plt.figure(figsize=(6, 6))
display = plot_glass_brain(None, display_mode='yz', figure=fig, title='S1')
display.add_contours(ls1, colors='pink', filled=True, linewidths=1)
display.add_contours(rs1, colors='pink', filled=True, linewidths=1)
plt.savefig('E:/Manip_IRM/Nilearn/Atlas_HMAT_images_nilearn/S1.png', dpi=300, bbox_inches='tight')

# SMA
fig = plt.figure(figsize=(6, 6))
display = plot_glass_brain(None, display_mode='yz', figure=fig, title='SMA')
display.add_contours(lsma, colors='black', filled=True, linewidths=1)
display.add_contours(rsma, colors='black', filled=True, linewidths=1)
plt.savefig('E:/Manip_IRM/Nilearn/Atlas_HMAT_images_nilearn/SMA.png', dpi=300, bbox_inches='tight')

