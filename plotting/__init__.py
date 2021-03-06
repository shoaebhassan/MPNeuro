# -*- coding: utf-8 -*-
"""
Created on Tue Jun 03 15:19:53 2014

@author: Michael Patterson, Palmiter lab, (map222@uw.edu)

Basic plotting functions
"""

import numpy as np
import pdb
import matplotlib.pyplot as plt
import math

def plot_hist_firingrate(bins, firing_rates, labels = ' ', firing_sem = []):
    ''' Plots a histogram of spike firing rates
    
    Arguments:
    bins: bins of histogram to be used as timepoints for x-axis
    firing_rates: N x (size(bins)) array of firing rates for different neurons
    labels: Labels for the neurons to be used in legends
    firing_sem: error bars to be used in plotting
    '''
    
    if labels == ' ':  # if no labels passed in, just generate generic labels
        labels = [str(i) for i in range(len(bins)) ]
    if np.shape(firing_sem)[0] == 0:
        firing_sem = np.zeros(np.shape(firing_rates))
    
    # setup
    bins2 = bins[:-1] + (bins[1]-bins[0])/2 # offset bins to center them
    fig = plt.figure(figsize = [12, 6])
    ax = fig.add_subplot(1,1,1)
    #lw = 4 # linewidth
    colorj = ['g', 'b', 'k', 'r']

    rate_conversion = 1# bins[1] - bins[0] #use bins to convert to firing rate
    
    # plot all the firing rates
    for i, rows in enumerate(firing_rates):
        #rows = np.convolve(rows, [0.25, 0.5, 0.25], mode = 'same')    
        ax.errorbar(bins2, rows / rate_conversion, yerr = firing_sem[i,:] / rate_conversion,
            label = labels[i], linewidth = math.ceil((i+4 )/ len(colorj)), color = colorj[i%len(colorj)])

    plt.legend(frameon = False)
    prettify_axes(ax)    
    
    plt.xlabel('Time (sec)', fontsize = 18)
    plt.ylabel('Spikes / trial', fontsize = 18)
    plt.show()
        
def raster(aligned_spikes): # copied from internet :)
    fig = plt.figure(figsize = [12, 6])
    ax = fig.add_subplot(1,1,1)
    for ith, trial in enumerate(aligned_spikes):
        ax.vlines(trial, ith + .5, ith + 1.5, color='black', linewidth = 2)
    plt.ylim(.5, len(aligned_spikes) + .5)
    
    prettify_axes(ax)    
    
    plt.xlabel('Time (sec)', fontsize = 18)
    plt.ylabel('Trial', fontsize = 18)
    return ax

def prettify_axes( ax ):
    """ takes a matplot lib axis, and removes the top and right parts of it, then increases font size """
      
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(14)
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(14)