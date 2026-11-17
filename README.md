# ResolveIQ 2.0

An intelligent complaint analysis and prioritization platform built with Django, NLP and machine learning.

## Current starter scope
- Django application and URL structure
- Complaint submission and history data model
- Transparent urgency rules
- Modular text preprocessing and ML inference interfaces
- Dark dashboard starter UI

The classifier is intentionally not trained or bundled yet. We will build the dataset preparation, training, evaluation and inference pipeline as separate verified steps.

## Windows setup (PowerShell)

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

If `py -3.11` is unavailable, use an installed Python version supported by the pinned Django release.

## Next development milestones
1. Add and validate the complaint dataset.
2. Build reproducible text preprocessing and model training.
3. Evaluate with macro-F1, per-class metrics and confusion matrix.
4. Connect model inference to complaint submission.
5. Add explainable priority scoring, confidence handling and review queue.
6. Expand dashboard analytics and tests.
