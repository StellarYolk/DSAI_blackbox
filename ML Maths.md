## MAL100 — Mathematics I

### 🟢 Directly Used in ML

| Topic | ML Relevance |
|---|---|
| **Partial derivatives** | Core of backpropagation; computing gradients of loss functions |
| **Gradient** | Gradient descent — the backbone of all model training |
| **Chain rule** (multivariable) | Backpropagation through computational graphs |
| **Maxima & Minima** (multivariable) | Loss minimization; finding optimal model parameters |
| **Lagrange multiplier method** | Constrained optimization (e.g., SVM margin maximization) |
| **Directional derivatives** | Understanding gradient direction in parameter space |
| **Definite integrals** | Probability distributions, expected value computation |
| **Improper integrals** | Normalization of continuous probability distributions |

### 🟡 Foundational / Indirectly Used

| Topic | ML Relevance |
|---|---|
| **Limits & Continuity** | Understanding loss function behavior; activation function design |
| **Convergence of sequences** | Understanding when iterative algorithms (like gradient descent) converge |
| **Cauchy sequences** | Theoretical basis for optimizer convergence proofs |
| **Mean Value Theorem** | Theoretical guarantees in optimization |
| **Rolle's Theorem** | Underpins proof of gradient-based convergence theorems |
| **Double & Triple integrals** | Marginalizing joint distributions in probabilistic ML |
| **Change of variables** | Normalizing flows; reparameterization trick in VAEs |

### 🔴 Low Direct Relevance

| Topic | ML Relevance |
|---|---|
| Series convergence tests (ratio, root, Leibnitz) | Rarely used directly; useful in theoretical proofs |
| Green's theorem, Stokes' theorem, Gauss's divergence theorem | Mostly irrelevant to standard ML; niche use in physics-informed NNs |
| Surface integrals, line integrals, vector fields | Same as above |
| Area, volume, surface area via integrals | Not directly used |

---

## MAL101 — Mathematics II

### 🟢 Directly Used in ML

| Topic | ML Relevance |
|---|---|
| **Eigenvalues & Eigenvectors** | PCA (dimensionality reduction), spectral clustering, covariance analysis |
| **Diagonalization** | Efficient matrix computations; PCA decomposition |
| **Inner product spaces** | Kernel methods (SVM, kernel PCA); similarity measures |
| **Gram-Schmidt process** | QR decomposition; orthogonalization in numerical methods |
| **Orthonormal bases** | Feature decorrelation; efficient representations |
| **Rank of a matrix** | Detecting redundant features; understanding model capacity |
| **Systems of linear equations** (Gauss elimination, LU) | Solving normal equations in linear regression |
| **Linear independence** | Feature independence; avoiding multicollinearity |
| **Real quadratic forms** | Convexity analysis of loss functions; positive definiteness checks |
| **Cayley-Hamilton theorem** | Matrix function computation; used in advanced optimization |

### 🟡 Foundational / Indirectly Used

| Topic | ML Relevance |
|---|---|
| **Vector spaces & subspaces** | Conceptual foundation for feature spaces, embedding spaces |
| **Linear transformations** | Every neural network layer is a linear transformation |
| **Range space & Null space** | Understanding what a model can and cannot represent |
| **Rank-Nullity theorem** | Analyzing layer expressiveness in neural networks |
| **Spanning space & Basis** | Basis of representation learning |
| **Matrix representations** | Weight matrices in neural networks |
| **First Order ODE** | Continuous-time models; Neural ODEs |
| **Lipschitz condition** | Gradient clipping; stability of training; Wasserstein GANs |
| **Linear ODE (higher order)** | Dynamical systems; recurrent network analysis |
| **Laplace Transform** | Signal processing features; time-series ML |

### 🔴 Low Direct Relevance

| Topic | ML Relevance |
|---|---|
| Hermitian / Skew-Hermitian / Unitary matrices | Niche; relevant in quantum ML only |
| Cauchy-Euler equations | Rarely appears outside physics-based ML |
| Method of undetermined coefficients / variation of parameters | ODE solving techniques; not directly used in standard ML |
| Wronskian & linear dependence of ODE solutions | Theoretical; not applied in typical ML workflows |
| Picard's theorem | Theoretical existence-uniqueness; background knowledge |

---


The most ML-critical topics across both courses are: **gradients & chain rule**, **eigenvalues & eigenvectors**, **inner product spaces**, **linear systems**, and **convergence** — these five areas underpin nearly every ML algorithm


---

## How to learn all of this

- try to learn from NPTEL courses from youtube, they will teach you the bare minimum for understanding ML
- The whatsapp group is always open for doubts
- Try to use claude for doubts and advanced problem & conceptual understanding


