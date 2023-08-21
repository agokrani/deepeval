# Alert Score

Alert score checks if a generated output is good or bad. It automatically checks for:

- Factual consistency
- Answer relevancy
- Toxicness (coming soon)

It then takes the minimum of those scores to alert.

## Assert Alert Score

```python
from deepeval.metrics.alert_score import assert_alert_score
assert_alert_score(
    generated_text="Who won the FIFA World Cup in 2018?",
    expected_output="French national football team",
    context="The FIFA World Cup in 2018 was won by the French national football team. They defeated Croatia 4-2 in the final match to claim the championship.",
    minimum_score=0.3
)
```

## Metric

```python
from deepeval.metrics.alert_score import AlertScoreMetric
metric = AlertScoreMetric()
score = metric.measure(
    generated_text="Who won the FIFA World Cup in 2018?",
    expected_output="French national football team"
)
score
```