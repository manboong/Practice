# Programming Practice

군 생활 동안 부족하다고 느낀 코딩 역량과 꾸준함을 훈련하고, Python과 R을 함께 연습하기 위한 저장소입니다.

## Structure

```text
Practice/
├── python/
│   └── solutions/      # Python algorithm / LeetCode practice
├── r/
│   ├── basics/         # R syntax and core data structures
│   ├── statistics/     # Probability and statistics practice
│   ├── data-analysis/  # Data wrangling and visualization
│   └── network/        # Graph analysis, random graphs, SBM practice
└── .devcontainer/      # GitHub Codespaces environment for Python + R
```

## Codespaces

The dev container includes Python and R, together with VS Code extensions for both languages.

R packages installed automatically when the Codespace is created:

- `languageserver`
- `tidyverse`
- `igraph`

After changing the dev container configuration, run **Codespaces: Rebuild Container** from the Command Palette.
