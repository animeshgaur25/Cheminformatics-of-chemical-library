# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:25:00 2019

@author: KineticFanatic
"""
import os
from rdkit import rdBase
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem import rdChemReactions
from rdkit.Chem import rdMolDescriptors
from IPython.display import display
from rdkit.Chem import PandasTools
import pandas as pd
import xlwt
from rdkit import RDConfig

rxn = AllChem.ReactionFromSmarts('[C:1](=[O:2])[O:3].[N:4].[C:5]=[O:6].[C-:7]#[N+:8]>>[C:1](=[O:2])[N:4][C:5][C:7](=[O:3])[N:8][H:9]')
display(Draw.ReactionToImage(rxn))
 
Aldehyde = Chem.MolFromSmiles("CCC=O")
cAcid = Chem.MolFromSmiles("CCCC(O)=O")
amine = Chem.MolFromSmiles("CCCN")
iCyanide = Chem.MolFromSmiles("[C-]#[N+]c1ccccc1")
display(Draw.MolsToGridImage([amine, Aldehyde, cAcid, iCyanide]))

reactant_1_ListMols = [cAcid]
reactant_2_ListMols = [amine]
reactant_3_ListMols = [Aldehyde]
reactant_4_ListMols = [iCyanide]

prods = AllChem.EnumerateLibraryFromReaction(rxn,[reactant_1_ListMols, reactant_2_ListMols, reactant_3_ListMols, reactant_4_ListMols])

smis = list(set([Chem.MolToSmiles(x[0], isomericSmiles=True) for x in prods]))
print (smis)