Getting Started: I want to ...
===========================================

fetch a structure from the PDB database
--------------------------------------------

Example::

  $ rna_pdb_tools.py --fetch 1xjr
  downloading...1xjr ok

fetch a biologicaly assembly
--------------------------------------------

Example::

  $ rna_pdb_tools.py --fetch_ba 1xjr
  downloading...1xjr_ba.pdb ok

or over a list of pdb ids in a text file::

  $ cat data/pdb_ids.txt
  1y26
  1fir

  $ while read p; do rna_pdb_tools.py --fetch_ba $p; done < data/pdb_ids.txt
  downloading...1y26_ba.pdb ok
  downloading...1fir_ba.pdb ok

  $ ls *.pdb
  1fir_ba.pdb 1y26_ba.pdb

delete a part of of your structure
--------------------------------------------

Examples::

    $ for i in `ls *pdb`; do rna_pdb_tools.py --delete A:46-56 $i > ../rpr_rm_loop/$i ; done

go over all files in the current directory, remove a fragment of chain A, residues between 46-56 (including them) and save outputs to in the folder `rpr_rm_loops`.

get numbering of your structure and rename chains
----------------------------------------------------
Rename chain B in structure 4_das_1_rpr.pdb::

  $ rna_pdb_tools.py --get_seq  4_das_1_rpr.pdb
  > 4_das_1_rpr.pdb B:1-126
  GGCUUAUCAAGAGAGGUGGAGGGACUGGCCCGAUGAAACCCGGCAACCACUAGUCUAGCGUCAGCUUCGGCUGACGCUAGGCUAGUGGUGCCAAUUCCUGCAGCGGAAACGUUGAAAGAUGAGCCA
  $ rna_pdb_tools.py --edit 'B:1-126>A:1-126' 4_das_1_rpr.pdb > 4_das_1_rpr2.pdb
  $ rna_pdb_tools.py --get_seq  4_das_1_rpr2.pdb
  > 4_das_1_rpr2.pdb A:1-126
  GGCUUAUCAAGAGAGGUGGAGGGACUGGCCCGAUGAAACCCGGCAACCACUAGUCUAGCGUCAGCUUCGGCUGACGCUAGGCUAGUGGUGCCAAUUCCUGCAGCGGAAACGUUGAAAGAUGAGCCA

edit your structure (rename chain)
--------------------------------------------

Examples::

   $ rna_pdb_tools.py --edit 'A:3-21>A:1-19' 1f27_clean.pdb > 1f27_clean_A1-19.pdb

or even::

   $ rna_pdb_tools.py --edit 'A:3-21>A:1-19,B:22-32>B:20-30' 1f27_clean.pdb > 1f27_clean_renumb.pdb

find missing atoms in my structure
--------------------------------------------

Run::

    $ rna_pdb_tools.py --get_rnapuzzle_ready input/1_das_1_rpr_fixed.pdb
    HEADER Generated with rna-pdb-tools
    HEADER ver 91ed4f8-dirty
    HEADER https://github.com/mmagnus/rna-pdb-tools
    HEADER Sun Mar  5 10:58:07 2017
    REMARK 000 Missing atoms:
    REMARK 000  + P B <Residue C het=  resseq=1 icode= > residue # 1
    REMARK 000  + OP1 B <Residue C het=  resseq=1 icode= > residue # 1
    REMARK 000  + OP2 B <Residue C het=  resseq=1 icode= > residue # 1
    REMARK 000  + O5' B <Residue C het=  resseq=1 icode= > residue # 1
    ATOM      1  P     C A   1     -16.936  -3.789  68.770  1.00 11.89           P
    ATOM      2  OP1   C A   1     -17.105  -3.675  67.302  1.00 14.35           O
    ATOM      3  OP2   C A   1     -15.666  -4.265  69.342  1.00 12.68           O
    ...

add missing atoms
--------------------------------------------

.. argparse::
   :ref: rna_pdb_tools.rna_pdb_rnapuzzle_ready.get_parser
   :prog: rna_pdb_rnapuzzle_ready.py

The tool is using the function:

.. automethod:: rna_pdb_tools.pdb_parser_lib.StrucFile.get_rnapuzzle_ready
	  
