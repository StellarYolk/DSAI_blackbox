1. Species Count (Bar Chart)
What it shows: A category count of the target column (Species) comparing Iris-setosa, Iris-versicolor, and Iris-virginica.

Graphical Interpretation:

All three bars reach an identical height of 50 count.

Key Finding: The dataset is perfectly balanced. There is no class imbalance bias, meaning a machine learning model trained on this dataset will receive equal exposure to all three classes during training.

2. Sepal Length vs Petal Length (Scatter Plot)
What it shows: The relationship between two continuous feature variables across all three species.

Graphical Interpretation:

Linear Separability: Iris-setosa (red) forms a completely isolated, tight cluster in the bottom-left region of the plot (Petal Length<2.0 cm).

Feature Correlation: For all species, as sepal length increases, petal length tends to increase as well (a positive trend).

Overlap: Iris-versicolor (blue) and Iris-virginica (green) show a slight region of overlap between 4.5 cm and 5.0 cm petal length, indicating that classification between these two species relies on additional features (like petal width).

3. Distribution of Petal Length (Histogram)
What it shows: The frequency distribution and spread of values for the PetalLengthCm measurement across all 150 flower samples.

Graphical Interpretation:

Bimodal Distribution: The histogram shows two distinct peaks—one prominent spike around 1.0 cm−1.5 cm and a second broader bell curve between 4.0 cm−6.0 cm.

Data Gap: There is a complete gap (zero frequency) between 2.0 cm and 3.0 cm. This gap visually represents the natural boundary separating Iris-setosa from the other two species.
