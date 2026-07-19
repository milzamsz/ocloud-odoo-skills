# Evaluation Improvement Prompt

Analyze trigger and outcome failures for the selected skill.

Classify each failure as:

- description false positive;
- description false negative;
- scope overlap;
- missing procedure;
- incorrect or stale reference;
- unsafe behavior;
- output contract failure;
- fixture defect;
- evaluator defect;
- model variance.

Create the smallest change that fixes the failure without overfitting. Preserve a held-out validation set and rerun adjacent skill regressions. Compare usefulness and token overhead with the previous version.
