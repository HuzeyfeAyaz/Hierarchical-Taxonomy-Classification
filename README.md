# Hierarchical Taxonomy Classification and Robustness Analysis
- The goal is this project, building an estimation model for Taxonomy classification and Species estimation.

### Data-Set:
- We have 3 main dataset namely Aves, Chiroptera, and Rodentia.
- We employed all experiments on combined dataset which includes all samples in three datasets.
- Features of each dataset increases exponentially as 4^k (ie. for 7k-merized data we have 4^7=16384 features)
- For the creating DNA barcode sequence, k neighbors of each DNA bases has taken from original DNA sequence as label and the features of that labels are counts of how much included in a sample. That is called as k-merization approach.
- 7k-merized combined modified data has used for the experiment of robustness analysis.
- Each kmerized dataset we used for hierarchical classification and robustness analysis occupying almost 200 mb and 500 mb storage respectively.

### Hierarchical SVM classification:
- We applied 4 SVM estimator in this step that one of them predicts the class level of taxonomies from combined dataset and other tree have used to predicts the species level according to class level prediction with using each dataset seperately.
- 10-Fold cross validation has employed for this experiment.

### Robustness Analysis:
- In this approach we evaluated the stability and robustness of each classifier.
- For Robustness analysis we modified the dataset which created as randomly distributed DNA bases and characters such as A, T, G, C, -, Na.
- Each kmerized data costs 6-8 days for compiling since we have relatively high dataset. Additionally, we could not used standard computer for this experiment because of high memory requirements

### 5-Fold Robustness Analysis with PCA technique:
- As I mentioned above compiling each dataset takes between 6-8 days. For that reason, we decided to use PCA dimensionality reduction techniques with 5-fold cross validation instead of 10-fold.
- According to my evaluations, PCA with 95% explained-variance ratio decreased the number of features from 16384 to 7308 which is really high.
- As a result of this analysis, we obtained new datasets have less than half of the number of features with preserving the 95% variances. Thus, we gained much time and compiling of all datasets takes max 1-2 days.

### Server Specs we used:
- Dell R720, 2 x Intel Xeon E5-2620V2 / 2.1 GHz 24core vCPU, 128GB Ram, 2.4 TB Storage.

