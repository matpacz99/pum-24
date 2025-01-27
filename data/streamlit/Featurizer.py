class Featurizer:
    def __init__(self, train_smiles):
        self.train_df = pd.DataFrame()
        
        self.train_df['smiles'] = train_smiles
        
        
        self.train_df['mol'] = self.train_df['smiles'].apply(Chem.MolFromSmiles)
        self.train_df['mol_wt'] = df['mol'].apply(rdMolDescriptors.CalcExactMolWt)             
        self.train_df['logp'] = df['mol'].apply(Crippen.MolLogP)                               
        self.train_df['num_heavy_atoms'] = df['mol'].apply(rdMolDescriptors.CalcNumHeavyAtoms) 
        self.train_df['num_HBD'] = df['mol'].apply(rdMolDescriptors.CalcNumHBD)                
        self.train_df['num_HBA'] = df['mol'].apply(rdMolDescriptors.CalcNumHBA)                
        self.train_df['aromatic_rings'] = df['mol'].apply(rdMolDescriptors.CalcNumAromaticRings)

        self.x_list = ['logp', 'num_heavy_atoms', 'num_HBD', 'num_HBA', 'aromatic_rings']
        self.train_X = self.train_df[self.x_list]
        self.scaler = StandardScaler().fit(self.train_X)

        self.X = None
        self.scaled_X = None

        self.df = pd.DataFrame()
        
 
           
    def featurize(self, smiles):
        self.df['SMILES'] = smiles

        self.df['mol'] = df['SMILES'].apply(Chem.MolFromSmiles)

        self.df['mol_wt'] = df['SMILES'].apply(Chem.MolFromSmiles).apply(rdMolDescriptors.CalcExactMolWt)            
        self.df['logp'] = df['mol'].apply(Crippen.MolLogP)                               
        self.df['num_heavy_atoms'] = df['mol'].apply(rdMolDescriptors.CalcNumHeavyAtoms) 
        self.df['num_HBD'] = df['mol'].apply(rdMolDescriptors.CalcNumHBD)                
        self.df['num_HBA'] = df['mol'].apply(rdMolDescriptors.CalcNumHBA)              
        self.df['aromatic_rings'] = df['mol'].apply(rdMolDescriptors.CalcNumAromaticRings)

        self.df[self.x_list] = self.scaler.transform(self.df[self.x_list])

        return self.df[self.x_list]