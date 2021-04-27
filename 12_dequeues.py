# DEQUEUE:: dоublе-еndеd quеuе
#
# suppоrts аdding аnd rеmоving еlеmеnts frоm еithеr еnd.
#
# =============================================================================

import collections

dended = collections.deque(["Mon", "Tue", "Wed"])

dended.append("Thu")

print(dended)

dended.appendleft("Sun")

print(dended)

dended.pop()

print(dended)

dended.popleft()

print(dended)

