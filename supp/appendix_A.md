# Appendix A: Analysis of Metrics

Overview Table: 

| Name          | Example sequence                            | $DRR$                                                | $RRdist$                                             | $Uniq$                               | $Gini$                                                   |
|---------------|---------------------------------------------|------------------------------------------------------|------------------------------------------------------|--------------------------------------|----------------------------------------------------------|
| Specific      | $[a, b, a, b, b, c]$                        | 0.2                                                  | 0.5                                                  | 0.4 $if &#124;L_j&#124; \geq 6$      | $0.6\dot{1}$                                             |
| All same      | $[a, a, \ldots, a]$                         | 1.0                                                  | 1.0                                                  | 0.0                                  | 0.0                                                      |
| Alternating   | $[a, b, a, b, \ldots, a, b]$                | 0.0                                                  | 0.5                                                  | $1/(&#124;L_j&#124;-1)$              | 0.5                                                      |
| All different | $[a, b, c, \ldots, j] $                     | 0.0                                                  | 0.0                                                  | 1.0                                  | $lim_{n \to \infty} = 1$                                 |
| Encased       | $[a, b, b, \ldots, b, a]$                   | $lim_{n \to \infty} = 1$                             | 0.5                                                  | $1/(&#124;L_j&#124;-1)$              | $lim_{n \to \infty} = 0$                                 |
| Random        | $[rand(L_j), rand(L_j), \ldots, rand(L_j)]$ | $lim_{n \to \infty}\mathbb{E}[S]= 1/&#124;L_j&#124;$ | $lim_{n \to \infty}\mathbb{E}[S]= 1/&#124;L_j&#124;$ | $lim_{n \to \infty}\mathbb{E}[S]= 1$ | $lim_{n \to \infty}\mathbb{E}[S]= 1-(1/&#124;L_j&#124;)$ |

## Direct Repetition Ratio (DRR)

$$DRR(S) = 1/(n-1) \sum_{i=1}^{n-1} 1_{l_i = l_{i+1}}$$

When considering the example sequences, we observe the in the *specific* example sequence one out of five sequential pairs is a direct repetition (i.e., $1/5$). Note that higher order patterns (e.g., *alternating* sequences) do not impact the value. Therefore, singular outliers (e.g., in the *encased* sequence) will only marginally affect the value. The convergence behavior of *random* sequences depends on the size of the label space.

## Reciprocal Repeat Distance (RRdist)

$$RRdist(S) = \frac{\sum_{i=1}^{n-1}\sum_{j=2}^{n} 1_{i < j, l_i = l_j \wedge l_i \neq l_k, \forall k, i < k < j}}{\sum_{i=1}^{n-1}\sum_{j=2}^{n} (j-i)1_{i < j, l_i = l_j \wedge l_i \neq l_k, \forall k, i < k < j}}$$

Concerning the *specific* example, $a$ has a distances of one and two, while $b$ has a distance of three, which results in an average distance of two (i.e., reciprocal value of $0.5$). Note that metric capture higher order patterns, such as both the *alternating and *encased* sequence having a distance of $0.5$.  In the former case, the distance is always two, while in the latter case, $n-3$ times a distance of one and one time a distance of $n-1$ resulting of $n-2$ repetition events (i.e., $\frac{n-2}{(n-3)*1+1*(n-1)}$). Similar to DDR, the limit of a *random* sequence approaches the reciprocal value of the label space.

## Uniqueness Index (Uniq)

$$Uniq(S) = \frac{|\{S\}|-1}{min(|S|,|L_j|)-1}$$

In Table~\ref{tab:sequence_examples}, the *specific* sequence is $(3-1)/(6-1)$ as three of potentially six labels are present. If *all* items are the *same*, then the minimum of zero is reached (which is why one is deducted from both the enumerator and denominator). The value tends towards one for long *random* sequences. Therefore, the metric is a form of coverage on the sequence level rather than system level.

## Distribution Imbalance (Gini)

$$Gini(S) = 1 - \sum_{l \in L_j} (p_l)^2, \quad p_l = \frac{1}{|S|} \sum_{i=1}^{n} \mathbb{1}_{l_i = l}$$

The *specific* example is thus the result of $1-((1/6)^2+(2/6)^2+(3/6)^2)$. Gini is $0$ with *all same* sequence, has $0.5$ with two labels equally distributed (e.g., *alternatin* sequence), and tends towards $1$ as long sequence of *all different* labels. Similar to DDR, singular outliers do not significantly affect the outcome on long sequences (e.g., consider *encased*). For long *random* sequences, the value depends on the size of the label space.
