# Tree

- 트리는 싸이클이 없는 무향 연결 그래프이다.
  - 두 노드 사이에는 유일한 경로가 존재한다.
  - 각 노드는 최대 하나의 부모 노드가 존재할 수 있다.
  - 각 노드는 자식 노드가 없거나 하나 이상이 존재할 수 있다.
- 비 선형 구조
  - 원소들 간에 1:n 관계를 가지는 자료구조
  - 원소들 간에 계층관계를 가지는 계층형 자료구조

- 노드 중 부모가 없는 노드를 루트라 한다.
- 나머지 노드들은 n개의 분리 집합으로 분리 될 수 있다. (서브트리)
- 단말 노드(리프 노드)
- 노드, 간선, 로트 노드
- 형제 노드, 조상 노드, 서브 트리, 자손 노드
- 차수(degree) : 연결된 자식 노드의 수
- 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값

- 높이 : 루트에서 노드에 이르는 간선의 수
- 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값, 최대 레벨
- 이진 트리 : 모든 노드들이  최대 2개의 서브 트리를 갖는 특별한 형태의 트리
  - 각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리
  - 왼쪽 자식 노드, 오른쪽 자식 노드

- 포화 이진 트리 : 모든 레벨에 노드가 포화상태로 채어져 있는 이진 트리
  - 루트를 1번으로 하여 이진트리 최대 노드 (2^(h+1)-1)번까지 번호가 있는 트리
- 완전 이진 트리 : 높이가 h이고 노드 수가 n개일 때(단, 2^h <= n < 2^(h+1)-1), 포화 이진 트리의 노드 번호가 1번부터 n번까지 빈자리가 없는 이진 트리
- 편향 이진 트리 : 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진트리
  - 왼쪽 편향 이진트리
  - 오른쪽 편향 이진트리
- 순회(traversal) : 트리의 각 노드를 중복되지 않게 전부 방문(visit)하는 것을 말하는데 트리는 비 선형 구조이기 때문에 선형구조에서와 같이 선후 연결 관계를 알 수 없다. 따라서 특별한 방법이 필요하다.
-    









