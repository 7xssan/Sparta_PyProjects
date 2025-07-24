frozen_set = frozenset(["hello", "world"])
# cannot alter frozen set after it is made, frozen sets are immutable
normal_set = {"lets", "learn"}
frozen_set = frozen_set.union(normal_set)
print(frozen_set)