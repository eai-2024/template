import typing as tp
from collections import defaultdict

import community as community_louvain
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

from vkapi.friends import get_mutual

# Типизация для структуры MutualFriends
class MutualFriends(tp.TypedDict):
    id: int
    common_friends: tp.List[int]
    common_count: int

def ego_network(user_id: int, friends: tp.List[int]) -> tp.List[tp.Tuple[int, int]]:
    edges = []

    # Получаем связи между пользователем и его друзьями, если есть общие
    mutual_friends: tp.List[MutualFriends] = get_mutual(source_uid=user_id, target_uids=friends)
    
    valid_friends = {mf["id"] for mf in mutual_friends if mf["common_count"] > 0}

    for friend in friends:
        if (
            friend in valid_friends
            and user_id != friend
            and user_id in [mf["id"] for mf in mutual_friends if friend in mf["common_friends"]]
        ):
            edges.append((user_id, friend))

    for mutual in mutual_friends:
        source = mutual["id"]
        for common_friend in mutual["common_friends"]:
            if (
                source != common_friend and (source, common_friend) not in edges
            ):  # Исключаем самосвязи и дубликаты
                edges.append((source, common_friend))

    return edges


def plot_ego_network(net: tp.List[tp.Tuple[int, int]]) -> None:
    graph = nx.Graph()
    graph.add_edges_from(net)
    layout = nx.spring_layout(graph)
    nx.draw(graph, layout, node_size=10, node_color="black", alpha=0.5)
    plt.title("Ego Network", size=15)
    plt.show()


def plot_communities(net: tp.List[tp.Tuple[int, int]]) -> None:
    graph = nx.Graph()
    graph.add_edges_from(net)
    layout = nx.spring_layout(graph)
    partition = community_louvain.best_partition(graph)
    nx.draw(graph, layout, node_size=25, node_color=list(partition.values()), alpha=0.8)
    plt.title("Ego Network", size=15)
    plt.show()


def get_communities(net: tp.List[tp.Tuple[int, int]]) -> tp.Dict[int, tp.List[int]]:
    communities = defaultdict(list)
    graph = nx.Graph()
    graph.add_edges_from(net)
    partition = community_louvain.best_partition(graph)
    for uid, cluster in partition.items():
        communities[cluster].append(uid)
    return communities


def describe_communities(
    clusters: tp.Dict[int, tp.List[int]],
    friends: tp.List[tp.Dict[str, tp.Any]],  # Типизация для списка друзей
    fields: tp.Optional[tp.List[str]] = None,
) -> pd.DataFrame:
    if fields is None:
        fields = ["first_name", "last_name"]

    data = []
    for cluster_n, cluster_users in clusters.items():
        for uid in cluster_users:
            for friend in friends:
                if uid == friend["id"]:
                    data.append([cluster_n] + [friend.get(field) for field in fields])  # type: ignore
                    break
    return pd.DataFrame(data=data, columns=["cluster"] + fields)
