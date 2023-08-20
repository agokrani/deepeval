"""Tests for answer relevancy
"""
import pytest

list1 = ["a", "b"]
list2 = ["b", "c"]
list3 = ["b", "a"]

list_dict_1 = [{"text": "a"}, {"text": "b"}]
list_dict_2 = [{"text": "b"}, {"text": "c"}]


@pytest.mark.asyncio
async def test_answer_relevancy():
    from deepeval.test_utils import assert_ranking_similarity

    assert_ranking_similarity(list1, list2, success_threshold=0.4)


@pytest.mark.asyncio
async def test_query_answer_relevancy():
    from deepeval.metrics.ranking_similarity import RankingSimilarity

    scorer = RankingSimilarity(success_threshold=0.5)
    result = scorer.measure(list_1=list1, list_2=list2)
    result_2 = scorer.measure(list_1=list1, list_2=list3)
    assert result_2 > result, "Ranking not working."


@pytest.mark.asyncio
async def test_query_answer_relevancy_dict():
    from deepeval.metrics.ranking_similarity import RankingSimilarity

    scorer = RankingSimilarity(success_threshold=0.5)
    result = scorer.measure(list_1=list_dict_1, list_2=list_dict_2)
    assert scorer.is_successful(), "Ranking dicts not working."
    