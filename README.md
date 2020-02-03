# Hierarchical Taxonomy Classification and Robustness Analysis
- The goal is this project, building an estimation model for Taxonomy classification and Species estimation.

### Data-Set:
- We have 3 main dataset namely Aves, Chiroptera, and Rodentia.
- We employed all experiments on combined dataset which includes Aves, Chiroptera, Rodentia datasets.
- For creating DNA barcode sequence we got the count of k neighbors of each DNA bases from original DNA sequence. That is called k-merization.
- We used 7kmerized data and modify it for robustness analysis.
- Each kmerized dataset we used almost 200 mb and 500 mb for hierarchical classification and robustness analysis respectively.

### Hierarchical SVM classification:
- We apply 4 SVM estimator in this step. one of them predicts the class level of taxonomies on combined dataset and other tree predicts the species according to class level prediction.
- We used 10-Fold cross validation for this experiment

### Robustness Analysis:
- In this approach we are observing the stability and robustness of the classifiers.
- For Robustness analysis we modified the dataset with random DNA bases and characters such as A, T, G, C, -, Na.
- Each kmerized data costs 6-8 days for compiling since we have relatively high dataset. Additionally, we could not used regular computer for this experiment because of high memory requirements

### Server Specs:
- Dell R720, 2x Intel Xeon E5 24 vCPU, 128GB Ram, 2.5 TB Storage.

