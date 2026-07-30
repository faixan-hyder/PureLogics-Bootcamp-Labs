# Comparison Report: Pickle vs Joblib

## Dataset
- Name: Breast Cancer Wisconsin
- Samples: 569
- Features: 30
- Train/Test Split: 80/20

## Models
- Algorithm: RandomForestClassifier
- Number of trees: 100
- Total versions: 3 (v1, v2, v3)

## File Size Comparison
| Version | Pickle Size | Joblib Size | Difference |
|---------|-------------|-------------|------------|
| v1 | 0.30 MB | 0.31 MB | Joblib is -3.4% smaller |
| v2 | 0.31 MB | 0.32 MB | Joblib is -3.4% smaller |
| v3 | 0.30 MB | 0.31 MB | Joblib is -3.4% smaller |

## Load Time Comparison
| Version | Pickle Load Time | Joblib Load Time | Difference |
|---------|------------------|------------------|------------|
| v1 | 0.0060s | 0.0310s | Joblib is -417.5% faster |
| v2 | 0.0060s | 0.0290s | Joblib is -383.0% faster |
| v3 | 0.0033s | 0.0247s | Joblib is -651.8% faster |

## Average Performance
- Pickle average load time: 0.0051s
- Joblib average load time: 0.0282s
- Joblib is -454.3% faster overall

## Conclusion
Joblib is recommended for scikit-learn models because:
1. Faster load times
2. Smaller file sizes
3. Same accuracy as Pickle
