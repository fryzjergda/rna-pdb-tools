#!/usr/bin/env python

from rna_pdb_tools.pdb_parser_lib import *
from pymol import cmd

def color_by_text(txt):
  for t in txt.strip().split('\n'):
      color, resi = t.replace('color ', '').split(',')
      print(color, resi)
      cmd.color(color.strip(), resi.strip())

def rp():
    """rna like in papers ;-)"""
    cmd.hide("sticks", "all")
    cmd.hide("lines", "all")
    cmd.show("cartoon", "all")
    cmd.set("cartoon_ring_mode", 3)
    cmd.set("cartoon_ring_finder", 2)
    cmd.set("cartoon_ladder_mode", 1)

def get_pdb():
    """ """
    tmpfn = '/tmp/pymol_get_pdb.pdb'
    cmd.save(tmpfn, '(sele)')
    s = StrucFile(tmpfn)
    for l in s.lines:
      print l

def p():
    cmd.set("seq_view_format", 4)
    cmd.set("seq_view", 1)
    cmd.set("seq_view_location", 1)
    cmd.set("seq_view_overlay", 1)

def rna_cartoon():
    """http://www-cryst.bioc.cam.ac.uk/members/zbyszek/figures_pymol

    .. image :: ../pngs/rna_cartoon.png
    """
    cmd.set("cartoon_ring_mode", 3)
    cmd.set("cartoon_ring_finder", 1)
    cmd.set("cartoon_ladder_mode", 1)
    cmd.set("cartoon_nucleic_acid_mode", 4)
    cmd.set("cartoon_ring_transparency", 0.5)

def rp17():
    txt ="""color forest, resi 1-5+12-16; # p1
 color magenta, resi 6-11+34-39
 color grey, resi 17-24
 color marine, resi 25-28+55-58 
 color deepblue, resi 29-33+40-42
 color orange, resi 42-47+48-52;
 color yellow, resi 53-54;

"""
    color_by_text(txt)

print '   PyMOL4RNA   '
print '==============='
print 'p - prepare seq for printing'    
print 'rp - rna present, object names only click to get compact legend'
print 'rp17'
print 'get_pdb'
print 'rna_cartoon'

cmd.extend('rp17', rp17)
cmd.extend('rp', rp)   
cmd.extend('p', p)   
cmd.extend('get_pdb', get_pdb)
cmd.extend('rna_cartoon', rna_cartoon)
