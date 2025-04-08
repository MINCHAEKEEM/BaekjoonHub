import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 최소 힙 생성
    mix_count = 0

    while len(scoville) >= 2 and scoville[0] < K:
        first = heapq.heappop(scoville)      # 가장 맵지 않은 음식
        second = heapq.heappop(scoville)     # 두 번째로 맵지 않은 음식
        new_food = first + (second * 2)      # 섞은 음식의 스코빌 지수
        heapq.heappush(scoville, new_food)   # 다시 힙에 추가
        mix_count += 1

    # 마지막 남은 음식의 스코빌 지수가 K 이상인지 확인
    return mix_count if scoville[0] >= K else -1