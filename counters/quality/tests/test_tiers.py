from quality.tiers import ALL_QUALITIES


class TestQualityTiers:
    """The five quality tiers shared across every domain (vehicle crews,
    infantry units, and any future domain) that needs a common vocabulary
    for unit experience/training level."""

    def test_five_tiers_in_descending_order(self):
        assert ALL_QUALITIES == ("elite", "veteran", "regular", "green", "militia")

    def test_all_tiers_are_distinct(self):
        assert len(set(ALL_QUALITIES)) == 5
