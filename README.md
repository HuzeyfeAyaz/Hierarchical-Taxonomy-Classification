# Hierarchical Taxonomy Classification and Robustness Analysis
- The goal of this project is building Hierarchical ML models to minimize the effort of taxonomy classification.

### Data-Set:
- We have 5 main dataset namely Aves, Chiroptera, Rodentia, Polypodiopsida, and Pucciniomycetes.
- We employed all experiments on combined dataset which includes all samples in five datasets.
- Features of each dataset increases exponentially as 4^k (ie. for 7k-merized data we have 4^7=16384 features)
- For the creating DNA barcode sequence, k neighbors of each DNA bases has taken from original DNA sequence as label and the features of that labels are counts of how much included in a sample. That is called as k-merization approach.
- 7k-merized combined modified data has used for the experiment of robustness analysis.
- Each kmerized dataset we used for hierarchical classification and robustness analysis occupying almost 200 mb and 500 mb storage respectively.

### Non-Hierarchical Classification:
- Linear Support Vector Machine (LinearSVM), Radial Support Vector Machine, and Random Forests (RF) used for this experiment.
- Performed on combined specie level data.

### Hierarchical classification:
- We applied 6 SVM and RF estimator in this step that one of them predicts the class level of taxonomies from combined dataset and other 5 have used to predicts the species level according to class level prediction.
- 10-Fold cross validation has employed for this experiment.

### Robustness Analysis:
- In this approach we evaluated the stability and robustness of each classifier.
- For Robustness analysis we modified the dataset which created as randomly distributed DNA bases and characters such as A, T, G, C, -, Na.
- Each kmerized data costs 6-8 days for compiling since SVM makes single core computation.
- Instead of standard computer, Lab server used for this experiment due to high memory requirements

### Contributors:
- [Ali Cakmak](https://github.com/alicakmak)
- [Ali Reza Ibrahimzada](https://github.com/ali0jn)

### Server Specs we used:
- Dell R720, 2 x Intel Xeon E5-2620V2 / 2.1 GHz 24core vCPU, 128GB Ram, 2.4 TB Storage.

Please read our paper for more detail.

