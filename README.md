# House Pricing Prediction – Comprehensive and Advanced README

## Table of Contents

1. [Project Overview](#project-overview)  
2. [The Problem Statement](#the-problem-statement)  
3. [Dataset Description](#dataset-description)  
4. [Code Breakdown and Explanation](#code-breakdown-and-explanation)  
5. [Data Preprocessing & Leakage Prevention](#data-preprocessing--leakage-prevention)  
6. [Handling Missing Data: MCAR, MAR, MNAR](#handling-missing-data-mcar-mar-mnar)  
7. [Feature Engineering: Transformations & Categorical Encoding](#feature-engineering-transformations--categorical-encoding)  
8. [Machine Learning Models & Mathematical Foundations](#machine-learning-models--mathematical-foundations)  
9. [Model Performance Analysis & Interpretation](#model-performance-analysis--interpretation)  
10. [Feature Importance & Statistical Justifications](#feature-importance--statistical-justifications)  
11. [Decision-Making](#decision-making)  
12. [Why Random Forest Performed Best](#why-random-forest-performed-best)  
13. [Conclusion](#conclusion)

---

## 1. Project Overview

This project uses advanced machine learning techniques combined with robust statistical and probabilistic methods to predict house prices. Key goals include:

- **Rigor in Data Handling:** Avoiding leakage via statistically validated splits and correlation checks.
- **Probabilistic Missing Data Imputation:** Addressing various missing data mechanisms (MCAR, MAR, MNAR) with KNN and iterative imputation methods.
- **Advanced Feature Engineering:** Applying power and log transformations to normalize distributions, and careful categorical encoding to preserve underlying patterns.
- **Mathematically-Informed Model Selection:** Comparing multiple models with emphasis on the bias-variance tradeoff, while underpinning each model’s approach with mathematical justification.
- **Actionable Economic Insights:** Translating statistical findings into clear decision-making strategies, particularly for real estate investments.

---

## 2. The Problem Statement

Our objective is to build an interpretable and robust model to predict **SalePrice** from structured real estate data. Challenges include:

- **Handling Missing Data:** Determining whether missingness is MCAR, MAR, or MNAR, and applying proper imputation techniques.
- **Preventing Data Leakage:** Ensuring no feature unduly biases the model by leaking information from the target.
- **Feature Importance:** Identifying influential predictors both statistically and economically.
- **Balancing Bias and Variance:** Crafting models that generalize well to unseen data, particularly using ensemble methods such as Random Forest.

Mathematically, we define the prediction task as approximating the mapping function $\( f: \mathbb{R}^d \rightarrow \mathbb{R} \)$ such that:
$$\[
\hat{y} = f(\mathbf{x})
\]$$
where $\(\mathbf{x} \in \mathbb{R}^d\)$ are the features and $\(\hat{y}\)$ is the predicted house price.

---

## 3. Dataset Description

The dataset includes:

- **Numerical Features:** e.g., Lot size, square footage, number of rooms.
- **Categorical Features:** e.g., Neighborhood, house style, zoning classification.
- **Target Variable:** SalePrice (the house price).

### Exploratory Data Analysis (EDA)
- **Price Distribution:** SalePrice exhibits a positively skewed distribution. A log transformation is applied, mathematically represented as:
  $$\[
  y_{\text{transformed}} = \log(y + c)
  \]$$
  where $\( c \)$ is a constant to ensure positivity.
- **Correlation Analysis:** Pearson correlation coefficients are computed:
  $$\[
  r_{X,Y} = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^{n}(X_i - \bar{X})^2 \sum_{i=1}^{n}(Y_i - \bar{Y})^2}}
  \]$$
  to identify multicollinearity and guide feature selection.
- **Outlier Detection:** Both the Interquartile Range (IQR) method and Z-score analysis are used:
  $$\[
  Z_i = \frac{X_i - \mu_X}{\sigma_X}
  \]$$
  where $\(\mu_X\)$ and $\(\sigma_X\)$ are the mean and standard deviation of feature $\(X\)$, respectively.

---

## 4. Code Breakdown and Explanation

The code workflow is structured as follows:

1. **Preprocessing:**
   - **Dropping Irrelevant Features:** For instance, the unique identifier (`Id`) is removed to avoid introducing artificial patterns.
   - **Missing Data Handling:** Implementation of KNN and Iterative Imputer (MICE) for missing value estimation.
   - **Transformations:** Log transformations and power transforms are applied to normalize distributions.
   - **Encoding:** One-hot encoding is applied for categorical features, expanding each category into binary columns.

2. **Statistical Validation:**
   - **Normality Testing:** The Kolmogorov-Smirnov test is used to compare empirical distributions with theoretical ones:
    $$\[
     D = \sup_x |F_n(x) - F(x)|
     \]$$
   - **Multicollinearity Check:** The Variance Inflation Factor (VIF) is calculated:
     $$\[
     \text{VIF}(X_i) = \frac{1}{1 - R^2_{X_i}}
     \]$$
     where $\(R^2_{X_i}\)$ is obtained by regressing $\(X_i\)$ against all other predictors.

---

## 5. Data Preprocessing & Leakage Prevention

### Eliminating Data Leakage
A feature may inadvertently “leak” information about the target if its distribution significantly shifts between the training and test sets. To detect this:
- **Pearson Correlation Analysis:** We compute correlations between each feature $\(X_i\)$ and SalePrice before and after the train-test split. A significant increase in correlation post-split suggests potential leakage:
  $$\[
  \Delta r = r_{\text{train}}(X_i, Y) - r_{\text{test}}(X_i, Y)
  \]$$
  A threshold for $\(\Delta r\)$ is established based on statistical significance (e.g., via Fisher’s Z-transformation).

---

## 6. Handling Missing Data: MCAR, MAR, MNAR

### Statistical and Probabilistic Framework

- **MCAR (Missing Completely at Random):**
  $$\[
  P(R \mid X) = P(R)
  \]$$
  where $\(R\)$ is the missingness indicator. No systematic bias is present.

- **MAR (Missing at Random):**
  $$\[
  P(R \mid X, Y) = P(R \mid X)
  \]$$
  Missingness is related to observed features, justifying the use of regression-based imputation methods.

- **MNAR (Missing Not at Random):**
  $$\[
  P(R \mid X, Y) \neq P(R \mid X)
  \]$$
  Imputation requires careful modeling (e.g., using expectation-maximization algorithms) as missingness depends on unobserved variables.

### Imputation Techniques:
- **KNN Imputation:**  
  Uses distance metrics (e.g., Euclidean distance) to impute missing values based on the $\(k\)$ nearest neighbors.
- **Iterative Imputation (MICE):**  
 <p>Models each feature with missing values as a function of other features iteratively. Mathematically, each missing value $\hat{x}_i$ is updated by:</p>
<p>$$  \hat{x}_i = \mathbb{E}[X_i \mid \mathbf{X}_{-i}]
  $$</p>
<p>where $\mathbf{X}_{-i}$ are the observed features.</p>

---

## 7. Feature Engineering: Transformations & Categorical Encoding

### Transformation Techniques:
- **Log & Power Transformations:**  
  Reduce skewness and stabilize variance. For a variable $\(X\)$, a power transformation might be:
  $$\[
  X' = \frac{X^\lambda - 1}{\lambda}, \quad \lambda \neq 0
  \]$$
  When $\(\lambda \rightarrow 0\)$, this approximates the logarithmic transformation.

### Categorical Encoding:
- **One-Hot Encoding:**  
 <p>Converts a categorical variable into a set of binary variables:</p>
<p>$$
  X_{\text{neighborhood}} \rightarrow \{ \mathbb{1}_{\{\text{neighborhood} = n\}} \}_{n=1}^{N}
  $$</p>
  **Why the “Neighborhood” Feature May Not Appear Strongly Correlated Initially:**  
  - **Dilution Across Dummies:** When a categorical variable is one-hot encoded, the impact is spread across multiple binary features. Individually, these binary indicators may show a low Pearson correlation with the target due to their binary nature and lower variance. However, collectively they capture important latent information.
  - **Interaction Effects:** The influence of “Neighborhood” may be indirect, affecting other variables (e.g., lot size, quality ratings). This indirect influence may only become apparent when examining multivariate models or via interaction terms.
  - **Non-Linear Relationships:** Linear correlation coefficients might fail to capture the non-linear or threshold-based effects of categorical variables on price.

- **Scaling:**  
  Numeric features are standardized using StandardScaler:
  $$\[
  X_{\text{scaled}} = \frac{X - \mu_X}{\sigma_X}
  \]$$
---

## 8. Machine Learning Models & Mathematical Foundations

### Bias-Variance Decomposition:
<p>For any estimator $\hat{f}$, the expected prediction error can be decomposed as:</p>
<p>$$
\mathbb{E}\left[(Y - \hat{f}(X))^2\right] = \underbrace{\left(\mathbb{E}[\hat{f}(X)] - f(X)\right)^2}_{\text{Bias}^2} + \underbrace{\mathbb{E}\left[(\hat{f}(X) - \mathbb{E}[\hat{f}(X)])^2\right]}_{\text{Variance}} + \sigma^2_{\text{irreducible}}
$$</p>
- **Random Forest:**  
  <p>Reduces variance via bagging (bootstrap aggregating) and random feature selection. Each tree $(\ f_t(X) )$ contributes to the final prediction</p>:
  <p>$$
  \hat{f}(X) = \frac{1}{T} \sum_{t=1}^T f_t(X)
  $$</p>
  Since each tree has high variance but low bias, the ensemble averages out the variance while keeping bias controlled.

### Other Models:
- **Linear Regression:**  
  Assumes a linear relationship:
  $$\[
  y = \beta_0 + \beta_1 X_1 + \ldots + \beta_d X_d + \epsilon
  \]$$
  Sensitivity to multicollinearity is checked via VIF.
**Gradient Boosting Machines (GBM):**  
Iteratively correct errors:
<p>
$$
\hat{f}_m(X) = \hat{f}_{m-1}(X) + \gamma_m h_m(X)
$$
</p>
<p>where $(\ h_m(X) )$ is the new weak learner and $(\ \gamma_m )$ is the step size.</p>

---

## 9. Model Performance Analysis & Interpretation

### Metrics:
- **R² (Coefficient of Determination):**
<p>
$$
R^2 = 1 - \frac{\sum_{i}(y_i - \hat{y}_i)^2}{\sum_{i}(y_i - \bar{y})^2}
$$
</p>
  This metric explains the proportion of variance in the dependent variable that is predictable from the independent variables.
- **Residual Analysis:**  
  Residuals are analyzed to verify:
  - **Homoscedasticity:** Constant variance across predictions.
  - **Normality:** Using quantile-quantile plots and statistical tests like the Kolmogorov-Smirnov test.

### Visual and Statistical Diagnostics:
- **Learning Curves:** To observe bias/variance tradeoff.
- **Partial Dependence Plots:** To understand the effect of individual features on the prediction, particularly for complex interactions involving categorical variables.

---

## 10. Feature Importance & Statistical Justifications

### Interpreting Feature Importance:
- **Neighborhood's Role:**  
  Although individual one-hot encoded neighborhood variables might show low correlation coefficients, their collective influence is significant. This is because:
  - **Latent Variable Effect:** Neighborhood indirectly impacts house prices through associated variables like lot size, overall quality, and local amenities.
  - **Statistical Significance in Multivariate Models:** When included in regression or ensemble models, the group effect of these variables reduces error variance significantly, as evidenced by partial dependency and permutation importance analyses.
  - **Regularization Insights:** In regularized linear models (like LASSO), groups of correlated dummies may be shrunk together rather than individually selected, highlighting their collective impact.

- **Mathematical Insight:**  
  Consider a group of dummy variables $\( \{D_1, D_2, \ldots, D_k\} \)$ representing neighborhoods. Their joint effect can be modeled as:
  $$\[
  \sum_{j=1}^k \beta_j D_j
  \]$$
  Even if each $\( \beta_j \)$ is modest, the aggregate effect can be large. Furthermore, when assessing multicollinearity, the combined Variance Inflation Factor (VIF) might reveal redundancy if not handled properly, leading to potential underestimation of their true impact.

---

## 11. Decision-Making 

### Translating Statistical Findings into Real-World Decisions:
- **Investment Strategy:**  
  The model indicates that properties with high overall quality (OverallQual) tend to have a ~20% higher sale price. Investors can prioritize such properties for better returns.
- **Neighborhood Analysis:**  
  Neighborhoods with characteristics such as higher lot areas and favorable school districts, though not always linearly correlated with price in isolation, are significant when their indirect effects (captured via categorical encoding) are considered. This suggests targeted investments in regions with latent high demand.
- **Risk Assessment:**  
  Residual analysis and confidence intervals (derived from bootstrapping predictions) provide insights into the risk associated with price predictions, which means more informed decision-making.

---

## 12. Why Random Forest Performed Best

### Mathematical and Practical Justifications:
- **Robust Handling of Missing Data:**  
  Random Forest inherently manages missing values through surrogate splits and averaging over trees.
- **Reduction in Overfitting:**  
  By constructing each tree on a bootstrap sample and considering a random subset of features at each split, the variance is reduced:
  $$\[
  \text{Var}(\hat{f}(X)) \approx \frac{1}{T} \text{Var}(f_t(X)) + \left(1 - \frac{1}{T}\right) \text{Cov}(f_t(X), f_{t'}(X))
  \]$$
- **Interpretability via Feature Importance:**  
  Feature importance scores derived from the decrease in impurity or permutation importance provide actionable insights.
- **Handling Non-Linearities & Interactions:**  
  Random Forest can naturally model complex interactions (e.g., between categorical neighborhoods and numerical lot sizes) without explicit feature engineering.

---

## 13. Conclusion

This advanced analysis combines rigorous statistical validation, probabilistic missing data handling, and mathematically-informed machine learning approaches to deliver robust, interpretable predictions of house prices.
